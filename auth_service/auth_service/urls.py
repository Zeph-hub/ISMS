from django.urls import path
from .views import registerView, RootView
from rest_framework_simplejwt.views import  TokenObtainPairView, TokenRefreshView  

urlpatterns = [
    path("", RootView.as_view(), name="root"),
    path("register/", registerView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
