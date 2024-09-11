from django.contrib import admin
from .models import User
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


@admin.register(User)
class UserAdmin(ModelAdmin):
    inlines = [EmployeeProfileStackedInline, StudentProfileStackedInline]


# Employee
@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ("full_name", "user")
    search_fields = ("first_name", "last_name", "middle_name")
    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    full_name.short_description = "full name"


# Student
@admin.register(StudentProfile)
class StudentProfileAdmin(ModelAdmin):
    list_display = ("full_name", "user")
    search_fields = ("first_name", "last_name", "middle_name")

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    full_name.short_description = "full name"

#Univer branch
@admin.register(UniverBranch)
class UniverBranchAdmin(ModelAdmin):
    list_display = ("id", "title")