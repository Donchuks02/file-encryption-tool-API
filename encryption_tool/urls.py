from django.urls import path
from . import views
import views 

urlpatterns = [
    path('profile/', views.UserProfileView.as_view()),
    path('encrypt/', views.EncryptedFileView.as_view(), name='encrypt'),
    path('decrypt/', views.DecryptFileView.as_view(), name='decrypt'),
    path('keys/', views.EncryptionKeyView.as_view(), name='keys'),
    path('keys/<int:key_id>/', views.EncryptionKeyView.as_view(), name='delete_key'),
    path('files/', views.ListEncryptedFilesView.as_view(), name='list-files'),
    path('files/<int:pk>/', views.DeleteEncryptedFileView.as_view(), name='delete-file'),
    path('analytics/', views.AnalyticsView.as_view(), name='analytics'),
]