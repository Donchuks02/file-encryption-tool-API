from django.urls import path
from . import views
from .views import UserProfileView, EncryptedFileView, DecryptFileView, EncryptionKeyView, ListEncryptedFilesView, DeleteEncryptedFileView

urlpatterns = [
    path('profile/', UserProfileView.as_view()),
    path('encrypt/', EncryptedFileView.as_view(), name='encrypt'),
    path('decrypt/', DecryptFileView.as_view(), name='decrypt'),
    path('keys/', EncryptionKeyView.as_view(), name='keys'),
    path('keys/<int:key_id>/', views.EncryptionKeyView.as_view(), name='delete_key'),
    path('files/', ListEncryptedFilesView.as_view(), name='list-files'),
    path('files/<int:pk>/', DeleteEncryptedFileView.as_view(), name='delete-file'),
]