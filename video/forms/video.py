from django.forms import models, forms, ModelForm

from video.models import Video


class VideoModelForm(ModelForm):
    class Meta:
        model = Video
        fields = "__all__"
