from django.urls import path
from .views import coming, index
from .forms import ServerForm

urlpatterns = [
    path('', coming),
    path('index', index, ServerForm, name="Emails")
]