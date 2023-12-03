from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from accounting.models import Subscriber, Plans
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from messenger import get_messenger
import json

def onboard_user(sender, **kwargs):
    ipn_obj = sender

    plan_id, subscription_period, subscriber_user_id = [str(i) for i in ipn_obj.custom.split("|")]
    plan = Plans.objects.get(id=int(plan_id))
    user = User.objects.get(id=int(subscriber_user_id))

    slack = get_messenger('slack')


    # check for subscription payment IPN
    if ipn_obj.txn_type == "subscr_payment":
        if Subscriber.objects.filter(user=user):

            subscriber = Subscriber.objects.get(user=user)
            if not subscriber.payment_confirmation:
                subscriber.plan = plan
                subscriber.payment_confirmation = True
                subscriber.status = 'active'
                subscriber.save()
                slack.new_subscriber(subscriber)

            ## Making sure user can upgrade the plan
            if subscriber.plan != plan:
                subscriber.plan = plan
                subscriber.payment_confirmation = True
                subscriber.status = 'active'
                subscriber.save()

            subscriber.extend(subscription_period)


    # check for subscription cancellation IPN
    elif ipn_obj.txn_type == "subscr_cancel":
        if Subscriber.objects.filter(user=user):
            subscriber = Subscriber.objects.get(user=user)
            subscriber.status = 'canceled'
            subscriber.save()
            slack.canceled_subscription(subscriber)


    # check for failed subscription payment IPN
    elif ipn_obj.txn_type == "subscr_failed":
        pass


    # check for subscription signup IPN
    elif ipn_obj.txn_type == "subscr_signup":
        pass


valid_ipn_received.connect(onboard_user)
