from django.shortcuts import get_object_or_404
from projectapp.models import Video
from .serializers import VideoSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAuthenticated, AllowAny
from rest_framework import filters, generics, viewsets, status 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

class VideoUserWritePermission(BasePermission):
    message = 'Editing videos is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user


class VideoList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

class VideoDetail(generics.RetrieveAPIView):
    serializer_class = VideoSerializer
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Video, id=item)


class VideoListDetailfilter(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title']



# class CreateVideo(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer

class CreateVideo(APIView):
    permissions_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminVideoDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    quesryset = Video.objects.all()
    serializer_class = VideoSerializer

class EditVideo(generics.UpdateAPIView):
    permission_classes = [VideoUserWritePermission]
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

class DeleteVideo(generics.RetrieveDestroyAPIView):
    permission_classes = [VideoUserWritePermission]
    serializer_class = VideoSerializer
    queryset = Video.objects.all()