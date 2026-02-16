from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, AssessmentViewSet

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet, basename='subjects')
router.register(r'assessments', AssessmentViewSet, basename='assessments')

urlpatterns = router.urls