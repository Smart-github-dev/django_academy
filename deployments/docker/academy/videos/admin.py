from django.contrib import admin
from videos.models import VideoFolder
from django.urls import path

admin.site.site_header = "Academy Admin dashboard"

class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'duration')

    list_filter = ('name', 'duration')

admin.site.register(VideoFolder, VideoAdmin)
