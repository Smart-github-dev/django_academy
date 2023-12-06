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
        event_type = request.headers.get('X-GitHub-Event')
        data = json.loads(request.body)
        eventdata={
            'event_type' : event_type ,
            'username'   : data['sender']['login'], 
            'url':data['repository']['full_name'], 
            'created_at':data['repository']['updated_at'],
            'evnet_content':data
        }
        GitHubActivitys.objects.create(eventdata)
        return HttpResponse(status=200)
        if event_type == 'ping':
            return 'pong'
        elif event_type=='member':
            data = json.loads(request.body)
            eventdata={
                'event_type' : event_type ,
                'username'   : data['sender']['login'], 
                'url':data['repository']['full_name'], 
                'created_at':data['repository']['updated_at'],
                'evnet_content':data
            }
            GitHubActivitys.objects.create(eventdata)
            return HttpResponse(status=200)
        elif event_type == 'push':
            data = json.loads(request.body)
            eventdata={
                'event_type' : event_type ,
                'username'   : data['sender']['login'], 
                'url':data['repository']['full_name'], 
                'created_at':data['repository']['updated_at'],
                'evnet_content':data
            }
            GitHubActivitys.objects.create(eventdata)
            return HttpResponse(status=200)   
        elif event_type == 'pull_request':
            data = json.loads(request.body)
            eventdata={
                'event_type' : event_type ,
                'username'   : data['sender']['login'], 
                'url':data['repository']['full_name'], 
                'created_at':data['repository']['updated_at'],
                'evnet_content':data
            }
            GitHubActivitys.objects.create(eventdata)
            return HttpResponse(status=200)
        elif event_type == 'issues':
            data = json.loads(request.body)
            eventdata={
                'event_type' : event_type ,
                'username'   : data['sender']['login'], 
                'url':data['repository']['full_name'], 
                'created_at':data['repository']['updated_at'],
                'evnet_content':data
            }
            GitHubActivitys.objects.create(eventdata)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=405)  

