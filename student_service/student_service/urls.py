from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("api/students/", include("student_service.urls")),
#     path("api/auth/", include("auth_service.urls")),
# ]

router =DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')

url_patterns = router.urls
