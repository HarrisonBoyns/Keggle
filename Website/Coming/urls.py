from django.urls import path
from .views import coming, index

urlpatterns = [
    path('coming', coming),
    path('index', index)
]