from django.urls import path
from .views import registerView
from rest_framework_simplejwt.views import  TokenObtainPairView, TokenRefreshView  

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("register/", registerView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
