from django.contrib import admin
from .models import ProfileAdmin

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('usernames', 'email', 'password')  # displayed fields
    list_filter = ('', '')  # filters for certain fields
    search_fields = ('', '')
    ordering = ('field1',)  # default sorting order
    actions = ['custom_action']

    def custom_action(self, request, queryset):
        # Your custom action logic here
        pass
    custom_action.short_description = 'Custom Action'  # Display name for the action
