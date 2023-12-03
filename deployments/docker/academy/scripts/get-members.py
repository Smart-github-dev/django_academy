from accounting.models import Subscriber, Plans
import json, yaml
plan = Plans.objects.get(name='Pro')
subscribers = Subscriber.objects.filter(plan=plan, payment_confirmation=True)
found_user = []

def run(*args):
    for user_subscription in subscribers:
        if not user_subscription.is_expired():
            user_data = {
                'first_name': user_subscription.user.first_name,
                'last_name': user_subscription.user.last_name,
                'email': user_subscription.user.email,
                'username': user_subscription.user.username,
                'phone': user_subscription.user.phone
            }
            # if user_subscription.user.email:
            #     found_user.append(user_subscription.user.email)
            found_user.append(user_data)
    with open('full_data.json', 'w') as file:
        yaml.dump(found_user, file, default_flow_style=False)

    print(yaml.dump(found_user, default_flow_style=False))
