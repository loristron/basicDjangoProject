from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.

def dynamic_lookup_view(request, my_id):
	obj = get_object_or_404(Product, id=my_id)

	context = {
		"object": obj
	}
	return render(request, "products/product_detail.html", context)

def product_create_view(request):
	# form = ProductForm(request.POST or None)
	# if form.is_valid():
	# 	form.save()
	# 	form = ProductForm()
	# context = {
	# 	"titulo": "Adicionar Produto",
	# 	"form": form
	# }
	formulario = RawProductForm()
	if request.method == 'POST':
		formulario = RawProductForm(request.POST)
		if formulario.is_valid():
			print(formulario.cleaned_data)
			Product.objects.create(**formulario.cleaned_data)
			formulario = RawProductForm()
		else:
			print(formulario.errors)

	context = {
		'titulo': 'Adicionar Produto',
		"form": formulario
	}
	return render(request, 'products/product_create.html', context)

def product_detail_view(request):
	obj = Product.objects.get(id=1)
	# context = {
	# 	'title': obj.title,
	# 	'description': obj.description,
	# 	'price': obj.price,
	# 	'summary': obj.summary,
	# 	'titulo': "produtos",
	# }
	context = {
	'object': obj
	}

	return render(request, "products/product_detail.html", context)

def product_delete_view(request, my_id):
	obj = get_object_or_404(Product, id=my_id)
	if request.method == 'POST':
		obj.delete()
		return redirect('../../')
	context = {
		"object": obj,
	}
	return render(request, 'products/product_delete.html', context)


def product_list_view(request):
	queryset = Product.objects.all()
	context = { 
	"object_list": queryset
	}
	return render(request, 'products/product_list.html', context)