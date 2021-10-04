from django.shortcuts import render

from .models import Listing

def index(request):
    listings = Listing.objects.all()

    context = {
        'listings': listings,
        'key': 'value',
    }
    return render(request, 'listings/listings.html', context)

def listing(request):

    context = {
        'key': 'value',
    }
    return render(request, 'listings/listing.html', context)

def search(request):

    context = {
        'key': 'value',
    }
    return render(request, 'listings/search.html', context)
