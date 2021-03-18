from django.contrib import admin
from .models import Price

class PriceAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price']
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

admin.site.register(Price, PriceAdmin)

