from django.views.generic import DetailView
from models import Post, PUBLISHED
from django.shortcuts import get_object_or_404


class PostDetailView(DetailView):
    def get_object(self):
        return get_object_or_404(Post, status=PUBLISHED)
