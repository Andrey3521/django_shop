from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *

def landing(request):
    name = "Andrey"
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(form)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'landing/landing.html', locals())

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)

    return render(request, 'landing/home.html', locals())