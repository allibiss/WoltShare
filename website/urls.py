from django.contrib import admin
from django.urls import include, path

from . import views as my_views

urlpatterns = [
    path("", my_views.HomeView.as_view()),
    path("buy", my_views.BuyView.as_view()),
    path("buy/<slug:food_id>", my_views.BuyProductView.as_view()),
    path("sell", my_views.SellView.as_view()),
]
