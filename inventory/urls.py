from django.urls import path

from djangodelights.urls import urlpatterns
from . import views


urlpatterns = [
    path("", views.index, name="index")
]