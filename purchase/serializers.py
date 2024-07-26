# from rest_framework import serializers
# from .models import *
# from apps_logic.employees.models import Employee

# class PurchaseTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PurchaseType
#         fields = "__all__"

# class PurchaseAdditionalSerialzier(serializers.ModelSerializer):
#     class Meta:
#         model = PurchaseAdditional
#         fields = ('id', 'qualification', 'requirement')

# class PurchaseSerializer(serializers.ModelSerializer):
#     logo = serializers.ImageField(source="univer_branch.logo", read_only=True)
#     univer_branch_name = serializers.CharField(source="univer_branch.title", read_only=True)
#     purchase_additional = PurchaseAdditionalSerialzier(many=True, required=False)
#     employee_name = serializers.CharField(source="employee.surname_name", read_only=True)
#     purchase_name = serializers.CharField(source="purchase_type.title", read_only=True)
#     purchase_type = serializers.PrimaryKeyRelatedField(queryset=PurchaseType.objects.all(), write_only=True)
#     employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), write_only=True)
#     date_end = serializers.DateTimeField(format="%d.%m.%Y %H:%M", input_formats=['%d.%m.%Y %H:%M', 'iso-8601'])
#     creator = serializers.SerializerMethodField()
#     status_text = serializers.SerializerMethodField()

#     class Meta:
#         model = Purchase
#         fields = ('id', 'employee', 'employee_name', 'creator', 'number', 'univer_branch', 'univer_branch_name', 'logo', 'purchase_type', 'purchase_name', 'title', 'text',
#                   'status', 'status_text', 'reason', 'documentation', 'contract', 'tech_task', 'instruction', 'winner', 'date_start', 'date_end', 'purchase_additional')

#     def get_creator(self, obj):
#         request = self.context.get('request')
#         if request and request.user.id == obj.employee.user.id:
#             return True
#         return False

#     def get_status_text(self, obj):
#         if obj.status == True:
#             return "Открыт"
#         else:
#             return "Закрыт"


# class ClosedPurchaseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Purchase
#         fields = ('id', 'number', 'title', 'winner')


# class LegalActSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LegalAct
#         fields = "__all__"


# class ContactInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ContactInfo
#         fields = "__all__"
