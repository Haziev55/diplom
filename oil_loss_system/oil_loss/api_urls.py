from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OilProductViewSet, StorageViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'oil-products', OilProductViewSet)
router.register(r'storage', StorageViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
