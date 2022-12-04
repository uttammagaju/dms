from django.urls import path,include
from . import views


app_name = 'dashboard'

urlpatterns =[
    path('',views.DashboardHomeView.as_view(),name = 'index'),

    #Company
    path('companies',views.CompanyListView.as_view(),name = 'companies-list'),
    path('companies/create',views.CompanyCreateView.as_view(),name = 'companies-create'),
    path('companies/<int:pk>/update',views.CompanyUpdateView.as_view(), name = 'companies-update'),
    path('companies/<int:pk>/delete/',views.CompanyDeleteView.as_view(), name = 'companies-delete'), 
    path('companies/<int:pk>/detail/',views.CompanyDetailView.as_view(), name = 'companies-detail'),

    #Product 
    path('products',views.ProductListView.as_view(), name = 'products-list'),
    path('products/create',views.ProductCreateView.as_view(),name = 'products-create'),
    path('products/<int:pk>/update',views.ProductUpdateView.as_view(), name = 'products-update'),
    path('products/<int:pk>/delete/',views.ProductDeleteView.as_view(), name = 'products-delete'), 
    path('products/<int:pk>/detail/',views.ProductDetailView.as_view(), name = 'products-detail'),
    
    #Order
    path('orders',views.OrderListView.as_view(), name = 'orders-list'),
    path('orders/create',views.OrderCreateView.as_view(),name = 'orders-create'),
    path('orders/<int:pk>/update',views.OrderUpdateView.as_view(), name = 'orders-update'),
    path('orders/<int:pk>/delete/',views.OrderDeleteView.as_view(), name = 'orders-delete'), 
    path('orders/<int:pk>/detail/',views.OrderDetailView.as_view(), name = 'orders-detail'),
]