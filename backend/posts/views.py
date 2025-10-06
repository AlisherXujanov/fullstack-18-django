from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Posts
from .serializers import PostsSerializer

# Create your views here.

class PostsAPIView(APIView):

    def get(self, request):
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response({"data": serializer.data }, status=status.HTTP_200_OK)
