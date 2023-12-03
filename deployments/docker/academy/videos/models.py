from django.db import models
from django.conf import settings
from django.core.validators import MaxLengthValidator
from accounting.models import Plans, Subscriber, Content


class VideoFolder(models.Model):
    max_content_length      = 20000
    type                = models.CharField(max_length=6)
    name                = models.CharField(max_length=100)
    vimeo_name          = models.CharField(max_length=100)
    total_items         = models.IntegerField(blank=True, null=True)
    has_new_videos      = models.BooleanField(blank=True, null=True)
    created_date        = models.DateTimeField(blank=True, null=True, help_text="HH:MM:SS DD Mmm YY, YYYY CDT")
    updated_date        = models.DateTimeField(blank=True, null=True, help_text="HH:MM:SS DD Mmm YY, YYYY CDT")
    plan_level          = models.IntegerField(blank=True, null=True)
    is_parent           = models.BooleanField(blank=True, null=True)
    has_child           = models.BooleanField(blank=True, null=True)
    thumbnail_link      = models.CharField(max_length=500, blank=True, null=True)
    link                = models.CharField(max_length=500, blank=True, null=True)
    total_views         = models.IntegerField(blank=True, null=True)
    description         = models.TextField(max_length=max_content_length, blank=True, null=True, validators=[MaxLengthValidator(max_content_length)])
    resource_key        = models.CharField(max_length=50, blank=True, null=True)
    subscription_plan   = models.ForeignKey(Plans, null=True, blank=True, on_delete = models.CASCADE)
    duration            = models.DurationField(blank=True, null=True)
    parent_resource_key = models.CharField(max_length=50, blank=True, null=True)
    parent              = models.ForeignKey('self', null=True, blank=True, on_delete = models.CASCADE)
    vimeo_uri           = models.CharField(max_length=2048, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed     = True
        ordering    = ['plan_level']
