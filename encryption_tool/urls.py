from django.urls import path
from . import views
from .views import UserProfileView, EncryptedFileView, DecryptFileView, EncryptionKeyView

urlpatterns = [
    path('profile/', UserProfileView.as_view()),
    path('encrypt/', EncryptedFileView.as_view(), name='encrypt'),
    path('decrypt/', DecryptFileView.as_view(), name='decrypt'),
    path('keys/', EncryptionKeyView.as_view(), name='keys'),
    path('keys/<int:key_id>/', views.EncryptionKeyView.as_view(), name='delete_key'),
]