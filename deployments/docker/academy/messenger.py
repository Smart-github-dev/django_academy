
## Load the json and requests library
import requests, json
from django.conf import settings
import logging.config

import requests
import logging

class Slack:
    def __init__(self, slack_webhook_url) -> None:
        self.slack_webhook_url  = slack_webhook_url
        self.logger             = logging.getLogger(__name__)

    def send_message(self, what):
        response = requests.post(self.slack_webhook_url, json={'text': what})
        if response.status_code != 200:
            self.logger.error(f"Failed to send message to Slack. Status code: {response.status_code}, Response: {response.text}")

    def new_subscriber(self, subscriber):
        slack_blocks = {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Hi Mentors :wave:"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "We have new subscriber and we need to make sure we onboard them to the platform. Please reach out to subscriber and make sure subscriber has all the access:"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"• Full name: {subscriber.first_name} {subscriber.last_name}\n • Phone Number: {subscriber.phone}\n • Email:  {subscriber.email}\n • Username: {subscriber.user.username}\n • Subscription plan: {subscriber.plan.name}"
                    }
                }
            ]
        }

        response = requests.post(self.slack_webhook_url, json=slack_blocks)
        if response.status_code != 200:
            self.logger.error(f"Failed to send message to Slack. Status code: {response.status_code}, Response: {response.text}")

    def canceled_subscription(self, subscriber):
        slack_blocks = {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Hi Mentors ❌"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"Unfortunalty {subscriber.first_name} {subscriber.last_name} has canceled the subscription and we need to make sure the username fully oboarded from the platform:"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"• Full name: {subscriber.first_name} {subscriber.last_name}\n • Phone Number: {subscriber.phone}\n • Email:  {subscriber.email}\n • Username: {subscriber.user.username}\n • Subscription plan: {subscriber.plan.name}"
                    }
                }
            ]
        }

        response = requests.post(self.slack_webhook_url, json=slack_blocks)
        if response.status_code != 200:
            self.logger.error(f"Failed to send message to Slack. Status code: {response.status_code}, Response: {response.text}")

    def notify_with_subscriber_info(self, subscriber, message):
        slack_blocks = {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Hello Mentors :warning:"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"{message}"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"• Full name: {subscriber.first_name} {subscriber.last_name}\n • Phone Number: {subscriber.phone}\n • Email:  {subscriber.email}\n • Username: {subscriber.user.username}\n • Subscription plan: {subscriber.plan.name}"
                    }
                }
            ]
        }

        response = requests.post(self.slack_webhook_url, json=slack_blocks)
        if response.status_code != 200:
            self.logger.error(f"Failed to send message to Slack. Status code: {response.status_code}, Response: {response.text}")






def get_messenger(which):
    slack_webhok_url = getattr(settings, 'SLACK_WEBHOOK_URL', None)

    if which.lower() == 'slack':
        return Slack(slack_webhok_url)

"""
from messenger import get_messenger
slack = get_messenger('slack')
slack.send_messenge('Hello Moto')


from accounting.models import Subscriber
from messenger import get_messenger
slack = get_messenger('slack')
slack.send_messenge('Hello Moto')

queryset = Subscriber.objects.all()
slack.send_table_message(queryset)

slack.send_messenge('Hello I want to learn more about yout projets')
"""
