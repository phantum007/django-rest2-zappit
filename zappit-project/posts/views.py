from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post, Vote
from .serializer import Postserializer, Voteserializer

# Create your views here.
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


# Create your views here.
class VoteCreate(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = Voteserializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, post=post)

    def perform_create(self, serializer):
        serializer.save(voter=self.request.user, post= Post.objects.get(pk=self.kwargs('pk')))