from django.urls import path, include

from django_basic_app_car_collection_app.car_collection import views


urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('profile/create', views.create_profile, name='create-profile'),
    path('profile/edit', views.edit_profile, name='edit-profile'),
    path('profile/delete', views.delete_profile, name='delete-profile'),
    path('profile/details', views.details_profile, name='details-profile'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('car/<int:pk>/details', views.details_car, name='details-car'),
    path('car/<int:pk>/delete', views.delete_car, name='delete-car'),
    path('car/<int:pk>/edit', views.edit_car, name='edit_car'),
    path('car/create/', views.create_car, name='car-create')
]