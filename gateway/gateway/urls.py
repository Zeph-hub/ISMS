from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", views.auth_proxy, name="auth_proxy"),
    path("students/", views.students_proxy, name="students_proxy"),
    path("staff/", views.staff_proxy, name="staff_proxy"),
    path("finance/", views.finance_proxy, name="finance_proxy"),
    path("notifications/", views.notifications_proxy, name="notifications_proxy"),
    path("curriculum/", views.curriculum_proxy, name="curriculum_proxy"),
]