from django.db import models
from user.models import User
from django.contrib.auth.models import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    GENDER = (("M", "Мужчина"), ("F", "Женщина"))
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="employee_profile",
        verbose_name="Пользователь",
    )
    first_name = models.CharField(max_length=150, null=True, blank=True, verbose_name="Имя")
    last_name = models.CharField(max_length=150, null=True, blank=True, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=150, null=True, blank=True, verbose_name="Отчество")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    gender = models.CharField(choices=GENDER, max_length=8, null=True, blank=True, verbose_name="Пол")
    phone_number = PhoneNumberField(unique=True, null=True, blank=False, verbose_name="Номер телефона")
    email = models.EmailField(unique=True, null=True, blank=False, verbose_name="Почта")

    class Meta:
        verbose_name = "employee"
        verbose_name_plural = "employees"
        db_table = "employee_profile"


@receiver(post_save, sender=Employee)
def create_employee_profile(sender, instance, created, **kwargs):
    if created and instance.role == "EMPLOYEE":
        EmployeeProfile.objects.create(user=instance)
