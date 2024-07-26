# from rest_framework.views import APIView
# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import *
# from .models import *
# from apps_logic.employees.models import Employee
# from apps_logic.movement.models import Movement
# from config import settings
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# import os


# class PurchaseTypeAPIView(generics.ListAPIView):
#     queryset = PurchaseType.objects.all()
#     serializer_class = PurchaseTypeSerializer


# class PurchaseAPIView(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def get(self, request, *args, **kwargs):
#         purchase_objects = Purchase.objects.exclude(winner__isnull=False).select_related('employee', 'employee__user', 'univer_branch', 'purchase_type').prefetch_related('purchase_additional')
#         serializer = PurchaseSerializer(purchase_objects, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, *args, **kwargs):
#         requested_data = request.data
#         try:
#             employee = Employee.objects.get(user_id=request.user.id)
#             movement = Movement.objects.get(employee=employee)
#         except Employee.DoesNotExist:
#             return Response({"error":"Сотрудник не найден"}, status=status.HTTP_404_NOT_FOUND)
#         except Movement.DoesNotExist:
#             return Response({"error":"Движение не найдено"}, status=status.HTTP_404_NOT_FOUND)

#         if movement.univer_branch:
#             requested_data['univer_branch'] = movement.univer_branch.id
#         else:
#             return Response({"error":"Сотрудник не назначен к филиалу"}, status=status.HTTP_404_NOT_FOUND)

#         requested_data['employee'] = employee.id
#         serializer = PurchaseSerializer(data=requested_data)
#         if serializer.is_valid():
#             purchase_additional = serializer.validated_data.pop("purchase_additional", [])
#             instance = Purchase.objects.create(**serializer.validated_data)
#             if purchase_additional:
#                 for obj in purchase_additional:
#                     if obj.get('qualification') != "" and obj.get('requirement') != "":
#                         PurchaseAdditional.objects.create(purchase=instance, **obj)
#             data = PurchaseSerializer(instance)
#             return Response(data.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class PurchaseDetailAPIView(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def get(self, request, *args, **kwargs):
#         try:
#             purchase_object = Purchase.objects.select_related('employee', 'univer_branch', 'purchase_type').prefetch_related('purchase_additional').get(id=kwargs['pk'])
#             serializer = PurchaseSerializer(purchase_object)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Purchase.DoesNotExist:
#             return Response({"error": "Purchase not found"}, status=status.HTTP_404_NOT_FOUND)

#     def patch(self, request, *args, **kwargs):
#         try:
#             purchase_instance = Purchase.objects.get(pk=kwargs['pk'])
#         except Purchase.DoesNotExist:
#             return Response({"error": "Purchase not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = PurchaseSerializer(instance=purchase_instance, data=request.data, partial=True)

#         if serializer.is_valid():
#             if request.user.id == purchase_instance.employee.user.id:
#                 for field_name, field_value in request.data.items():
#                     if field_name in ['documentation', 'contract', 'tech_task', 'instruction']:
#                         old_file = getattr(purchase_instance, field_name)
#                         if old_file:
#                             file_path = os.path.join(settings.MEDIA_ROOT, str(old_file))
#                             if os.path.exists(file_path):
#                                 os.remove(file_path)
#                         setattr(purchase_instance, field_name, field_value)
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response({"error": "You are not the purchase creator"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self, request, *args, **kwargs):
#         try:
#             purchase_instance = Purchase.objects.get(pk=kwargs['pk'])
#         except Purchase.DoesNotExist:
#             return Response({"error": "Purchase not found"}, status=status.HTTP_404_NOT_FOUND)

#         if request.user.id == purchase_instance.employee.user.id:
#             for field_name in ['documentation', 'contract', 'tech_task', 'instruction']:
#                 file_field = getattr(purchase_instance, field_name)
#                 if file_field:
#                     file_path = os.path.join(settings.MEDIA_ROOT, str(file_field))
#                     if os.path.exists(file_path):
#                         os.remove(file_path)
#             purchase_instance.delete()
#         else:
#             return Response({"error": "You are not the purchase creator"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ClosedContractsListAPIView(generics.ListAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Purchase.objects.exclude(winner__isnull=True).only('id', 'number', 'title', 'winner')
#     serializer_class = ClosedPurchaseSerializer


# class LegalActListCreate(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = LegalAct.objects.all()
#     serializer_class = LegalActSerializer


# class LegalActUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = LegalAct.objects.all()
#     serializer_class = LegalActSerializer

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         if 'file' in request.data:
#             old_file = getattr(instance, 'file')
#             if old_file:
#                 file_path = os.path.join(settings.MEDIA_ROOT, str(old_file))
#                 if os.path.exists(file_path):
#                     os.remove(file_path)
#             setattr(instance, 'file', request.data.get('file'))
#         serializer.save()
#         return Response(serializer.data)

#     def delete(self, request, *args, **kwargs):
#         instance = self.get_object()
#         file_path = getattr(instance, 'file')
#         if file_path:
#             full_file_path = os.path.join(settings.MEDIA_ROOT, str(file_path))
#             if os.path.exists(full_file_path):
#                 os.remove(full_file_path)
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ContactInfoListCreate(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = ContactInfo.objects.all()
#     serializer_class = ContactInfoSerializer


# class ContactInfoUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ContactInfo.objects.all()
#     serializer_class = ContactInfoSerializer


# class PurchaseAdditionalDestroy(generics.DestroyAPIView):
#     queryset = PurchaseAdditional.objects.all()
#     serializer_class = PurchaseAdditionalSerialzier
