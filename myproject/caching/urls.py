from django import views
from django.contrib import admin
from django.urls import path
from caching import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cache-data/', views.fetch_cached_data , name='fetch_cached_data'),
    path('get-keys/', views.get_cached_keys, name='get_cached_keys'),   
]