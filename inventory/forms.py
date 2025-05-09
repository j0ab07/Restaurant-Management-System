from django import forms
from .models import Stock

# Form for adding new stock items
class AddStockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['item_name', 'quantity', 'supplier_name', 'supplier_contact']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'supplier_name': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_contact': forms.TextInput(attrs={'class': 'form-control'}),
        }
    