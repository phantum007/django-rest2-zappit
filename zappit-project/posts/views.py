from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializer import Postserializer

# Create your views here.
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer
