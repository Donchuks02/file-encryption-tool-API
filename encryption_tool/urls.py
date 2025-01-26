from django.urls import path
from . import views
from .views import UserProfileView, EncryptedFileView, DecryptFileView

urlpatterns = [
    path('profile/', views.UserProfileView.as_view()),
    path('encrypt/', views.EncryptedFileView.as_view(), name='encrypt'),
    path('decrypt/', views.DecryptFileView.as_view(), name='decrypt'),
]