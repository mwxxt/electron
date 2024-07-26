from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Student"
        EMPLOYEE = "EMPLOYEE", "Employee"

    base_role = Role.ADMIN
    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

    class Meta:
        db_table = "user"


class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STUDENT)


class Student(User):
    base_role = User.Role.STUDENT
    student = StudentManager()

    class Meta:
        proxy = True


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    middle_name = models.CharField(max_length=150, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "student_profile"


@receiver(post_save, sender=Student)
def create_student_profile(sender, instance, created, **kwargs):
    if created and instance.role == "STUDENT":
        StudentProfile.objects.create(user=instance)


class EmployeeManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.EMPLOYEE)


class Employee(User):
    base_role = User.Role.EMPLOYEE
    employee = EmployeeManager()

    class Meta:
        proxy = True


class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    middle_name = models.CharField(max_length=150, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "employee_profile"


@receiver(post_save, sender=Employee)
def create_employee_profile(sender, instance, created, **kwargs):
    if created and instance.role == "EMPLOYEE":
        EmployeeProfile.objects.create(user=instance)
