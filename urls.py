from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurant/<int:id>/', views.restaurant_detail, name='restaurant_detail'),
    path('book/<int:table_id>/', views.book_table, name='book_table'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
