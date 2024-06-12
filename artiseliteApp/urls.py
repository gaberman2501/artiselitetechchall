# inventory/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('manager/', views.managerhome, name='manager_home'), 
    path('operator/', views.operatorhome, name='operator_home'), 
    path('view_inbound/', views.view_incoming_products, name='view_inbound'),
    path('view_outbound/', views.view_outgoing_products, name='view_outgoing'),
    path('add/', views.add_product, name='add_product'),
    path('view/', views.view_products, name='view_products'),
    path('update_product/', views.update_product, name='update_product'),
    path('search/', views.search_products, name='search_products'),
    path('add_supplier/', views.add_supplier, name='add_supplier'),
    path('add_incoming_product/', views.add_incoming_product, name='add_incoming_product'),
]
