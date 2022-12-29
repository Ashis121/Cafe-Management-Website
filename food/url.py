from django.urls import URLPattern, path

from . import views

urlpatterns =[
    path('menu/',views.menu,name='menu'),
    path('details/<int:id>/',views.details,name='details'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.cart,name='cart'),
    path('delete_cart_items/<str:id>',views.delete_cart_items,name='delete_cart_items'),
    path('check_out',views.check_out,name='check_out'),
    path('place_order',views.place_order,name='place_order'),
    path('orders',views.orders,name='orders')
    
]