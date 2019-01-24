from django.shortcuts import render
from django.template.response import TemplateResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_POST
from catalogue.forms import ProductEditForm, ProductSearchForm
from catalogue.models import Product


def product_list(request):
	products = Product.objects.order_by('name')

	form = ProductSearchForm(request.GET)
	products = form.filter_products(products)

	paginator = Paginator(products, 5)
	#page = request.GET.get('page', 1)
	params = request.GET.copy()
	if 'page' in params:
		page = params['page']
		del params['page']
	else:
		page = 1

	search_params = params.urlencode()

	try:
		products = paginator.page(page)
	except (EmptyPage, PageNotAnInteger):
		products = paginator.page(1)

	return TemplateResponse(request, 'catalogue/product_list.html',
													{
													'products': products,
													'form': form,
													'search_params': search_params
													})

def product_detail(request, product_id):
	try:
		product = Product.objects.get(id=product_id)
	except Product.DoseNotExist:
		raise Http404

	return TemplateResponse(request, 'catalogue/product_detail.html',
													{'product': product})

def product_edit(request, product_id):
	try:
		product = Product.objects.get(id=product_id)
	except Product.DoseNotExist:
		raise Http404

	if request.method == 'POST':
		form = ProductEditForm(request.POST, instance=product)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('product_detail', args=(product.id)))


	return TemplateResponse(request, 'catalogue/product_edit.html',
													{'product': product})


def product_delete(request, product_id):
	try:
		product = Product.objects.get(id=product_id)
	except Product.DoseNotExist:
		raise Http404

	if request.method == 'POST':
		product.delete()
		return HttpResponseRedirect(reverse('product_list'))

	return TemplateResponse(request, 'catalogue/product_delete.html',
														{'product': product})

	

# Create your views here.
