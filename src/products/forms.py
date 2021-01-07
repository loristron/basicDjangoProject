from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
		"title",
		"price",
		"description",
		"summary",
		"featured",
		]

class RawProductForm(forms.Form):
	title = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Título do Produto"}))
	price = forms.DecimalField(initial=0.00)
	description = forms.CharField(
						required=False,
						widget=forms.Textarea(
								attrs={
									"placeholder":'Insira a descrição',
									"class": 'description_form_class',
									"id": 'description_form_id',
									"rows": 12,
									"cols": 60,
								}	
							)
						)
	summary = forms.BooleanField(required=False)