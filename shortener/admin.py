from django.contrib import admin
from .models import Url
# Register your models here.
@admin.register(Url)

class Url(admin.ModelAdmin):
    list_display = ('real_url', 'generated_link', 'url_views')
    list_filter = ('url_views', 'real_url')