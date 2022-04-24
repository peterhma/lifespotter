from django.urls import path
from . import views

urlpatterns = [
  path('main/<slug:authorname>/', views.index),
  path('sighting/<slug:authorname>/<slug:id>/', views.sighting),
  path('trip/<slug:authorname>/<slug:id>/', views.trip),
  path('species/<slug:species_id>/', views.species),
  path('', views.index),
]
