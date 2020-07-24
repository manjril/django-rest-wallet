from django.urls import path, include
from rest_framework.routers import DefaultRouter

from budget import views

router = DefaultRouter()
router.register(r'transactions', views.TransactionViewset)
router.register(r'wallet', views.WalletViewset)
router.register(r'update-wallet', views.BalanceUpdateViewSet, basename='test')

urlpatterns = [
    path('', include(router.urls)),

]
