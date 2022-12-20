from django import forms
from .models import Checkout


class CheckoutForm(forms.ModelForm):
    dishes = forms.BooleanField()

    class Meta:
        model = Checkout
        fields = '__all__'

