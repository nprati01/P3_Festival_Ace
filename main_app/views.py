from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Festival, MyFestivalPlanning



# Create your views here.
def home(request):
    return render(request, 'home.html')

def festivals_index(request):
    festivals = Festival.objects.all()
    return render(request, 'festivals/index.html', {'festivals': festivals})

def festivals_detail(request, festival_id):
    festival = Festival.objects.get(id=festival_id)
    return render(request, 'festivals/detail.html', { 'festival': festival})

def add_festival(request, festival_id):
    festival = get_object_or_404(Festival, id=festival_id)
    print(festival)
    in_my_festivals = MyFestivalPlanning.objects.filter(user=request.user, festival=festival)
    print(in_my_festivals)
    if in_my_festivals.exists():
            return redirect('detail', festival_id=festival_id)
    add_to_my_festivals = MyFestivalPlanning(user=request.user, festival=festival)
    print(add_to_my_festivals)
    add_to_my_festivals.save()
    return redirect('detail', festival_id=festival_id)




def my_festivals_index(request):
    festivals = Festival.objects.filter(myfestivalplanning__user=request.user)
    return render(request, 'myfestivals/index.html', {'festivals': festivals})
