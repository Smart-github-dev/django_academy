from django.contrib import admin
from .models import Plans, Subscriber, Content

# Register your models here.
class PlansAdmin(admin.ModelAdmin):
    list_filter = ('name', 'price')

class ContentAdmin(admin.ModelAdmin):
    list_filter = ('conent_type', 'publish', 'user')


class SubscriberAdmin(admin.ModelAdmin):
    list_filter = ('created_date', 'expire_date', 'plan', 'user')


admin.site.register(Plans, PlansAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Content, ContentAdmin)
