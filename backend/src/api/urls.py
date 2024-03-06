from django.urls import path
from src.api.views import ApiController

urlpatterns=[
    path('get-data',ApiController.as_view())
]