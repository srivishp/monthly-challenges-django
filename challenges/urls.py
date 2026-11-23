from django.urls import path
from . import views

urlpatterns = [
    # Points to the actual monthly challenges
    path("january", views.index)
]
