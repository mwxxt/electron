from django.contrib import admin
from . import models
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from univer.employee.models import EmployeeProfile
from univer.student.models import StudentProfile
from unfold.admin import ModelAdmin, StackedInline
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

# User
class EmployeeProfileStackedInline(StackedInline):
    model = EmployeeProfile
    can_delete = True


class StudentProfileStackedInline(StackedInline):
    model = StudentProfile
    can_delete = True


@admin.register(models.User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    inlines = [EmployeeProfileStackedInline, StudentProfileStackedInline]

admin.site.unregister(Group)

@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass