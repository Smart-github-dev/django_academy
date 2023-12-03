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

def main(request):
    login_form = AuthenticationForm()

    plans = Plans.objects.all().order_by('level')
    if request.method == 'POST':
        request.session['plan_id']  = request.POST.get('plan_id')
        user_selected_plan = Plans.objects.get(id=request.POST.get('plan_id'))
        if float(user_selected_plan.price) <= 1:
            messages.add_message(request, messages.INFO, f"Please contact to administrator to get access selected plan <{user_selected_plan.name}>")
            return redirect(reverse('main'))
        return redirect(reverse('subscription'))
    return render(request, 'main.html', locals())



@login_required
def profile(request, username):
    login_form = AuthenticationForm()
    if User.objects.filter(username=username):
        if Subscriber.objects.filter(user=request.user):
            subscription = Subscriber.objects.get(user=request.user)
        else:
            messages.add_message(request, messages.WARNING, "Seams like you don't have subscription with us please select one of the plans")
            return redirect(reverse('main'))
    common_variables = get_common_variables(request.user.username)
    return render(request, 'profile.html', locals())


@login_required
def settings(request):
    user = User.objects.get(username=request.user.username)

    if Subscriber.objects.filter(user=user):
        subscription = Subscriber.objects.get(user=user)

    if request.method == 'POST':
        form = UpdateSubscriptionInfoForm(request.POST, instance=subscription)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UpdateSubscriptionInfoForm()
    common_variables = get_common_variables(request.user.username)

    return render(request, 'settings.html', locals())



@login_required
def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profile')
        else:
            alert = True
            return render(request, 'change_password.html', locals())

    else:
        form = PasswordChangeForm(user=request.user)
        common_variables = get_common_variables(request.user.username)
        return render(request, 'change_password.html', locals())



#signtup page tacking id of the selected item as an argument
def signup(request, id):
    if Plans.objects.filter(id=id).exists():
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()

                user = authenticate(username=request.POST['username'], password=request.POST['password1'])
                login(request, user)

                plan = Plans.objects.filter(id=id).first()
                related_user = User.objects.get(username=request.user.username)

                feature = Feature.objects.create(feature_type= "Basic", user=related_user)

                if plan.price == 'Free':
                    return redirect('/profile')

                return redirect(f'/accounting/paypal/{id}')

        else:
            form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})


def contact(request):

    from django.conf import  settings

    form = ContactForm()

    recaptcha = True
    secret = getattr(settings, 'GOOGLE_RECAPTCHA_SECRET_KEY', None)
    admin_email = getattr(settings, 'EMAIL_HOST_USER', None)
    public_key = getattr(settings, 'GOOGLE_RECAPTCHA_PUBLIC_KEY', None)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        message = f"""
        New Contact request
        First name: {request.POST.get('first_name')}
        Last name: {request.POST.get('last_name')}
        Email: {request.POST.get('email')}
        ########################################
        {request.POST.get('message')}
        ########################################
        """
        send_message(message)
        return redirect('/contact-success')

    return render(request, 'contact.html', locals())


def faq(request):
    questions = Questions.objects.filter(publish=True).order_by('-subject')
    paginator = Paginator(questions, 3)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.page_range)

    page_obj_range = range(1, paginator.num_pages + 1)

    return render(request, 'faq.html', locals())


def contact_success(request):
    return render(request,'contact_success_msg.html')


def test(request):
    return render(request,'test.html')

@login_required
def user_questions(request):
    questions = Questions.objects.filter(user=request.user).order_by('-subject')
    return render(request,'user-questions.html', locals())

@login_required
def links_view(request):
    user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=user):
        subscription = Subscriber.objects.get(user=user)
    return render(request,'links.html', locals())

@login_required
def dashboard_view(request):
    logger.info(f"The user '{request.user.username}' login to the academy")
    current_user = User.objects.get(username=request.user.username)
    if Subscriber.objects.filter(user=current_user):
        subscription = Subscriber.objects.get(user=current_user)
        videos = get_new_videos()[0:6]
    else:
        messages.add_message(request, messages.INFO, "You don't have the subscription with us please choice one of the subsciption!!")
        return redirect(reverse('main'))
    return render(request,'dashboard.html', locals())


def forbidden(request):
    return render(request,'forbidden.html')
