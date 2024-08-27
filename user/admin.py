from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry
from univer.employee.models import EmployeeProfile
from univer.student.models import StudentProfile

# User
class EmployeeProfileStackedInline(admin.StackedInline):
    model = EmployeeProfile
    can_delete = True


class StudentProfileStackedInline(admin.StackedInline):
    model = StudentProfile
    can_delete = True

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    inlines = [EmployeeProfileStackedInline, StudentProfileStackedInline]


admin.site.register(LogEntry)