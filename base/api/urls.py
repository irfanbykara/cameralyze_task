from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_routes),
    path( 'books/', views.fetch_books ),
    path( 'books/<str:pk>/', views.retrieve_book ),
    path('add-book/', views.add_book),
    path( 'delete-book/<str:pk>', views.delete_book ),
    path( 'update-book/<str:pk>', views.update_book ),

]
