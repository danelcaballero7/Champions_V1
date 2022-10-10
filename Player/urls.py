from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add_player/', views.add_player_function, name='add'),
    path('update_player/<player_id>', views.update_player_function, name='update'),
    path('delete_player/<player_id>', views.delete_player_function, name='delete'),
]