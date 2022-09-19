from django.urls import path

from blog.views import Feed


app_name = 'blog'


urlpatterns = [
    path('', Feed.as_view(), name='feed'),
]
