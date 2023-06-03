from django.contrib import admin

from .models import *


@admin.register(Cure)
class CureAdmin(admin.ModelAdmin):
    pass
