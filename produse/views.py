from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView

from produse.models import Produse

from .forms import ProductForm, CategoriiProduseForm


# Create your views here.
class ProductsView(ListView):
    template_name = 'produse/products.html'
    model = Produse


class ProductDetailView(DetailView):
    template_name = 'produse/details.html'
    model = Produse


class ProductAddView(CreateView):
    template_name = 'produse/product_form.html'
    success_url = reverse_lazy('all-products')
    form_class = ProductForm
    model = Produse


class ProductUpdateView(UpdateView):
    template_name = 'produse/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('all-products')
    model = Produse


class ProductDeleteView(DeleteView):
    template_name = 'produse/delete_confirmation.html'
    success_url = reverse_lazy('all-products')
    model = Produse
