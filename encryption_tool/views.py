from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# imports for user profile view
from rest_framework.permissions import IsAuthenticated
from .models import Profile, EncryptedFile
from .serializers import ProfileSerializer, FileSerializer


# imports for uploaded file encryption and decryption view
from rest_framework.parsers import MultiPartParser
from .encrypt_decrypt_logic import encrypt_file, decrypt_file




# Create your views here.


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = request.user.profile
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        profile = request.user.profile
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class EncryptedFileView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.FILES['file']
        key = generate_key()
        encrypted_data = encrypt_file(file, key)

        encrypted_file = EncryptedFile.objects.create(
            user=request.user,
            file=file,
            encrypted_file=None,
            encryption_method='AES',
        )

        encrypted_file.encrypted_file.save(file.name + "enc", ContentFile(encrypted_data))
        return Response({'message': 'File encrypted successfully', 'key': key.decode()})




class DecryptFileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file_id = request.data['file_id']
        key = request.data['key'].encode()
        encrypted_file = EncryptedFile.objects.get(id=file_id, user=request.user)

        decrypted_data = decrypt_file(encrypted_file.encrypted_file.read(), key)
        response = HttpResponse(decrypted_data, content_type="application/octet-stream")
        response['Content-Disposition'] = f'attachment; filename="{encrypted_file.file.name}"'
        return response
