from django import forms
from .models import Checkout


class CheckoutForm(forms.ModelForm):
    dish = forms.BooleanField()

    class Meta:
        model = Checkout
        fields = ['dish']