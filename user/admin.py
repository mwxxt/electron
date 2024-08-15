from django.contrib import admin
from .models import User
from univer.employee.models import EmployeeProfile
from univer.student.models import StudentProfile


# User
class EmployeeProfileStackedInline(admin.StackedInline):
    model = EmployeeProfile
    can_delete = True


class StudentProfileStackedInline(admin.StackedInline):
    model = StudentProfile
    can_delete = True


class UserAdmin(admin.ModelAdmin):
    inlines = [EmployeeProfileStackedInline, StudentProfileStackedInline]


admin.site.register(User, UserAdmin)


# Employee
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "user")
    search_fields = ("first_name", "last_name", "middle_name")

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    full_name.short_description = "full name"


admin.site.register(EmployeeProfile, EmployeeProfileAdmin)


# Student
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "user")
    search_fields = ("first_name", "last_name", "middle_name")

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    full_name.short_description = "full name"


admin.site.register(StudentProfile, StudentProfileAdmin)
