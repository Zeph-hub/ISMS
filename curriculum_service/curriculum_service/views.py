from rest_framework import viewsets
from .models import subject, Assessment
from .serializers import SubjectSerializer, AssessmentSerializer
from rest_framework.permissions import IsAuthenticated

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    Permission_classes = [IsAuthenticated]

