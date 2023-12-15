from django.forms import forms, ModelForm,  CharField, TextInput, Textarea, BooleanField, CheckboxInput
from django import forms
from product.models import Variant, Product, ProductVariantPrice


class VariantForm(ModelForm):
    class Meta:
        model = Variant
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'active'})
        }




class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductVariantPrice
        fields = '__all__'
        widgets = {
            'product_variant_one': forms.TextInput(attrs={'class': 'form-control'}),
            'product_variant_two': forms.TextInput(attrs={'class': 'form-control'}),
            'product_variant_three': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.TextInput(attrs={'class': 'form-control'}),
            'product': forms.TextInput(attrs={'class': 'form-control'}),
        }

    #images= forms.ClearableFileInput(attrs={'class': 'form-control'})
    #variants = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))