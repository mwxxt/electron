from django.contrib import admin
from unfold.admin import ModelAdmin
from . import models
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm


@admin.register(models.UniverBranch)
class UniverBranchAdmin(ModelAdmin):
    list_display = ("id", "title")
    
    
@admin.register(models.Department)
class DepartmentAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ("title", "title_short")
    ordering = ["title"]
    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm


@admin.register(models.Institute)
class InstituteAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ("title", "title_short")
    ordering = ["title"]
    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm


@admin.register(models.Cathedra)
class CathedraAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ("title", "institute", "title_short")
    search_fields = ("title", "institute__title", "title_short")
    ordering = ["title"]
    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm