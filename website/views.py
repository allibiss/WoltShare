from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.views.generic import (
    CreateView,
    DeleteView,
    FormView,
    TemplateView,
    UpdateView,
)

from .forms import SellForm
from .models import Product, User


class ProfileView(TemplateView):
    template_name = "profile.html"


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


# class BuyProductView(TemplateView):
#     template_name = "buy_product.html"


class ProductCreateView(CreateView):
    model = Product
    fields = [
        "seller",
        "quantity",
        "price_per_quant",
        "description",
        "type",
        "packaging",
    ]


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name"]


class ProductDeleteView(DeleteView):
    model = Product
    # success_url = reverse_lazy('author-list')


# class SellFormView(FormView):
#     template_name = "sell.html"
#     form_class = SellForm
#     success_url = "/thanks"

#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.add_product()
#         return super().form_valid(form)
