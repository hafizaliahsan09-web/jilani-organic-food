from django import forms
from .models import Buyer

class BuyerForm(forms.ModelForm):
    QUANTITY_CHOICES = [
        ('250g', '250g'),
        ('500g', '500g'),
        ('1000g', '1000g'),
    ]

    PRODUCT_CHOICES = [
        ('honey', '🍯 Honey'),
        ('desi_ghee', '🧈 Desi Ghee'),
    ]

    quantity = forms.ChoiceField(
        choices=QUANTITY_CHOICES,
        widget=forms.RadioSelect,
        label="Select Quantity"
    )

    product = forms.ChoiceField(
        choices=PRODUCT_CHOICES,
        widget=forms.Select,
        label="Select Product"
    )


    class Meta:
        model = Buyer
        fields = ['name', 'fathername', 'email', 'phone', 'address', 'product', 'quantity']
        widgets = {
            'quantity': forms.RadioSelect(),  # ✅ radio buttons
        }
    
