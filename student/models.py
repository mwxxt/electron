from django.db import models
from user.models import User
from django.contrib.auth.models import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    GENDER = (("M", "Мужчина"), ("F", "Женщина"))
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile",
        verbose_name="Пользователь",
    )
    first_name = models.CharField(max_length=150, null=True, blank=True, verbose_name="Имя")
    last_name = models.CharField(max_length=150, null=True, blank=True, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=150, null=True, blank=True, verbose_name="Отчество")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    gender = models.CharField(choices=GENDER, max_length=8, null=True, blank=True, verbose_name="Пол")
    phone_number = PhoneNumberField(unique=True, null=True, blank=False, verbose_name="Номер телефона")

    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"
        db_table = "student_profile"


@receiver(post_save, sender=Student)
def create_student_profile(sender, instance, created, **kwargs):
    if created and instance.role == "STUDENT":
        StudentProfile.objects.create(user=instance)
