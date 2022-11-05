from django import forms


class SellForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def add_product(self):
        # send email using the self.cleaned_data dictionary
        print("add_product", self.cleaned_data)
