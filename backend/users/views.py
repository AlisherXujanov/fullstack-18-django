from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # def post(self, request):
    #     serializer = ProfileSerializer(request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(
    #             {"data": "Profile created successfully"},
    #             status=status.HTTP_201_CREATED)
    #     return Response({
    #         "error": serializer.errors
    #     }, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"data": "Profile updated successfully"},
                status=status.HTTP_200_OK)
        return Response({
            "error": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)