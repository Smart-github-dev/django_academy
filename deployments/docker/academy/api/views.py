from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from main.models import JsonStore
from api.serializers import JsonSerializer
from accounting.models import Plans, Subscriber, Content
from django.contrib.auth.models import User
from .serializers import PlansSerializer, SubscriberSerializer, ContentSerializer
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

from messenger import get_messenger
from main.models import GitHubActivitys
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django.http import JsonResponse
from django.http import HttpResponse


class JsonViewSet(viewsets.ModelViewSet):
    queryset = JsonStore.objects.all()
    serializer_class = JsonSerializer


class PlansViewSet(viewsets.ModelViewSet):
    queryset = Plans.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PlansSerializer


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SubscriberSerializer

    def get_queryset(self):
        all_subscribers = Subscriber.objects.filter()
        query_params = self.request.query_params

        ## Query based on the email
        email = query_params.get("email")
        if email:
            all_subscribers = all_subscribers.filter(email=email)

        ## Query based on the plan_name
        plan_name = query_params.get("plan_name")
        if plan_name:
            plan = Plans.objects.get(name=plan_name)
            all_subscribers = all_subscribers.filter(plan__id=plan.id)

        ## Query based on the username
        username = query_params.get("username")
        if username:
            user = User.objects.get(username=username)
            all_subscribers = all_subscribers.filter(user=user.id)

        ## Query based on the status
        status = query_params.get("status")
        if query_params.get("status") and status.lower() == "active":
            queryset = queryset.filter(
                payment_confirmation=True, expire_date__gt=timezone.now()
            )

        return all_subscribers


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ContentSerializer


@require_POST
@csrf_exempt
def set_github_activitys(request):
    if request.method == "POST":
        payload = json.loads(request.body)
        event_type = request.headers.get("X-GitHub-Event")
        handle_github_event(event_type, payload)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


def handle_github_event(event_type, payload):
    repo_name = payload["repository"]["name"]
    username = payload["repository"]["owner"]["login"]

    if event_type == "ping":
        description = "Ping event received"
    elif event_type == "push":
        description = "Pushed commits to {}".format(payload["ref"])
        handle_push_event(payload, event_type)
    elif event_type == "pull_request":
        action = payload["action"]
        description = "Pull Request {} in {}".format(action, repo_name)
        handle_pull_request_event(payload)
    elif event_type == "create":
        ref_type = payload["ref_type"]
        ref_name = payload["ref"]
        description = "Created {} {} in {}".format(ref_type, ref_name, repo_name)
        handle_create_event(payload)
    elif event_type == "delete":
        ref_type = payload["ref_type"]
        ref_name = payload["ref"]
        description = "Deleted {} {} in {}".format(ref_type, ref_name, repo_name)
        handle_delete_event(payload)
    elif event_type == "commit_comment":
        commit_id = payload["comment"]["commit_id"]
        description = "Commented on commit {} in {}".format(commit_id, repo_name)
        handle_commit_comment_event(payload)
    elif event_type == "check_run":
        action = payload["action"]
        check_run_name = payload["check_run"]["name"]
        description = "Check Run {} for {} in {}".format(
            action, check_run_name, repo_name
        )
        handle_check_run_event(payload)
    elif event_type == "pull_request_review":
        event_type = "conversation"
        action = payload["action"]
        description = "Pull Request Review {} in {}".format(action, repo_name)
        handle_pull_request_review_event(payload)
    elif event_type == "issues":
        action = payload["action"]
        issue_title = payload["issue"]["title"]
        description = "Issue {} - {} in {}".format(action, issue_title, repo_name)
        handle_issues_event(payload)
    elif event_type == "issue_comment":
        event_type = "comment"
        comment_body = payload["comment"]["body"]
        description = "Commented on issue in {}".format(repo_name)
        handle_issue_comment_event(payload)
    elif event_type == "pull_request_review_comment":
        event_type = "conversation"
        action = payload["action"]
        description = "Pull Request Review Comment {} in {}".format(action, repo_name)
        handle_pull_request_review_comment_event(payload)
    elif event_type == "repository_dispatch":
        action = payload["action"]
        description = "Repository Dispatch {} in {}".format(action, repo_name)
        handle_repository_dispatch_event(payload)
    elif event_type == "repository":
        action = payload["action"]
        description = "Repository {} in {}".format(action, repo_name)
        handle_repository_event(payload)
    elif event_type == "milestone":
        action = payload["action"]
        milestone_title = payload["milestone"]["title"]
        description = "Milestone {} - {} in {}".format(
            action, milestone_title, repo_name
        )
        handle_milestone_event(payload)
    elif event_type == "force-push":
        description = "Force Push event in {}".format(repo_name)
        handle_force_push_event(payload)
    elif event_type == "linked":
        description = "Linked event in {}".format(repo_name)
        handle_linked_event(payload)
    elif event_type == "files_changed":
        description = "Files Changed event in {}".format(repo_name)
        handle_files_changed_event(payload)
    elif event_type == "requested":
        description = "Requested event in {}".format(repo_name)
        handle_requested_event(payload)
    elif event_type == "board":
        description = "Board event in {}".format(repo_name)
        handle_board_event(payload)
    elif event_type == "assign":
        description = "Assign event in {}".format(repo_name)
        handle_assign_event(payload)
    elif event_type == "changed":
        description = "Changed event in {}".format(repo_name)
        handle_changed_event(payload)
    elif event_type == "requested":
        description = "Requested event in {}".format(repo_name)
    else:
        description = "Unknown event type"
    GitHubActivitys.objects.create(
        event_type=event_type,
        github_name=username,
        repo_name=repo_name,
        activity_description=description,
        evnet_content=payload,
        created_date=timezone.now(),
    )
    print("GitHub event received:", description)
    # Additional handling logic


