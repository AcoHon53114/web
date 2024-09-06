from django.shortcuts import render
from .models import Realtor
# Create your views here.

def about(request):
    # ! get all data from listing database 
    realtors = Realtor.objects.all()
    # ! pass database records into listings context
    context ={'realtors':realtors}
    
    return render(request, 'pages/about.html', context)
