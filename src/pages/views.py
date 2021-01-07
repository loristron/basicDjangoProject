from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def pInicial_view(request, *args, **kwargs):
	my_context = {
		"my_text": "About Us Page",
		"my_number": 123,
		"my_list": [123, 'abc', 456],
		"my_variable": True,
		"titulo": "Página Inicial",
	}
	return render(request, "home.html", my_context)

def contact_view(request, *ars, **kwars):
	my_context = {
		"titulo": "contato",
	}
	
	return render(request, "contact.html", my_context)

def profile_view(request, *ars, **kwars):
	my_context = {
		"titulo": "perfil",
	}
	return render(request, "profile.html", my_context)

def about_view(request, *ars, **kwars):
	my_context = {
		"titulo": "sobre nós",
	}

	return render(request, "about.html", my_context)

def feed_view(request, *ars, **kwars):
	my_context = {
		"titulo": "feed",
	}
	return render(request, "feed.html", my_context)
