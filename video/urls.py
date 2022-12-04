from django.urls import path

from video.views import VideoListView, VideoCreateView

app_name = "video"

urlpatterns = [
    path("", VideoListView.as_view(), name='list'),
    path("new/", VideoCreateView.as_view(), name='new'),
]
