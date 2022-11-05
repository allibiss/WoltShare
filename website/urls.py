from django.contrib import admin
from django.urls import include, path

from . import views as my_views

app_name = 'woltshare'

urlpatterns = [
    path("", my_views.HomeView.as_view()),
    path("buy/", my_views.BuyView.as_view()),
    # path("products/<slug:food_id>", my_views.BuyProductView.as_view()),
    # path("sell", my_views.SellFormView.as_view()),
    path("product/add-form/", my_views.ProductCreateFormView.as_view(), name="product-add-form"),
    path('product/add/', my_views.product_add, name='product_add'),
    path("product/<int:pk>/", my_views.ProductView.as_view(), name="product-update"),
    path(
        "product/<int:pk>/delete/",
        my_views.ProductDeleteView.as_view(),
        name="product-delete",
    ),
]
