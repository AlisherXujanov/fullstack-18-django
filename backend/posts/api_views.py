from rest_framework import permissions, viewsets
from .models import Posts
from .serializers import PostsSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('-created_at')
    serializer_class = PostsSerializer
    permission_classes = [permissions.AllowAny]
