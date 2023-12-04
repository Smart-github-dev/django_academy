from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from common import get_common_variables, is_folder_has_new_videos, is_video_new, get_new_videos
from main.forms import (RegistrationForm, faqForm, UpdateSubscriptionInfoForm, ContactForm )
from main.models import (NewsletterEmailer, AdminEmailer, FAQEmailer, Feature, Questions, Notification, JsonStore)
from accounting.models import Plans, Subscriber
from django.contrib.auth import update_session_auth_hash
from common import get_common_variables, send_message
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)


# Create your views here.
# def main(request):
#     return render(request,'main.html')

def mentorDashboard(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        videos = get_new_videos()[0:6]
    else:
        return redirect(reverse('/'))
    return render(request,'mentor_dashboard.html',locals())


def mentorHistory(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        videos = get_new_videos()[0:6]
    else: 
        return redirect(reverse('/'))
    return render(request,'mentor_history.html',locals())

def mentorPayPal(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        videos = get_new_videos()[0:6]
    else:
        return redirect(reverse('/'))
    return render(request,'mentor_paypal.html',locals())

def mentorChanges(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        videos = get_new_videos()[0:6]
    else:
        return redirect(reverse('/'))
    return render(request,'mentor_changes.html',locals())

def mentorUpdateUser(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        videos = get_new_videos()[0:6]
    else:
        return redirect(reverse('/'))
    return render(request,'mentor_update_user.html',locals())

def mentorUserInfo(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        videos = get_new_videos()[0:6]
    else:
        return redirect(reverse('/'))
    return render(request,'mentor_userInfo.html',locals())


def mentorUserInfoDetails(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        videos = get_new_videos()[0:6]
    else:
        return redirect(reverse('/'))
    return render(request,'mentor_userdetails.html',locals())

def mentorAccessControl(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        videos = get_new_videos()[0:6]
    else:
        return redirect(reverse('/'))
    return render(request,'mentor_access_control.html',locals())



def mentorManageUser(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        videos = get_new_videos()[0:6]
    else:
        return redirect(reverse('/'))
    return render(request,'mentor_manage_user.html',locals())





   