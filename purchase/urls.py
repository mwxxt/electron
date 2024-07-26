# from django.urls import path
# from . import views

# urlpatterns = [
#     path('purchase-types/', views.PurchaseTypeAPIView.as_view()), # тип закупок
#     path('purchase-additional/<int:pk>/', views.PurchaseAdditionalDestroy.as_view()), # квалификация и требования удаление
#     path('purchases/', views.PurchaseAPIView.as_view()), # закупки
#     path('purchase/<int:pk>/', views.PurchaseDetailAPIView.as_view()), # закупка по id
#     path('closed-contracts/', views.ClosedContractsListAPIView.as_view()),
#     path('legal-act/', views.LegalActListCreate.as_view()), # нормативно-правовые акты
#     path('legal-act/<int:pk>/', views.LegalActUpdateDestroy.as_view()),
#     path('contact-info/', views.ContactInfoListCreate.as_view()), # контактная информация
#     path('contact-info/<int:pk>/', views.ContactInfoUpdateDestroy.as_view()),
# ]
