from rest_framework import serializers
from .models import subject, Assessment

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = subject
        fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'


