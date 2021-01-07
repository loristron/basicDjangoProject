from django.urls import path

#importação da home no arquivo views, no APP pages 
from pages.views import pInicial_view, contact_view, profile_view, about_view, feed_view
from products.views import ( 
		product_detail_view, 
		product_create_view, 
		dynamic_lookup_view, 
		product_delete_view, 
		product_list_view,
	)
urlpatterns = [ 
    path('', product_list_view, name="list-products"),
  	path('<int:my_id>/', dynamic_lookup_view, name="product-detail"),
    path('<int:my_id>/delete/', product_delete_view, name="product-delete"),
    path('create/', product_create_view, name='create'),

    ]