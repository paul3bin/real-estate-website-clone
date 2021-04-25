from django.shortcuts import render
from django.http import HttpResponse

from listings.choices import price_choices, bedroom_choices, state_choices
from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    return render(request, 'pages/index.html', context={
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    })


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtor = Realtor.objects.filter(is_mvp=True)
    return render(request, 'pages/about.html', context={
        'realtors': realtors,
        'mvp': mvp_realtor
    })
