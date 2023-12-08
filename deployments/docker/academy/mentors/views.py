from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.db.models import Prefetch
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from mentors.models import Users_activity
from django.http import HttpResponse
from django.db.models import Q

import math

from common import (
    get_common_variables,
    is_folder_has_new_videos,
    is_video_new,
    get_new_videos,
)
from main.forms import (
    RegistrationForm,
    faqForm,
    UpdateSubscriptionInfoForm,
    ContactForm,
)
from main.models import (
    NewsletterEmailer,
    AdminEmailer,
    FAQEmailer,
    Feature,
    Questions,
    Notification,
    JsonStore,
)
from accounting.models import Plans, Subscriber
from main.models import GitHubActivitys
from django.db.models import Count
from django.contrib.auth import update_session_auth_hash
from common import get_common_variables, send_message
from collections import namedtuple
from django.contrib import messages
import logging
import json


logger = logging.getLogger(__name__)


@login_required
def mentor_dashboard(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        subscribed_users = get_subscribed_users()
        plans_subscription_totals = Plans.objects.annotate(
            counts=Count("subscriber")
        ).all()
        expired_subscriptions = get_expired_subscriptions()
        paypal_cancellations = get_paypal_cancellations(Subscriber.objects.all()[0:4])

        github_activity_trakers = get_github_activitys()
    else:
        return redirect(reverse("/"))
    return render(request, "mentor_dashboard.html", locals())


@login_required
def mentor_history(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        deactived_users = get_deactived_users()
        paypal_cancellations = get_paypal_cancellations(Subscriber.objects.all()[0:4])
        change_historys = list(
            map(history_change_date, Users_activity.objects.all()[0:4])
        )
    else:
        return redirect(reverse("/"))
    return render(request, "mentor_history.html", locals())


@login_required
def mentor_payPal(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        param1 = request.GET.get("s")
        param2 = request.GET.get("e")
        search = request.GET.get("search")
        if search is not None:
            subscribeds = Subscriber.objects.filter(
                Q(status="canceled")
                & (Q(user__username__icontains=search) | Q(email__icontains=search))
            )
        else:
            search = ""
            subscribeds = Subscriber.objects.filter(status="canceled")

        totalnum = subscribeds.count()
        pagination = get_pagination(param1, param2, totalnum)
        start_index = pagination["param1"] * pagination["param2"]
        end_index = start_index + pagination["param2"]
        paypal_cancellations = get_paypal_cancellations(
            subscribeds[start_index:end_index]
        )
    else:
        return redirect(reverse("/"))
    return render(request, "mentor_paypal.html", locals())


def subscriber_change_date(subscriber):
    subscriber.created_date = subscriber.created_date.strftime("%d/%m/%Y")
    return subscriber


def history_change_date(history):
    history.created_at = history.created_at.strftime("%d/%m/%Y")
    return history


@login_required
def mentor_changes(request):
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        param1 = request.GET.get("s")
        param2 = request.GET.get("e")
        search = request.GET.get("search")
        if search is not None:
            historys = Users_activity.objects.filter(
                Q(mentor_name__icontains=search) | Q(user_name__icontains=search)
            )
        else:
            search = ""
            historys = Users_activity.objects.all()
        totalnum = historys.count()
        pagination = get_pagination(param1, param2, totalnum)
        start_index = pagination["param1"] * pagination["param2"]
        end_index = start_index + pagination["param2"]
        change_historys = list(
            map(history_change_date, historys[start_index:end_index])
        )
    else:
        return redirect(reverse("/"))
    return render(request, "mentor_changes.html", locals())


@login_required
def mentor_update_user(request):
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        param1 = request.GET.get("s")
        param2 = request.GET.get("e")
        search = request.GET.get("search")
        if search is not None:
            historys = Users_activity.objects.filter(
                Q(mentor_name__icontains=search) | Q(user_name__icontains=search)
            )
        else:
            search = ""
            historys = Users_activity.objects.all()
        totalnum = historys.count()
        pagination = get_pagination(param1, param2, totalnum)
        start_index = pagination["param1"] * pagination["param2"]
        end_index = start_index + pagination["param2"]
        change_historys = list(
            map(history_change_date, historys[start_index:end_index])
        )
    else:
        return redirect(reverse("/"))
    return render(request, "mentor_update_user.html", locals())


@login_required
def mentor_user_info_details(request):
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        userid = request.GET.get("id")
        if userid:
            user = Subscriber.objects.get(id=userid)
            plans = Plans.objects.all()

            if request.method == "POST":
                username = request.POST.get("username")
                if username is not None and username != user.user.username:
                    user.user.username = username
                    mentor_activity_record(
                        "update", request.user.username, user.user.username, "User name"
                    )

                first_name = request.POST.get("first_name")
                if first_name is not None and first_name != user.first_name:
                    user.first_name = first_name
                    mentor_activity_record(
                        "update",
                        request.user.username,
                        user.user.username,
                        "First name",
                    )

                last_name = request.POST.get("last_name")
                if last_name is not None and last_name != user.last_name:
                    user.last_name = last_name
                    mentor_activity_record(
                        "update", request.user.username, user.user.username, "Last name"
                    )

                plan_id = request.POST.get("plan_id")
                if plan_id is not None and plan_id != user.plan_id:
                    user.plan_id = int(plan_id)
                    mentor_activity_record(
                        "update",
                        request.user.username,
                        user.user.username,
                        "Plan to " + Plans.objects.get(id=user.plan_id).name,
                    )

                email = request.POST.get("email")
                if email is not None and email != user.email:
                    user.email = email
                    mentor_activity_record(
                        "update", request.user.username, user.user.username, "Email"
                    )

                address = request.POST.get("address")
                if address is not None and address != user.address:
                    user.address = address
                    mentor_activity_record(
                        "update", request.user.username, user.user.username, "Address"
                    )

                city = request.POST.get("city")
                if city is not None and city != user.city:
                    user.city = city
                    mentor_activity_record(
                        "update", request.user.username, user.user.username, "City"
                    )

                zip_code = request.POST.get("zip_code")
                if zip_code is not None and zip_code != user.zip_code:
                    user.zip_code = zip_code
                    mentor_activity_record(
                        "update", request.user.username, user.user.username, "Zip code"
                    )

                state = request.POST.get("state")
                if state is not None and state != user.state:
                    user.state = state
                    mentor_activity_record(
                        "update", request.user.username, user.user.username, "State"
                    )

                phone = request.POST.get("phone")
                if phone is not None and phone != user.phone:
                    user.phone = phone
                    mentor_activity_record(
                        "update", request.user.username, user.user.username, "Phone"
                    )
                user.save()

            user.expire_date = user.expire_date.strftime("%d/%m/%Y")
            user.created_date = user.created_date.strftime("%d/%m/%Y")
            return render(request, "mentor_userdetails.html", locals())
    return redirect(reverse("/"))


@login_required
def mentor_manage_user(request):
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        search = request.GET.get("search")
        if search is not None:
            subscribers = Subscriber.objects.filter(Q(user__username__icontains=search))
        else:
            search = ""
            subscribers = Subscriber.objects.all()
        totalnum = subscribers.count()
        param1 = request.GET.get("s")
        param2 = request.GET.get("e")
        pagination = get_pagination(param1, param2, totalnum)
        start_index = pagination["param1"] * pagination["param2"]
        end_index = start_index + pagination["param2"]
        users_info = get_users_info(subscribers[start_index:end_index])
    else:
        return redirect(reverse("/"))
    return render(request, "mentor_manage_user.html", locals())


def get_subscribed_users():
    new_subscribeds = []
    new_subscriber = namedtuple(
        "subscribers",
        ["plan_name", "user_name", "first_name", "last_name", "date", "email"],
    )
    subscribeds = Plans.objects.prefetch_related("subscriber_set").all()
    for plan in subscribeds:
        for subscriber in plan.subscriber_set.order_by("created_date")[:1]:
            new_subscribeds.append(
                new_subscriber(
                    plan_name=plan.name,
                    user_name=subscriber.user.username,
                    first_name=subscriber.first_name,
                    last_name=subscriber.last_name,
                    date=subscriber.created_date.strftime("%d/%m/%Y"),
                    email=subscriber.email,
                )
            )
    return new_subscribeds


def get_expired_subscriptions():
    expired_subscribers = []
    new_subscriber = namedtuple(
        "subscribers",
        ["plan_name", "user_name", "first_name", "last_name", "date", "email"],
    )
    subscribeds = Plans.objects.prefetch_related("subscriber_set").all()
    current_date = datetime.now()
    for plan in subscribeds:
        for subscriber in plan.subscriber_set.filter(
            expire_date__lt=current_date
        ).order_by("expire_date")[:1]:
            expired_subscribers.append(
                new_subscriber(
                    plan_name=plan.name,
                    user_name=subscriber.user.username,
                    first_name=subscriber.first_name,
                    last_name=subscriber.last_name,
                    date=subscriber.expire_date.strftime("%d/%m/%Y"),
                    email=subscriber.email,
                )
            )
    return expired_subscribers


def get_paypal_cancellations(subscribeds):
    payal_canceled_subscribers = []
    new_subscriber = namedtuple(
        "subscribers",
        ["plan_name", "user_name", "first_name", "last_name", "email", "date"],
    )
    for subscriber in subscribeds:
        payal_canceled_subscribers.append(
            new_subscriber(
                plan_name=subscriber.plan.name,
                user_name=subscriber.user.username,
                first_name=subscriber.first_name,
                last_name=subscriber.last_name,
                email=subscriber.email,
                date=subscriber.created_date.strftime("%d/%m/%Y"),
            )
        )
    return payal_canceled_subscribers


def get_github_activitys():
    github_activitys = []
    new_activitys = namedtuple(
        "activitys", ["event_type", "username", "url", "created_at"]
    )
    for activity in GitHubActivitys.objects.all()[:4]:
        github_activitys.append(
            new_activitys(
                event_type=activity.event_type,
                username=activity.username,
                url=activity.url,
                created_at=activity.created_at.strftime("%d/%m/%Y"),
            )
        )
    return github_activitys


def get_deactived_users():
    deactives = []
    new_subscriber = namedtuple(
        "subscribers",
        ["plan_name", "user_name", "first_name", "last_name", "date", "email"],
    )
    for subscriber in Subscriber.objects.filter(status="new"):
        deactives.append(
            new_subscriber(
                plan_name=subscriber.plan.name,
                user_name=subscriber.user.username,
                first_name=subscriber.first_name,
                last_name=subscriber.last_name,
                date=subscriber.created_date.strftime("%d/%m/%Y"),
                email=subscriber.email,
            )
        )
    return deactives


def get_users_info(subscribers):
    users_info = []
    new_user = namedtuple(
        "subscribers",
        [
            "id",
            "plan_name",
            "user_name",
            "first_name",
            "last_name",
            "expiration_date",
            "status",
        ],
    )
    for subscriber in subscribers:
        users_info.append(
            new_user(
                id=subscriber.id,
                plan_name=subscriber.plan.name,
                user_name=subscriber.user.username,
                first_name=subscriber.first_name,
                last_name=subscriber.last_name,
                expiration_date=subscriber.expire_date.strftime("%d/%m/%Y"),
                status=subscriber.status,
            )
        )
    return users_info


def get_pagination(param1, param2, totalnum):
    if param1 is not None:
        param1 = int(param1) - 1
        if param1 < 0:
            param1 = 0
    else:
        param1 = 0

    if param2 is not None:
        param2 = int(param2)
    else:
        param2 = 15
    totalnum = math.ceil(totalnum / param2)
    minshow = False
    maxshow = False
    minshownum = param1 - 3
    maxshownum = param1 + 3
    if minshownum > 0:
        minshow = True
    else:
        minshownum = 0
    if maxshownum < totalnum:
        maxshow = True
    else:
        maxshownum = totalnum - 1
    previounum = param1
    nextnum = param1 + 2
    if nextnum > totalnum - 1:
        nextnum = totalnum - 1
    if previounum < 0:
        previounum = 0
    totalleng = []
    i = minshownum
    while i <= maxshownum:
        totalleng.append(i + 1)
        i += 1
    return {
        "minshow": minshow,
        "maxshow": maxshow,
        "previounum": previounum,
        "nextnum": nextnum,
        "totalleng": totalleng,
        "param1": param1,
        "param2": param2,
        "selected": param1 + 1,
    }


def mentor_activity_record(action, mentor_name, user_name, description):
    Users_activity.objects.create(
        action=action,
        description=description,
        mentor_name=mentor_name,
        user_name=user_name,
        created_at=datetime.now(),
    )


def update_status_change(request):
    if request.method == "POST":
        try:
            request_data = json.loads(request.body)
            subscription = Subscriber.objects.get(id=request_data["userid"])
            if request_data["value"] == True:
                subscription.status = "active"
            else:
                subscription.status = "new"
            mentor_activity_record(
                "update", request.user.username, subscription.user.username, "Status"
            )
            subscription.save()
            return HttpResponse(status=200)
        except json.JSONDecodeError:
            return HttpResponse(status=400)
    return HttpResponse(status=500)
