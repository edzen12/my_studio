from django.contrib import admin
from .models import Service, Help_bus, My_steak


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'color']
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

admin.site.register(Service, ServiceAdmin)

admin.site.register(Help_bus)
admin.site.register(My_steak)
