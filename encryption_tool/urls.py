from django.urls import path
from . import views
from .views import UserProfileView

urlpatterns = [
    path('profile/', views.UserProfileView.as_view()),
]