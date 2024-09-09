from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator


# Create your views here.

def index(request):
    #return HttpResponse("<h1>Hello World</h1>")
    
    # ! get all data from listing database 
    listings = Listing.objects.all()
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
     # ! pass database records into listings context
    context ={'listings': paged_listings}
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    
    # ! get all data from listing database 
    listings = Listing.objects.all()
    # ! pass database records into listings context
    context ={'listing':listings}
    
    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html')