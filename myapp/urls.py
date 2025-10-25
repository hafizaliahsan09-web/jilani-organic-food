from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("newpage/", views.new_page, name="newpage"),
    path('orders/', views.orders, name='orders'), 
    path('buy-now/', views.buy_now, name='buy_now'),
    path('order/', views.order_form, name='order_form'),
    path('thankyou/', views.thankyou, name='thankyou'),  # thank-you page
]







