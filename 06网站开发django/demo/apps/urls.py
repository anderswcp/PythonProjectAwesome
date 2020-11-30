from django.urls import path
from .views import index

app_name = 'apps'
urlpatterns = [
    path('', index, name='index')
]
