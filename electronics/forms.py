from django import forms
from .models import Product

class ProductForm(forms.ModelForm): #pascal case P and F are capital in class name
    class Meta:
        model=Product
        fields=['id','name','price','description']

