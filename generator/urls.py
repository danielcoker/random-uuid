from django.urls import path
from .views import generate_uuid


urlpatterns = [
    path('uuid/generate', generate_uuid, name='uuid-generator')
]
