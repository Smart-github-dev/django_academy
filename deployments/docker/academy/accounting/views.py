from django.shortcuts import render, redirect, reverse
from accounting.models import Plans, Subscriber, Content
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from accounting.forms import SubscriptionForm
from paypal.standard.forms import PayPalPaymentsForm
from django.contrib.auth.models import User
from django.conf import  settings
from paypal.standard.ipn.models import PayPalIPN
from django.contrib import messages


def terms_of_condition(request):
    content_data = Content.objects.filter(conent_type='terms-and-conditions', publish=True).first()
    return render(request, 'terms.html', locals())

def privacy_policy(request):
    content_data = Content.objects.filter(conent_type='privacy-policy', publish=True).first()
    return render(request, 'terms.html', locals())

def learn_more(request, plan_id):
    content_data = Plans.objects.get(id=plan_id)
    return render(request, 'markdown.html', locals())

@login_required
def transactions(request, username):
    if User.objects.filter(username=username):
        if request.user.username == username:
            user = User.objects.get(username=username)
            if Subscriber.objects.filter(user=user):
                subscription = Subscriber.objects.get(user=user)
            else:
                messages.add_message(request, messages.WARNING, 'You do not have subscriptions with us please subscribe first!!')
                return redirect(reverse('main'))
            if PayPalIPN.objects.filter(custom__contains=f"|{user.id}"):
                all_ipns = PayPalIPN.objects.filter(custom__contains=f"|{user.id}")
            else:
                messages.add_message(request, messages.WARNING, 'Not able to find any paypal transactions with your accounts')
                return redirect(reverse('dashboard'))


    return render(request, 'user-subscription.html', locals())


## Before they pay the subscription
@login_required
def subscription(request):

    if request.session.get('plan_id'):
        plan_id = request.session.get('plan_id')
    else:
        return redirect(reverse('main'))

    if Plans.objects.filter(id=plan_id).exists():
        plan = Plans.objects.get(id=plan_id)

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            if not Subscriber.objects.filter(user=request.user, plan=plan).exists():
                subscription = form.save(commit=False)
                subscription.user = request.user
                subscription.save()

                request.session['subscription_period'] = request.POST.get('selected_period')
                request.session['subscription_plan_id'] = request.POST.get('plan_id')
                return redirect('process')
            else:
                messages.add_message(request, messages.WARNING, "You have existing subscription please cancel before you subscribe again!")
                return redirect(reverse('main'))
    else:
        form = SubscriptionForm()

    return render(request, 'subscription.html', locals())


@login_required
def process(request):
    subscription_data = {
        'host': request.get_host(),
        'plan_id': request.session.get('subscription_plan_id'),
        'subscriber_user_id': request.user.id,
        'subscription_period' : request.session.get('subscription_period')
    }

    paypal_custom = [
        f"{subscription_data['plan_id']}",
        f"{subscription_data['subscription_period']}",
        f"{subscription_data['subscriber_user_id']}" ]
    plan = Plans.objects.get(id=subscription_data['plan_id'])

    if subscription_data['subscription_period'] == '1-month':
        price = f"{plan.price}"
        billing_cycle = 1
        billing_cycle_unit = "M"

    elif subscription_data['subscription_period'] == '6-month':
        price = f"{plan.six_months_price}"
        billing_cycle = 6
        billing_cycle_unit = "M"

    else:
        price = f"{plan.year_price}"
        billing_cycle = 1
        billing_cycle_unit = "Y"

    paypal_custom_packed = str.join('|', paypal_custom)

    paypal_dict  = {
        "cmd": "_xclick-subscriptions",
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        "a3": price,
        "p3": billing_cycle,
        "t3": billing_cycle_unit,
        "src": "1",
        "sra": "1",
        "no_note": "1",
        'item_name': f"Academy Plan {plan.name}",
        'custom': paypal_custom_packed,
        'currency_code': 'USD',
        'notify_url': 'https://{}{}'.format(subscription_data['host'], reverse('paypal-ipn')),
        'return_url': 'https://{}{}'.format(subscription_data['host'], reverse('success')),
        'cancel_return': 'https://{}{}'.format(subscription_data['host'], reverse('declined')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict, button_type="subscribe")
    return render(request, 'process.html', locals())


@login_required
def payment_complete(request):
    return JsonResponse('payment completed!', safe=False)


@login_required
def declined_payment(request):
    return render(request, 'declined.html')

@login_required
def success_payment(request):
    return render(request, 'success.html')


@login_required
def cancel_subscription(request):
    return render(request, 'cancel.html')
