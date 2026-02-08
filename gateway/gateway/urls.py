from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("auth_service.urls")),
    path("students/", include("student_service.urls")),
    path("staff/", include("staff_service.urls")),
    path("curriculum/", include("curriculum_service.urls")),
    path("finance/", include("finance_service.urls")),
    path("notifications/", include("notification_service.urls")),
    
]
