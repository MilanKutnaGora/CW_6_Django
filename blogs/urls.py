from django.urls import path
from django.views.decorators.cache import cache_page

from blogs.apps import BlogsConfig
from blogs.views import BlogDetailView

app_name = BlogsConfig.name

urlpatterns = [
    path('blog/article/<slug>', cache_page(60)(BlogDetailView.as_view()), name='article'),

]