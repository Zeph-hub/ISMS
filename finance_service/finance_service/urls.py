from rest_framework import routers
from .views import TransactionViewSet, FeeViewSet
from django.contrib import admin
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r"transactions", TransactionViewSet)
router.register(r"fees", FeeViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)), 
]