# Add handling methods for each event type
def handle_push_event(payload, event_type):
    # Handle push event logic
    commits = payload["commits"]
    branch = payload["ref"]
    repo_name = payload["repository"]["name"]
    username = payload["repository"]["owner"]["login"]
    branch_name = payload["ref"].split("/")[
        -1
    ]  # Extract the branch name from the full ref
    commits = payload["commits"]

    for commit in commits:
        commit_id = commit["id"]
        commit_message = commit["message"]
        commit_author = commit["author"]["name"]

        description = f'Commit {commit_id} by {commit_author}: "{commit_message}" in {repo_name}:{branch_name}'
        # Additional handling logic
        print(description)
        GitHubActivitys.objects.create(
            event_type=event_type,
            github_name=username,
            repo_name=repo_name,
            activity_description=description,
            evnet_content=payload,
            created_date=timezone.now(),
        )
    # Additional handling logic


def handle_pull_request_event(payload):
    # Handle pull request event logic
    action = payload["action"]
    pull_request_number = payload["pull_request"]["number"]
    pull_request_title = payload["pull_request"]["title"]
    # Additional handling logic


def handle_create_event(payload):
    # Handle create event logic
    ref_type = payload["ref_type"]
    ref_name = payload["ref"]
    # Additional handling logic


def handle_delete_event(payload):
    # Handle delete event logic
    ref_type = payload["ref_type"]
    ref_name = payload["ref"]
    # Additional handling logic


def handle_commit_comment_event(payload):
    # Handle commit comment event logic
    commit_id = payload["comment"]["commit_id"]
    comment_body = payload["comment"]["body"]
    # Additional handling logic


def handle_check_run_event(payload):
    # Handle check run event logic
    action = payload["action"]
    check_run_name = payload["check_run"]["name"]
    # Additional handling logic


def handle_pull_request_review_event(payload):
    # Handle pull request review event logic
    action = payload["action"]
    review_body = payload["review"]["body"]
    # Additional handling logic


def handle_issues_event(payload):
    repo_name = payload["repository"]["name"]
    username = payload["repository"]["owner"]["login"]
    action = payload["action"]
    issue_title = payload["issue"]["title"]
    description = "Issue {} - {} in {}".format(action, issue_title, repo_name)
    # Additional handling logic
    print(description)


def handle_issue_comment_event(payload):
    # Handle issue comment event logic
    comment_body = payload["comment"]["body"]
    # Additional handling logic


def handle_pull_request_review_comment_event(payload):
    # Handle pull request review comment event logic
    action = payload["action"]
    comment_body = payload["comment"]["body"]
    # Additional handling logic


def handle_repository_dispatch_event(payload):
    # Handle repository dispatch event logic
    action = payload["action"]
    # Additional handling logic


def handle_repository_event(payload):
    # Handle repository event logic
    action = payload["action"]
    repository_name = payload["repository"]["name"]
    # Additional handling logic


def handle_milestone_event(payload):
    # Handle milestone event logic
    action = payload["action"]
    milestone_title = payload["milestone"]["title"]
    # Additional handling logic


def handle_force_push_event(payload):
    repo_name = payload["repository"]["name"]
    username = payload["repository"]["owner"]["login"]
    branch_name = payload["ref"].split("/")[-1]
    description = f"Force Push to {branch_name} in {repo_name} by {username}"
    # Additional handling logic
    print(description)


def handle_linked_event(payload):
    repo_name = payload["repository"]["name"]
    username = payload["repository"]["owner"]["login"]
    description = f"Repository {repo_name} linked by {username}"
    # Additional handling logic
    print(description)


def handle_files_changed_event(payload):
    repo_name = payload["repository"]["name"]
    username = payload["repository"]["owner"]["login"]
    files_changed = payload["files"]
    description = f"Files changed in {repo_name} by {username}: {files_changed}"
    # Additional handling logic
    print(description)


def handle_requested_event(payload):
    repo_name = payload["repository"]["name"]
    username = payload["repository"]["owner"]["login"]
    requested_action = payload["action"]
    description = f"Requested action: {requested_action} in {repo_name} by {username}"
    # Additional handling logic
    print(description)


def handle_board_event(payload):
    repo_name = payload["repository"]["name"]
    username = payload["repository"]["owner"]["login"]
    board_event_action = payload["action"]
    description = f"Board event: {board_event_action} in {repo_name} by {username}"
    # Additional handling logic
    print(description)


def handle_assign_event(payload):
    repo_name = payload["repository"]["name"]
    username = payload["repository"]["owner"]["login"]
    assignee = payload["assignee"]["login"]
    description = f"Assignee {assignee} assigned in {repo_name} by {username}"
    # Additional handling logic
    print(description)


def handle_changed_event(payload):
    repo_name = payload["repository"]["name"]
    username = payload["repository"]["owner"]["login"]
    changed_action = payload["action"]
    description = f"Changed action: {changed_action} in {repo_name} by {username}"
    # Additional handling logic
    print(description)
