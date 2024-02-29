from django.urls import path
from .views import *


urlpatterns = [

    path('', ProductsView.as_view(), name="all-products"),
    path('add/', ProductAddView.as_view(), name="add-products"),
    path('detail/<pk>/', ProductDetailView.as_view(), name='detail-products'),
    path('update/<pk>/', ProductUpdateView.as_view(), name='update-products'),
    path('delete/<pk>/', ProductDeleteView.as_view(), name='delete-products'),
]