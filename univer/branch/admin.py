from django.contrib import admin
from . import models
from unfold.admin import ModelAdmin

@admin.register(models.UniverBranch)
class UniverBranchAdmin(ModelAdmin):
    list_display = ("id", "title")