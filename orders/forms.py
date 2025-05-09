from django import forms
from .models import Menu, MenuIngredients
from inventory.models import Stock

# Form for adding new menu items
class AddMenuItemForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'description', 'price', 'allergens']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
        }
        
# Form for adding ingredients to menu items
class MenuIngredientForm(forms.ModelForm):
    class Meta:
        model = MenuIngredients
        fields = ['stock_item', 'quantity_required']
        widgets = {
            'quantity_required': forms.NumberInput(attrs={'step': '0.01'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock_item'].queryset = Stock.objects.all()