import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    FormView,
    RedirectView,
    TemplateView,
    UpdateView,
    View,
)
from django.views.generic.detail import DetailView

from . import api_set_order
from .api_get_price import DelFeeReq_strg, get_fee
from .forms import ProductForm, SellForm
from .models import CustomUser, Product


class HomeView(TemplateView):
    template_name = "home.html"


# class PurchaseView(RedirectView):
#     permanent = False
#     query_string = True
#     pattern_name = 'article-detail'

#     def get_redirect_url(self, *args, **kwargs):
#         article = get_object_or_404(Article, pk=kwargs['pk'])
#         article.update_counter()
#         return super().get_redirect_url(*args, **kwargs)


class LoginView(TemplateView):
    template_name = "login.html"


def purchase_view(request, pk):
    buyer = request.user

    buyer = api_set_order.User(
        buyer.name,
        buyer.address,
        buyer.phone,
        buyer.email,
    )

    product = Product.objects.get(id=pk)
    seller = product.seller
    seller = api_set_order.User(
        seller.name,
        seller.address,
        seller.phone,
        seller.email,
    )
    order = api_set_order.Order(seller, buyer, 2579)
    order_strg = api_set_order.makeOrderStrg(order)
    url = api_set_order.make_order(order_strg)

    return redirect(url)


class ProductsView(TemplateView):
    template_name = "buy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # All products
        products_pack = Product.objects.filter(food_type="PACK")  # .order_by("date")
        products_cook = Product.objects.filter(food_type="COOK")  # .order_by("date")
        context["products_pack"] = products_pack
        context["products_cook"] = products_cook
        return context


class ProductView(TemplateView):
    template_name = "product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # All products
        pk = self.kwargs["pk"]
        product = Product.objects.get(id=pk)
        shipping_cost = self._get_shipping_fee(product.seller, self.request.user)
        context["product"] = product
        context["shipping_cost"] = shipping_cost / 100
        return context

    def _get_shipping_fee(self, seller: CustomUser, buyer: CustomUser):
        start = seller.address
        end = buyer.address
        myStrgReq = DelFeeReq_strg(start, end)
        return get_fee(myStrgReq)


class ProductCreateFormView(View):
    def get(self, request):
        return render(request, "post_form.html")

    def post(self, request):
        return redirect("/product/")


class ProductDeleteView(DeleteView):
    product = Product


class DoneView(TemplateView):
    template_name = "done.html"


class CustomUserView(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # All products
        pk = self.kwargs["pk"]
        user = CustomUser.objects.get(id=pk)
        context["user"] = user
        return context


class CustomUserOwnView(TemplateView):
    template_name = "profile.html"


#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.add_product()
#         return super().form_valid(form)


def product_add(request):
    data = {}
    if request.method == "POST":
        data = request.POST.dict()

        print("hee", CustomUser.objects.all())
        print("hoo", CustomUser.objects.all()[0])
        seller = CustomUser.objects.all()[0]

        quantity = data["quantity"]
        price_per_quant = data["price_per_quant"]
        description = data["description"]
        food_type = data["food_type"]
        if "packaging" in data:
            packaging = data["packaging"] == "on"
        else:
            packaging = False

        # image = data["image"]

        print("pack", packaging)

        # # rules
        # if "rules" not in data:
        #     # reload? not let forward
        #     return render(
        #         request,
        #         "post_form.html",
        #         {"error": "Accept terms of condition, please!"},
        #     )

        print("PRODS", Product.objects.all().values())
        product.save()

    return render(request, "success.html", {"product": data})
