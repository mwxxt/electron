from django.contrib import admin
from . import models
from unfold.admin import ModelAdmin

@admin.register(models.StudentProfile)
class StudentProfileAdmin(ModelAdmin):
    list_display = ("full_name", "user")
    search_fields = ("first_name", "last_name", "middle_name")

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    full_name.short_description = "full name"
