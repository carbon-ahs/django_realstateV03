from django.core import paginator
from django.shortcuts import render
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger 

from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings,
        'key': 'value',
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):

    context = {
        'key': 'value',
    }
    return render(request, 'listings/listing.html', context)

def search(request):

    context = {
        'key': 'value',
    }
    return render(request, 'listings/search.html', context)
