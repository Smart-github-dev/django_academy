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
        email = query_params.get('email')
        if email:
            all_subscribers = all_subscribers.filter(email=email)

        ## Query based on the plan_name
        plan_name = query_params.get('plan_name')
        if plan_name:
            plan = Plans.objects.get(name=plan_name)
            all_subscribers = all_subscribers.filter(plan__id=plan.id)

        ## Query based on the username
        username = query_params.get('username')
        if username:
            user = User.objects.get(username=username)
            all_subscribers = all_subscribers.filter(user=user.id)

        ## Query based on the status
        status = query_params.get('status')
        if query_params.get('status') and status.lower() == 'active':
            queryset = queryset.filter(payment_confirmation=True, expire_date__gt=timezone.now())

        return all_subscribers

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ContentSerializer

@require_POST
@csrf_exempt
def set_github_activitys(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        for commit in data['commits']:
            print(commit['id'])
            print('\n')
            eventdata={
                'commit_id':commit['id'], 
                'distinct':commit['distinct'], 
                'tree_id':commit['tree_id'],
                'message':commit['message'],
                'author':commit['author'],
                'created_date':commit['timestamp'],
                'url':commit['url'],
                'committer':commit['committer'],
                "added":commit['added'],
                'removed':commit['removed'],
                'modified':commit['modified']
            }
            if not GitHubActivitys.objects.filter(commit_id=commit['id']).exists():
                GitHubActivitys.objects.create(**eventdata)
        return HttpResponse(status=200)  # Return a 200 OK response
    else:
        return HttpResponse(status=405)  

