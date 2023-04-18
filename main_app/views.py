from django.shortcuts import render
from .models import Festival, MyFestivalPlanning



# Create your views here.
def home(request):
    return render(request, 'home.html')

def festivals_index(request):
    festivals = Festival.objects.all()
    return render(request, 'festivals_index.html', {'festivals': festivals})


def my_festivals_index(request):
    festivals = Festival.objects.filter(myfestivalplanning__user=request.user)
    return render(request, 'myfestivals/index.html', {'festivals': festivals})
