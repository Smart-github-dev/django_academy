from django.contrib.auth.models import Group
from django.urls import resolve
from django.shortcuts import render, redirect

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not self.has_access_to_app(request):
            return redirect("/")
        return self.get_response(request)

    def has_access_to_app(self, request):  
        app_name = self.get_current_app_name(request)
        if app_name == "mentors":# auth middleware for mentro app
            required_group_name = "mentors"
            try:
                required_group = Group.objects.get(name=required_group_name)
                if required_group in request.user.groups.all():
                    return True
            except Group.DoesNotExist:
                return False
            return False
        return True

    def get_current_app_name(self, request):
        resolver_match = resolve(request.path_info)
        if resolver_match.app_name:
            return resolver_match.app_name
        return None
