from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.db.models import Prefetch
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from common import get_common_variables, is_folder_has_new_videos, is_video_new, get_new_videos
from main.forms import (RegistrationForm, faqForm, UpdateSubscriptionInfoForm, ContactForm )
from main.models import (NewsletterEmailer, AdminEmailer, FAQEmailer, Feature, Questions, Notification, JsonStore)
from accounting.models import Plans, Subscriber
from main.models import GitHubActivitys
from django.db.models import Count
from django.contrib.auth import update_session_auth_hash
from common import get_common_variables, send_message
from collections import namedtuple
from django.contrib import messages
import logging


logger = logging.getLogger(__name__)


def mentor_dashboard(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        subscribed_users=get_subscribed_users()
        plans_subscription_totals = Plans.objects.annotate(counts=Count('subscriber')).all()
        expired_subscriptions=get_expired_subscriptions()
        paypal_cancellations=get_paypal_cancellations()
        videos = get_new_videos()[0:6]
        github_activity_trakers=get_github_activitys()
    else:
        return redirect(reverse('/'))
    return render(request,'mentor_dashboard.html',locals())


def mentor_history(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        videos = get_new_videos()[0:6]
    else:
        return redirect(reverse('/'))
    return render(request,'mentor_history.html',locals())

def mentor_payPal(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        videos = get_new_videos()[0:6]
    else:
        return redirect(reverse('/'))
    return render(request,'mentor_paypal.html',locals())

def mentor_changes(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        videos = get_new_videos()[0:6]
    else:
        return redirect(reverse('/'))
    return render(request,'mentor_changes.html',locals())

def mentor_update_user(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        videos = get_new_videos()[0:6]
    else:
        return redirect(reverse('/'))
    return render(request,'mentor_update_user.html',locals())

def mentor_user_info(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        videos = get_new_videos()[0:6]
    else:
        return redirect(reverse('/'))
    return render(request,'mentor_userInfo.html',locals())

def mentor_user_info_details(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        videos = get_new_videos()[0:6]
    else:
        return redirect(reverse('/'))
    return render(request,'mentor_userdetails.html',locals())

def mentor_access_control(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        videos = get_new_videos()[0:6]
    else:
        return redirect(reverse('/'))
    return render(request,'mentor_access_control.html',locals())

def mentor_manage_user(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        videos = get_new_videos()[0:6]
    else:
        return redirect(reverse('/'))
    return render(request,'mentor_manage_user.html',locals())

def get_subscribed_users():
    new_subscribeds = []
    new_subscriber=namedtuple("subscribers",['plan_name','user_name','first_name','last_name','date','email'])
    subscribeds=Plans.objects.prefetch_related("subscriber_set").all()
    for plan in  subscribeds:
        for subscriber in plan.subscriber_set.order_by('created_date')[:1]:
            new_subscribeds.append(
                new_subscriber(
                    plan_name=plan.name,
                    user_name=subscriber.user.username,
                    first_name=subscriber.first_name,
                    last_name=subscriber.last_name,
                    date=subscriber.created_date.strftime('%d/%m/%Y'),
                    email=subscriber.email
                )
            )
    return new_subscribeds

def get_expired_subscriptions(): 
    expired_subscribers = []
    new_subscriber=namedtuple("subscribers",['plan_name','user_name','first_name','last_name','date','email'])
    subscribeds=Plans.objects.prefetch_related("subscriber_set").all()
    current_date = datetime.now()
    for plan in subscribeds:
            for subscriber in plan.subscriber_set.filter(expire_date__lt=current_date).order_by('expire_date')[:1]:
                expired_subscribers.append(
                    new_subscriber(
                        plan_name=plan.name,
                        user_name=subscriber.user.username,
                        first_name=subscriber.first_name,
                        last_name=subscriber.last_name,
                        date=subscriber.expire_date.strftime('%d/%m/%Y'),
                        email=subscriber.email
                    )
                )
    return expired_subscribers

def get_paypal_cancellations():
    payal_canceled_subscribers = []
    new_subscriber=namedtuple("subscribers",['user_name','first_name','last_name','date'])
    subscribeds=Subscriber.objects.filter(status='canceled')[:4]
    for subscriber in subscribeds:
        payal_canceled_subscribers.append(
            new_subscriber(
                user_name=subscriber.user.username,
                first_name=subscriber.first_name,
                last_name=subscriber.last_name,
                date=subscriber.created_date.strftime('%d/%m/%Y')
            )
        )
    return payal_canceled_subscribers


def get_github_activitys():
    github_activitys = []
    new_activitys=namedtuple("activitys",['event_id','event_type','user_name','repo_name','created_date'])
    for ativity in GitHubActivitys.objects.all()[:4]:
        github_activitys.append(
            new_activitys(
                event_id=ativity.event_id,
                event_type=ativity.event_type,
                user_name=ativity.user_name,
                repo_name=ativity.repo_name,
                created_date=ativity.created_date.strftime('%d/%m/%Y')
            )
        )
    return github_activitys

def set_github_activitys(request):
    logger.info(f"listen event from github")
    print(request)
    # if response.status_code == 200:
    #     data = response.json()
    #     for event in data:
    #         eventdata={
    #             'event_id':event['id'], 
    #             'event_type':event['type'], 
    #             'user_name':event['actor']['login'],
    #             'repo_name':event['repo']['name'],
    #             'created_date':event['created_at']
    #         }
    #         if not GitHubActivitys.objects.filter(event_id=event['id']).exists():
    #             GitHubActivitys.objects.create(**eventdata)


        
 