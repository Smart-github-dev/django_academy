import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  # Replace 'your_project_name' with your project's name
django.setup()

from django.contrib.auth.models import User
from getpass import getpass

def run():
    # List all users
    users = User.objects.all()
    for idx, user in enumerate(users, 1):
        print(f"{idx}. {user.username}")

    # Get user choice
    choice = int(input("Enter the number of the user you want to update: "))
    if choice < 1 or choice > len(users):
        print("Invalid choice.")
        return

    selected_user = users[choice - 1]

    # Get the new password
    password = getpass("Enter the new password (input will be hidden): ")
    confirm_password = getpass("Confirm the new password: ")

    if password != confirm_password:
        print("Passwords do not match.")
        return

    # Update the password
    selected_user.set_password(password)
    selected_user.save()
    print(f"Password for {selected_user.username} has been updated!")
