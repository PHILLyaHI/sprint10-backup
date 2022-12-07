from api.views import *
from django.urls import path

app_name = 'api'


urlpatterns = [
    path('<int:pk>/', VideoDetail.as_view(), name='detailcreate'),
    path('search/', VideoListDetailfilter.as_view(), name='videosearch'),
    path('', VideoList.as_view(), name='listcreate'),
    path('admin/create/', CreateVideo.as_view(), name="createvideo"),
    path('admin/edit/videodetail/<int:pk>/', AdminVideoDetail.as_view(), name="admindetailvideo"),
    path('admin/edit/<int:pk>/', EditVideo.as_view(), name="editvideo"),
    path('admin/delete/<int:pk>', DeleteVideo.as_view(), name="deletevideo")


]