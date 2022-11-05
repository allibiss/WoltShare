from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    FormView,
    TemplateView,
    UpdateView,
)

from .forms import SellForm, ProductForm
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
        products = Product.objects.all()  # .order_by("date")
        context["products"] = products
        return context


class ProductView(TemplateView):
    template_name = "product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # All products
        pk = self.kwargs["pk"]
        product = Product.objects.get(id=pk)
        context["product"] = product
        return context


# class BuyProductView(TemplateView):
#     template_name = "buy_product.html"


class ProductCreateFormView(CreateView):
    template_name = "post_form.html"
    model = Product
    form_class = ProductForm
    # fields = [
    #     "seller",
    #     "quantity",
    #     "price_per_quant",
    #     "description",
    #     "type",
    #     "packaging",
    # ]

    def get_success_url(self):
        return reverse("product-update", kwargs={"pk": self.object.lawyer_slug})


class ProductDeleteView(DeleteView):
    Product = Product
    # success_url = reverse_lazy('author-list'){% csrf_token %}


# class SellFormView(FormView):
#     template_name = "sell.html"
#     form_class = SellForm
#     success_url = "/thanks"

#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.add_product()
#         return super().form_valid(form)


def product_add(request):
    if request.method == "POST":
        data = request.POST.dict()
        action = data.get("firstname")

        user = User.objects.all()[0]
        product = Product(
            seller=user,
            quantity = 55,
            price_per_quant = 123,
            description = 'Very nice ratatouille',
            type = 'Big food',
            packaging = 'True',
            )
        product.save()

    return render(request, "success.html", {"product": data})
