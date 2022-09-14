from django.contrib import admin
from main import models


@admin.register(models.ShortedLink)
class ShortedLinkAdmin(admin.ModelAdmin):
    list_display = ['shorted', 'url']
