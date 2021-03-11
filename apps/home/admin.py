from django.contrib import admin
from apps.home.models import Setting


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'update_at']
    save_on_top = True

admin.site.register(Setting, SettingAdmin)