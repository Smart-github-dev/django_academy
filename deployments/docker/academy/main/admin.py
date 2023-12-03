from django.contrib import admin
from .models import (Feature,
                     Questions,
                     Notification,
                    )

# Register your models here.
class FeatureAdmin(admin.ModelAdmin):
    list_filter = ('feature_type',)

admin.site.register(Feature, FeatureAdmin)
admin.site.register(Questions)
admin.site.register(Notification)
