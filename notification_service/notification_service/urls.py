from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import NotificationViewSet, MessageViewSet, AnnouncementViewSet, AlertViewSet

router = routers.DefaultRouter()
router.register(r"notifications", NotificationViewSet)
router.register(r"messages", MessageViewSet)
router.register(r"announcements", AnnouncementViewSet)
router.register(r"alerts", AlertViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    # path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
