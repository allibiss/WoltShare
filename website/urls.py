from django.contrib import admin
from django.urls import include, path

from . import views as my_views

urlpatterns = [
    path("", my_views.HomeView.as_view()),
    path("buy", my_views.BuyView.as_view()),
    # path("products/<slug:food_id>", my_views.BuyProductView.as_view()),
    # path("sell", my_views.SellFormView.as_view()),
    path("product/add/", my_views.ProductCreateView.as_view(), name="product-add"),
    path(
        "product/<int:pk>/", my_views.ProductUpdateView.as_view(), name="product-update"
    ),
    path(
        "product/<int:pk>/delete/",
        my_views.ProductDeleteView.as_view(),
        name="product-delete",
    ),
]
