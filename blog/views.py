from django.views.generic import DetailView
from models import PUBLISHED
from django.http import Http404, HttpResponseRedirect


class PostDetailView(DetailView):
    def get_object(self):
        post = super(PostDetailView, self).get_object()
        if post.status != PUBLISHED:
            raise Http404
        return post

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        if not request.META["PATH_INFO"].endswith(post.slug + "/"):
            return HttpResponseRedirect(post.get_absolute_url())
        else:
            return super(PostDetailView, self).get(request, *args, **kwargs)
