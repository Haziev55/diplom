from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet
router = DefaultRouter()
from django.shortcuts import redirect
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', views.oil_product_list, name='oil_product_list'),
    path('add/', views.add_oil_product, name='add_oil_product'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('api/', include(router.urls)),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name='home'),  # страница после входа
    path('report/pdf/', views.generate_pdf, name='generate_pdf'),
    path('report/excel/', views.generate_excel, name='generate_excel'),
    path('chart/', views.generate_chart, name='generate_chart'),
    path('api/', include(router.urls)),
    path('', lambda request: redirect('home')),  # Перенаправляет на главную страницу
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('add/', views.add_oil_product, name='add_oil_product'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('report/pdf/', views.generate_pdf, name='generate_pdf'),
    path('report/excel/', views.generate_excel, name='generate_excel'),
    path('profile/', views.profile, name='profile'),
    path('base/', views.show_base, name='show_base'),
    path('', views.home, name='home'),  # Главная страница
    path('добавить/', views.add_oil_product, name='add_oil_product'),  # Добавление нефтепродукта
    path('transactions/', views.transaction_list, name='transaction_list'),  # Список транзакций
    path('report/pdf/', views.generate_pdf_report, name='generate_pdf'),  # Отчет PDF
    path('report/excel/', views.generate_excel_report, name='generate_excel'),  # Отчет Excel
    path('profile/', views.profile, name='profile'),  # Профиль пользователя
]

