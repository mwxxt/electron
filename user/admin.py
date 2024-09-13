from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry
from univer.employee.models import EmployeeProfile
from univer.student.models import StudentProfile
from univer.branch.models import UniverBranch
from unfold.admin import ModelAdmin, StackedInline, TabularInline
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm


# User
class EmployeeProfileStackedInline(StackedInline):
    model = EmployeeProfile
    can_delete = True


class StudentProfileStackedInline(StackedInline):
    model = StudentProfile
    can_delete = True


@admin.register(models.User)
class UserAdmin(ModelAdmin):
    inlines = [EmployeeProfileStackedInline, StudentProfileStackedInline]