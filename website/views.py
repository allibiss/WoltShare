from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class HomeView(TemplateView):
    template_name = "home.html"


class BuyView(TemplateView):
    template_name = "buy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # All products
        products = Product.objects.all()   #.order_by("date")
        context["products"] = products
        return context


class BuyProductView(TemplateView):
    template_name = "buy_product.html"


class SellView(TemplateView):
    template_name = "sell.html"
