from django.shortcuts import render, redirect

from listings.models import Listing
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'key': 'value',
    }
    return render(request, 'pages/index.html', context)


def about(request):

    context = {
        'key': 'value',
    }
    return render(request, 'pages/about.html', context)
