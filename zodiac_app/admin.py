from django.contrib import admin
from .models import ZodiacModel


@admin.register(ZodiacModel)
class ZodiacAdmin(admin.ModelAdmin):
    list_display = ['name']