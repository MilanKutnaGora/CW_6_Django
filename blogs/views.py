from django.conf import settings
from django.core.cache import cache
from django.views.generic import DetailView

from blogs.models import Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object()
        self.object.views_count += 1
        self.object.save()
        return self.object
