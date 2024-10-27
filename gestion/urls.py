from django.urls import path

from . import views

urlpatterns = [
    
    path('gestion/users/', views.user_list, name="user_list"),
    path("gestion/users/<int:user_id>/", views.user_detail, name="user_detail"),
    path("gestion/users/create/", views.user_create, name="user_create"),
    path("gestion/users/<int:user_id>/update/", views.user_update, name="user_update"),
    path("gestion/users/<int:user_id>/delete/", views.user_delete, name="user_delete"),
]