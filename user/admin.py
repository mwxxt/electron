from django.contrib import admin
from . import models
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from univer.employee.models import EmployeeProfile
from univer.student.models import StudentProfile
from unfold.admin import ModelAdmin, StackedInline
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from unfold.decorators import display
from django.db.models import TextChoices


class UserStatus(TextChoices):
    ACTIVE = "ACTIVE", _("Active")
    INACTIVE = "INACTIVE", _("Inactive")
    TRUE = "TRUE", _("True")
    FALSE = "FALSE", _("False")


class UserRole(TextChoices):
    ADMIN = "ADMIN", _("Admin")
    EMPLOYEE = "EMPLOYEE", _("Employee")
    STUDENT = "STUDENT", _("Student")


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
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
        "show_role",
        "show_active",
        "show_superuser",
    ]

    @display(
        description=_("Active"),
        ordering="is_active",
        label={
            UserStatus.ACTIVE: "success",  # green
            UserStatus.INACTIVE: "danger",  # orange
        },
    )
    def show_active(self, obj):
        return "ACTIVE" if obj.is_active else "INACTIVE"

    @display(
        description=_("Admin"),
        ordering="is_superuser",
        label={
            UserStatus.TRUE: "success",  # green
            UserStatus.FALSE: "danger",  # orange
        },
    )
    def show_superuser(self, obj):
        return "TRUE" if obj.is_superuser else "FALSE"

    @display(
        description=_("Role"),
        ordering="role",
        label={
            UserRole.ADMIN: "info",  # green
            UserRole.EMPLOYEE: "info",  # orange
            UserRole.STUDENT: "info",
        },
    )
    def show_role(self, obj):
        return obj.role


admin.site.unregister(Group)


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass
