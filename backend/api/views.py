from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from.serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from.models import*
# Create your views here.

class NoteListCreate(generics.ListCreateAPIView):
    
    serializer_class=NoteSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user=self.request.user
        return Note.objects.filter(author=user)
    def perform_create(self, serializer):
        if serializers.is_valid:
            serializer.save(author=self.request.user)
        else:
            print(serializers.errors)
class NoteDelete(generics.DestroyAPIView):
    
    serializer_class=NoteSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user=self.request.user
        return Note.objects.filter(author=user)


class CreateUserView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes = [AllowAny]

