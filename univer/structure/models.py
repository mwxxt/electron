from django.db import models
from base.models import BaseModel

class UniverBranch(models.Model): 
    title = models.CharField(verbose_name="Филиал", max_length=500)
    logo = models.ImageField(verbose_name="Логотип", upload_to='media/logo/', default='media/logo/logo_kstu.jpg', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Univer branch"
        verbose_name_plural = "Univer branches"
        db_table = "univer_branch"


class Department(BaseModel):
    title = models.CharField(verbose_name="Отдел", max_length=500, unique=True)
    title_short = models.CharField(verbose_name="Аббревиатура", max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        db_table = "univer_department"


class Institute(BaseModel):
    title = models.CharField(verbose_name="Институт", max_length=500)
    title_short = models.CharField(verbose_name="Аббревиатура", max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Institute"
        verbose_name_plural = "Institutes"
        db_table = "univer_institute"


class Cathedra(BaseModel):
    institute = models.ForeignKey(to=Institute, on_delete=models.CASCADE, verbose_name="Институт", null=True, related_name="cathedra")
    title = models.CharField(verbose_name="Кафедра", max_length=500)
    title_short = models.CharField(verbose_name="Аббревиатура", max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Cathedra"
        verbose_name_plural = "Cathedras"
        db_table = "univer_cathedra"