from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class BuyView(TemplateView):
    template_name = "buy.html"


class BuyProductView(TemplateView):
    template_name = "buy_product.html"


class SellView(TemplateView):
    template_name = "sell.html"
