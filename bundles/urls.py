from . import views
from django.urls import path

urlpatterns = [
    path('', views.bundles, name='bundles'),
    path('api/bundles/', views.bundle_list, name='bundle-list'),
    path('api/bundles/<int:pk>/', views.bundle_detail, name='bundle-detail'),
]