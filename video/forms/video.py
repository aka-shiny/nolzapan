from django.forms import ModelForm

from video.models import Video


class VideoModelForm(ModelForm[Video]):
    class Meta:
        model = Video
        fields = "__all__"
