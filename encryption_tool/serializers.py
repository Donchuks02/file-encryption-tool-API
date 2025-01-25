from rest_framework import serializers
from .models import Profile
from .models import EncryptedFile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'



class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncryptedFile
        fields = ['file', 'encrypted_method', 'encrypted_file']
        read_only_fields = ['encrypted_file']
    