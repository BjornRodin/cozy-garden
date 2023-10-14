from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
    path('add_favorite/<int:product_id>',
         views.add_favorite, name='add_favorite'),
]
