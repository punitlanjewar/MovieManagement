from django.urls import path
from MovieApp import views


urlpatterns = [
    path('', views.home, name='home'),
    path('admin_home', views.admin_home_page, name='admin_home'),
    path('customer_home', views.customer_home_page, name='customer_home'),
    path('customer_login', views.customer_login_page, name='customer_login'),
    path('customer_register', views.customer_register_page, name='customer_register'),
    path('admin_login', views.admin_login_page, name='admin_login'),
    path('admin_register', views.admin_register_page, name='admin_register'),
    path('add_movie', views.add_movie_page, name='add_movie'),
    path('display_movie', views.display_movie_page, name='display_movie'),
    path('update_movie/<int:id>', views.update_movie_page, name='update_movie'),
    path('delete_movie/<int:id>', views.delete_movie_page, name='delete_movie'),
    path('customer_movie_display', views.display2_movie_page, name='customer_movie_display'),
    path('book_ticket', views.book_ticket_page, name='book_ticket'),
    path('booking_status', views.booking_status_page, name='booking_status'),
    path('booking_details', views.booking_details_page, name='booking_details'),
    path('logout', views.logout_page, name='logout'),
   

]