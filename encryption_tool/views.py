from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError, NotFound


# imports for user profile view
from rest_framework.permissions import IsAuthenticated
from .models import Profile, EncryptedFile
from .serializers import ProfileSerializer, FileSerializer, EncryptedFileSerializer


# imports for uploaded file encryption and decryption view
from rest_framework.parsers import MultiPartParser
from .encrypt_decrypt_logic import generate_key, encrypt_file, decrypt_file


# imports to list and delete encrypted files
from rest_framework.generics import ListAPIView, DestroyAPIView




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
        try:
            file = request.FILES['file']
        except KeyError:
            raise ValidationError("No file provided")

        key = generate_key()
        encrypted_data = encrypt_file(file, key)

        encrypted_file = EncryptedFile.objects.create(
            user=request.user,
            file=file,
            encrypted_file=None,
            encryption_method='AES',
        )

        encrypted_file.encrypted_file.save(file.name + "enc", ContentFile(encrypted_data))

        encryption_key = EncryptedKey.objects.create(user=request.user, key=key.decode())

        return Response({'message': 'File encrypted successfully', 'key': key.decode()}, status=status.HTTP_201_CREATED)




class DecryptFileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            file_id = request.data['file_id']
            key = request.data['key'].encode()
        except KeyError:
            raise ValidationError("File ID and key are required")
        
        try:
            encrypted_file = EncryptedFile.objects.get(id=file_id, user=request.user)
        except EncryptedFile.DoesNotExist:
            raise NotFound("File not found")

        decrypted_data = decrypt_file(encrypted_file.encrypted_file.read(), key)
        response = HttpResponse(decrypted_data, content_type="application/octet-stream")
        response['Content-Disposition'] = f'attachment; filename="{encrypted_file.file.name}"'
        return response


class EncryptionKeyView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        keys = EncryptionKey.objects.filter(user=request.user)
        serializer = EncryptedKeySerializer(keys, many=True)
        return Response(serializer.data)



    def delete(self, request, key_id):
        try:
            encryption_key = EncryptionKey.objects.get(id=key_id, user=request.user)
            encryption_key.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except EncryptionKey.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ListEncryptedFilesView(APIView):
    serializer_class = EncryptedFileSerializer
    queryset = EncryptedFile.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class DeleteEncryptedFileView(DestroyAPIView):
    queryset = EncryptedFile.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)