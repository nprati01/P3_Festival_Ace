from django.shortcuts import render
from .models import Festival

myfestivals = [
    {'name': 'EDC', 'location': 'Las Vegas', 'date':'May 20th 2023', 'duration': 'four days'}
]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def festivals_index(request):
    festivals = Festival.objects.all()
    return render(request, 'festivals_index.html', {'festivals': festivals})


def my_festivals_index(request):
    return render(request, 'myfestivals/index.html', {'myfestivals': myfestivals})
