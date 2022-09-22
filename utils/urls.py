from django.urls import path

from utils.views import Index


app_name = 'utils'


urlpatterns = [
    path('', Index.as_view(), name='index'),
]
