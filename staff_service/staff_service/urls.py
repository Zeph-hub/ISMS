from rest_framework import viewsets
from views import StaffViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'staff', StaffViewSet)

urlpatterns = router.urls