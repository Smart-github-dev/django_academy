from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from videos.models import VideoFolder
from main.models import Feature
from accounting.models import Subscriber
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from common import get_common_variables, is_folder_has_new_videos, is_video_new, get_new_videos
from datetime import datetime, timedelta
from django.conf import settings
from videos.filters import VideoFolderFilter
from django.core import serializers


def videos(request, resource_key=None):
    if Subscriber.objects.filter(user=request.user).exists():
        subscription = Subscriber.objects.get(user=request.user)
    if resource_key:
        parent = VideoFolder.objects.filter(resource_key=resource_key).first()
        videos = VideoFolder.objects.filter(parent=parent)
    else:
        videos = get_new_videos()

    return render(request, 'videos.html', locals())


def get_ajax_tree(request):
    parents = VideoFolder.objects.filter(is_parent=True)
    json_data = []
    for parent in parents:

        parent_dict = { 'text' : parent.name, 'children': [], 'resource_key' : parent.resource_key}

        for child in VideoFolder.objects.filter(parent=parent):
            if child.type == 'folder':
                child_dict = { 'text' : child.name, 'children': [], 'icon' : 'fa fa-folder text-success', 'resource_key' : child.resource_key}
                parent_dict['children'].append(child_dict)

            for sub_child in VideoFolder.objects.filter(parent=child):
                if sub_child.type == 'folder':
                    sub_child_dict = { 'text' : sub_child.name, 'children': [], 'icon' : 'fa fa-folder text-default',  'resource_key' : sub_child.resource_key}
                    child_dict['children'].append(sub_child_dict)

        json_data.append(parent_dict)
    return JsonResponse(json_data, safe=False)


def get_child_or_video(request, resource_key):
    if VideoFolder.objects.filter(resource_key=resource_key).exists():
        parent = VideoFolder.objects.filter(resource_key=resource_key).first()
        child = VideoFolder.objects.filter(parent=parent)
    else:
        return JsonResponse({'message' : 'The child not found'}, status=404)

    json_data = []
    for video in child:
        json_data.append({
            'name': video.name,
            'type': video.type,
            'description': video.description,
            'resource_key': video.resource_key,
            'is_parent': video.is_parent,
            'created_date': video.created_date,
        })
    return JsonResponse(json_data, safe=False)



@login_required
def watch(request, key=None):
    if Subscriber.objects.filter(user=request.user).exists():
        subscription = Subscriber.objects.get(user=request.user)
    else:
        message = "Seams like you don't have subscription with us please select one of the plans"
        return redirect(reverse('main'))

    if Subscriber.objects.filter(user=request.user).exists():
        user_subscription = Subscriber.objects.get(user=request.user)
    else:
        return HttpResponseRedirect('/#subscriptions')

    if VideoFolder.objects.filter(resource_key=key).exists():
        video = VideoFolder.objects.filter(resource_key=key).first()

    common_variables = get_common_variables(request.user.username)
    return render(request, 'video.html', locals())


@login_required
def recent_videos(request):
    if Subscriber.objects.filter(user=request.user).exists():
        subscription = Subscriber.objects.get(user=request.user)
    else:
        message = "Seams like you don't have subscription with us please select one of the plans"
        return redirect(reverse('main'))
    videos = get_new_videos()
    return render(request, 'recents.html', locals())


@login_required
def search_videos(request):
    if Subscriber.objects.filter(user=request.user).exists():
        subscription = Subscriber.objects.get(user=request.user)
    else:
        message = "Seams like you don't have subscription with us please select one of the plans"
        return redirect(reverse('main'))

    video_filter = VideoFolderFilter(request.GET, queryset=VideoFolder.objects.filter(type='video').order_by('-created_date'))
    videos = video_filter.qs

    return render(request, 'search-videos.html', locals())
