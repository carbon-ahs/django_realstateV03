from django.shortcuts import render, redirect

from listings.models import Listing
from realtors.models import Realtor
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'key': 'value',
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.all()
    mvp_realtors = Realtor.objects.filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
        'key': 'value',
    }
    return render(request, 'pages/about.html', context)
