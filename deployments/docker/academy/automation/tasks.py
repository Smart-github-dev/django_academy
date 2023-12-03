from automation.tasks import shared_task
from django.utils import timezone
from accounting.models import Subscriber
from messenger import get_messenger

@shared_task
def check_subscriptions():
    expired_subscriptions = Subscriber.objects.filter(expire_date__lte=timezone.now(), payment_confirmation=True)
    for subscription in expired_subscriptions:
        slack = get_messenger('slack')
        message = f"The subscriber {subscription.first_name} {subscription.last_name}'s account has been expired please check the account"
        slack.notify_with_subscriber_info(subscription, message)
