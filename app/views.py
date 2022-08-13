from math import prod
from unicodedata import category
from django.shortcuts import render
from app.models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models.functions import Lower
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import base64
from django.conf import settings
import os
# Create your views here.
def base(request):
    return render(request, "app/base.html")

@csrf_exempt
def home_page(request):
    category_search = request.POST.get("category_search")
    if category_search:
        categories = Category.objects.filter(
            name__icontains=category_search.lower().strip()
        )
    else:
        categories = Category.objects.all()    
    return render(request, "app/home.html", {"categories": categories, "category_search":category_search})


@csrf_exempt
def home_cats(request):
    category_search = request.POST.get("searched_cat")
    if category_search:
        categories = Category.objects.filter(
            name__icontains=category_search.lower().strip()
        ).values("id", "name", "featured_image")
    else:
        categories = Category.objects.all().values("id", "name", "featured_image")
    response = []
    for cat in categories:
        response.append(
            {
                "id": int(cat['id']),
                'name':cat['name'],
                "image": cat['featured_image'],
            }
        )
    return JsonResponse(response, safe=False)


def products(request, id=None):
    product_search = request.POST.get("product_search")
    if id and product_search:
        products = Product.objects.filter(
            name__icontains=product_search.lower().strip(), category_id=id
        )
    else:
        products = Product.objects.filter(category_id=id)
    return render(
        request, "app/Buttweldfittings.html", {"products": products, "cat_id": id, "product_search": product_search}
    )


import json
import base64

@csrf_exempt
def all_cats(request):
    product_search = request.POST.get("search_product")
    print("product_search========",product_search)
    if product_search:
        products = Product.objects.filter(
            name__icontains=product_search.lower().strip()
        ).values("id", "name", "featured_image", "category__name", "material"
        ,"mark_type", "standard", "size", "schedule")
    else:
        products = Product.objects.all().values("id", "name", "featured_image", "category__name", "material"
        ,"mark_type", "standard", "size", "schedule")
    response = []
    for prod in products:
        response.append(
            {
                "id": int(prod['id']),
                'name':prod['name'],
                "image": prod['featured_image'],
                "category": prod['category__name'],
                "material": prod['material'],
                "mark_type": prod['mark_type'],
                "size": prod['size'],
                "schedule": prod['schedule'],
                "standard": prod['standard'],
            }
        )
    print("=======",response)    
    return JsonResponse(response, safe=False)
