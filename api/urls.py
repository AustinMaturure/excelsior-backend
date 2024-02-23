from django.urls import path
from . import views


urlpatterns = [
    path('', views.getData),
    path('articles/', views.getData),
    path('categories/', views.getCategoryData),
    path('increment_views', views.increment_views)
]
