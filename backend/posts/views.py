from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Posts
from .serializers import PostsSerializer

# Create your views here.

class PostsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response({"data": serializer.data }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data }, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        # post = Posts.objects.get(id=pk)
        # if post:
        if post := Posts.objects.get(id=pk):
            post.delete()
            return Response({"data": "Post deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    # user = User.objects.create_user(username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=200)
    else:
        return Response({'error': 'Wrong credentials'}, status=400)
