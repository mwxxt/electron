from django.contrib import admin
from . import models
from unfold.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm
    
# Employee
@admin.register(models.EmployeeProfile)
class EmployeeProfileAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ("full_name", "user")
    search_fields = ("first_name", "last_name", "middle_name")
    list_filter = [
        "gender"
    ]
    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    full_name.short_description = "full name"