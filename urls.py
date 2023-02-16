from django.urls import path
from .views import authPageView

urlpatterns = [
    path("", authPageView, name="auth"),
]