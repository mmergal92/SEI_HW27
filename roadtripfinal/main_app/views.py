from django.db.models import query
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Roadtrips

# Create your views here.

class roadtripListView(View):
    def get(self, request):
        queryset = Roadtrips.objects.all()
        context = {
        'objects': queryset
        }
        return render(request, 'roadtrips/roadtrip_list.html', context)

def home(request):
    return render(request, 'home.html')

def roadtrip_detail(request, id):
    object = get_object_or_404(Roadtrips, id=id)
    context = {
        'object': object
    }
    return render(request, 'roadtrips/roadtrip_detail.html', context)

def about(request):
    return render(request, 'about.html')

class roadtrip_create(CreateView):
    model = Roadtrips
    fields = '__all__'

def roadtrip_update(request):
    return render(request, 'roadtrips/roadtrip_update.html')

def roadtrip_delete(request, id):
    object = get_object_or_404(Roadtrips, id=id)
    if request.method == "POST":
        object.delet()
        return redirect('../../')
    context = {
        "object": object
    }
    return render(request, 'roadtrips/roadtrip_delete.html', context)