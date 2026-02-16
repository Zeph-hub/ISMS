from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from .models import User


class registerView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class RootView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response({
            "message": "Auth service running",
            "endpoints": ["/register/", "/token/", "/token/refresh/"]
        })