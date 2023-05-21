
from django.contrib import admin
from django.urls import path, include

import django_basic_app_car_collection_app.car_collection.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(django_basic_app_car_collection_app.car_collection.urls))
]
