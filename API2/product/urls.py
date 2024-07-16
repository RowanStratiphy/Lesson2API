from django.urls import path
from .views import listproducts

urlpatterns = [
    path('productlist/', listproducts, name='ListProducts'),
]