# from django.db import models
# from django.utils import timezone
# from apps_logic.employees.models import Employee
# from apps_logic.univer.models import UniverBranch
# from django.core.validators import FileExtensionValidator
# from django.db import transaction

# class PurchaseType(models.Model):
#     title = models.CharField(max_length=255)

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = "Вид закупки"
#         verbose_name_plural = "Виды закупок"
#         db_table = "purchase_type"

# class Purchase(models.Model):
#     purchase_type = models.ForeignKey(to=PurchaseType, on_delete=models.CASCADE, verbose_name="Вид закупки")
#     univer_branch = models.ForeignKey(to=UniverBranch, on_delete=models.SET_NULL, null=True, verbose_name="Филиал")
#     employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE, verbose_name="Сотрудник")
#     number = models.CharField(verbose_name="Номер закупки", max_length=300, blank=True, unique=True, editable=False)
#     title = models.TextField(verbose_name="Название закупки")
#     text = models.TextField(verbose_name="Текст", blank=True, null=True)
#     status = models.BooleanField(verbose_name="Статус тендера", default=True)
#     reason = models.CharField(verbose_name="Причина", max_length=400, blank=True, null=True)
#     documentation = models.FileField(verbose_name="Документация", upload_to="purchase/documentation/%Y/%m/%d/", validators=[FileExtensionValidator(['pdf', 'docx', 'doc'])], blank=True, null=True)
#     contract = models.FileField(verbose_name="Договор", upload_to="purchase/contract/%Y/%m/%d/", validators=[FileExtensionValidator(['pdf', 'docx', 'doc'])], blank=True, null=True)
#     tech_task =models.FileField(verbose_name="Техническое задание", upload_to="purchase/tech_task/%Y/%m/%d/", validators=[FileExtensionValidator(['pdf', 'docx', 'doc'])], blank=True, null=True)
#     instruction = models.FileField(verbose_name="Инструкция", upload_to="purchase/instruction/%Y/%m/%d/", validators=[FileExtensionValidator(['pdf', 'docx', 'doc'])], blank=True, null=True)
#     winner = models.CharField(verbose_name="Победитель", max_length=255, blank=True, null=True)
#     date_start = models.DateTimeField(verbose_name="Дата публикации", auto_now_add=True, editable=False)
#     date_end = models.DateTimeField(verbose_name="Дата конца")


#     def __str__(self):
#         return self.title

#     def save(self, *args, **kwargs):
#         if not self.number:
#             today_date = timezone.now().strftime("%d_%m_%Y")
#             today_purchases = Purchase.objects.filter(date_start__date=timezone.now().date())
#             if today_purchases.exists():
#                 last_purchase = today_purchases.order_by('-date_start').first()
#                 last_number = int(last_purchase.number.split("_")[-1])
#                 new_number = f"{today_date}_{last_number + 1:02d}"
#             else:
#                 new_number = f"{today_date}_01"
#             self.number = new_number

#         with transaction.atomic():
#             super().save(*args, **kwargs)

#     class Meta:
#         verbose_name = "Закупка"
#         verbose_name_plural = "Закупки"
#         db_table = "purchase"
#         ordering = ["-date_start"]


# class PurchaseAdditional(models.Model):
#     purchase = models.ForeignKey(to=Purchase, on_delete=models.CASCADE, verbose_name="Закупка", blank=True, related_name="purchase_additional")
#     qualification = models.TextField(verbose_name="Квалификация", blank=True, null=True)
#     requirement = models.TextField(verbose_name="Требования", blank=True, null=True)

#     def __str__(self):
#         return self.qualification + " --- " + self.requirement

#     class Meta:
#         verbose_name = "Квалификация и требования"
#         verbose_name_plural = "Квалификации и требования"
#         db_table = "purchase_additional"


# class LegalAct(models.Model):
#     title = models.CharField(verbose_name="Тема", max_length=255)
#     file = models.FileField(verbose_name="Файл", upload_to="purchase/legal-act/", validators=[FileExtensionValidator(['pdf', 'docx', 'doc'])], blank=True, null=True)

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = "Нормативно-правовой акт"
#         verbose_name_plural = "Нормативно-правовые акты"
#         db_table = "legal_act"
#         ordering = ["id"]


# class ContactInfo(models.Model):
#     title = models.CharField(verbose_name="Заголовок", max_length=255)
#     text = models.TextField(verbose_name="Описание")

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = "Контактная информация"
#         verbose_name_plural = "Контактные информации"
#         db_table = "contact_info"
