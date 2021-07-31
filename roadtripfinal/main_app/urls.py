from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('roadtrip/', views.roadtrip, name="roadtrip_list"),
    path('roadtrip/<int:id>/delete/', views.roadtrip_delete, name="roadtrip_delete"),
    path('roadtrip_update/<int:id>/update/', views.roadtrip_update, name="roadtrip_update"),
    path('roadtrip/<int:id>/', views.roadtrip_detail, name="roadtrip_detail"),
    path('roadtrip_create', views.roadtrip_create, name='roadtrip_create'),
    path('about/', views.about, name="about"),
]