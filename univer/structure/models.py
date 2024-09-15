from django.db import models

class UniverBranch(models.Model): 
    title = models.CharField(verbose_name="Название филиала", max_length=500)
    logo = models.ImageField(verbose_name="Логотип", upload_to='media/logo/', default='media/logo/logo_kstu.jpg', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Univer branch"
        verbose_name_plural = "Univer branches"
        db_table = "univer_branch"
