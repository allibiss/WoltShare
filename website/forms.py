from django import forms

from .models import Product


class SellForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def add_product(self):
        # send email using the self.cleaned_data dictionary
        print("add_product", self.cleaned_data)


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # for visible in self.visible_fields():
        #     visible.label.widget.attrs['class'] = 'form-control-label'

        # for visible in self.visible_fields():
        #     visible.field.widget.attrs['class'] = 'form-control'
        # visible.label.widget.attrs['class'] = 'form-control'

    # class Meta:
    #     model = Product
    #     fields = [
    #         "seller",
    #         "quantity",
    #         "price_per_quant",
    #         "description",
    #         "food_type",
    #         "packaging",
    #     ]
