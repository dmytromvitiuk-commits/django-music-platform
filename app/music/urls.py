from django.urls import path
from . import views

urlpatterns = [
   
    path('categories/', views.category_list_view, name='category_list'),
    path('categories/add/', views.category_create_view, name='category_create'),
    path('categories/<int:id>/', views.category_detail_view, name='category_detail'),
    path('categories/<int:id>/edit/', views.category_update_view, name='category_update'),
    path('categories/<int:id>/delete/', views.category_delete_view, name='category_delete'),

     
    path('tracks/', views.product_list_view, name='product_list'),
    path('tracks/add/', views.product_create_view, name='product_create'),
    path('tracks/<int:id>/', views.product_detail_view, name='product_detail'),
    path('tracks/<int:id>/edit/', views.product_update_view, name='product_update'),
    path('tracks/<int:id>/delete/', views.product_delete_view, name='product_delete'),

    # Artist (Виконавці)
    path('artists/', views.artist_list_view, name='artist_list'),
    path('artists/add/', views.artist_create_view, name='artist_create'),
    path('artists/<int:id>/', views.artist_detail_view, name='artist_detail'),
    path('artists/<int:id>/edit/', views.artist_update_view, name='artist_update'),
    path('artists/<int:id>/delete/', views.artist_delete_view, name='artist_delete'),
]