from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy

# Create your views here.
from . models import *
from . forms import *

class DashboardHomeView(TemplateView):
    template_name= "dashboard/index.html"

#Company view
class CompanyListView(ListView):
    template_name = 'dashboard/companies/list.html'
    model = Company


class CompanyCreateView(CreateView):
    template_name = 'dashboard/companies/form.html'
    form_class = CompanyForm
    success_url = reverse_lazy('dashboard:companies-list')


class CompanyUpdateView(UpdateView):
    template_name = 'dashboard/companies/form.html'
    form_class = CompanyForm
    model = Company
    success_url = reverse_lazy('dashboard:companies-list')


class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('dashboard:companies-list')


class CompanyDetailView(DetailView):
    template_name = 'dashboard/companies/form.html'
    model = Company

#Product View
class ProductListView(ListView):
    template_name = 'dashboard/products/list.html'
    model = Product


class ProductCreateView(CreateView):
    template_name = 'dashboard/products/form.html'
    form_class = ProductForm
    success_url = reverse_lazy('dashboard:products-list')

class ProductUpdateView(UpdateView):
    template_name = 'dashboard/products/form.html'
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('dashboard:products-list')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('dashboard:products-list')

class ProductDetailView(DetailView):
    template_name = 'dashboard/products/form.html'
    model = Product

#order view
class OrderListView(ListView):
    template_name = 'dashboard/orders/list.html'
    model = Order


class OrderCreateView(CreateView):
    template_name = 'dashboard/orders/form.html'
    form_class = OrderForm
    success_url = reverse_lazy('dashboard:orders-list')

class OrderUpdateView(UpdateView):
    template_name = 'dashboard/orders/form.html'
    form_class = OrderForm
    model = Order
    success_url = reverse_lazy('dashboard:orders-list')

class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('dashboard:orders-list')

class OrderDetailView(DetailView):
    template_name = 'dashboard/orders/form.html'
    model = Order