from django.db.models import query
from django.shortcuts import render, get_object_or_404, redirect
from .models import Roadtrips

# Create your views here.
def home(request):
    return render(request, 'home.html')

def roadtrip(request):
    queryset = Roadtrips.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'roadtrips/roadtrip_list.html', context)

def roadtrip_detail(request, id):
    object = Roadtrips.objects.get(id = id)
    context = {
        'object_list': object
    }
    return render(request, 'roadtrips/roadtrip_list.html', context)

def about(request):
    return render(request, 'about.html')

def roadtrip_create(request):
    return render(request, 'roadtrips/roadtrip_create.html')

def roadtrip_update(request):
    return render(request, 'roadtrips/roadtrip_update.html')

def roadtrip_delete(request):
    return render(request, 'roadtrips/roadtrip_delete.html')