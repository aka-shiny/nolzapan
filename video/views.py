from typing import Any, Dict

from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView

from video.forms.video import VideoModelForm
from video.models import Video


class VideoListView(ListView["VideoListVIew"]):
    model = Video
    paginate_by = 15

    def get_queryset(self):
        qs = super(VideoListView, self).get_queryset()
        return qs

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(VideoListView, self).get_context_data()
        context = {"form": context}
        return context


class VideoCreateView(CreateView):
    model = Video
    form_class = VideoModelForm
    template_name = "video/video_form.html"

    def get(self, request: HttpRequest) -> TemplateResponse:
        return TemplateResponse(request=request, template=self.get_template_names())

    def post(self, request: HttpRequest) -> HttpResponse:
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("video:list"))
        else:
            return HttpResponse(form.errors.values())


class VideoDetailView(DetailView):
    model = Video
