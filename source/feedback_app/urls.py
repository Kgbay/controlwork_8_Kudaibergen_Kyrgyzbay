from django.urls import path

from .views.base import IndexView
from .views.products import ProductCreateView, ProductDetail, ProductDeleteView, ProductUpdateView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("product/add/", ProductCreateView.as_view(), name='product_add'),
    path("products/<int:pk>/", ProductDetail.as_view(), name='product_view'),
    path("products/<int:pk>/remove/", ProductDeleteView.as_view(), name='remove_product'),
    path("products/<int:pk>/confirm_remove/", ProductDeleteView.as_view(), name='confirm_remove_product'),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="update_product"),
]