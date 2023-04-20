from django.contrib.auth import login
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import CreateView
from .forms import TaskForm
from .models import Festival, MyFestival, Task, Suitecase




# Create your views here.
def home(request):
    return render(request, 'home.html')

def festivals_index(request):
    festivals = Festival.objects.all()
    return render(request, 'festivals/index.html', {'festivals': festivals})

def festivals_detail(request, festival_id):
    festival = Festival.objects.get(id=festival_id)
    return render(request, 'festivals/detail.html', { 'festival': festival})

def my_festivals_index(request):
    festivals = Festival.objects.filter(myfestival__user=request.user)
    return render(request, 'myfestivals/index.html', {'festivals': festivals})

def my_festivals_detail(request, festival_id):
    my_festival = MyFestival.objects.get(user=request.user)
    festival = Festival.objects.get(pk=festival_id)
    print(festival)
    return render(request, 'myfestivals/detail.html', {'festival': festival, 'my_festival': my_festival})

def add_festival(request, festival_id):
    user = request.user
    festival = Festival.objects.get(id=festival_id)
    my_festivals = MyFestival.objects.get(user=user)
    my_festivals.festivals.add(festival)
    return redirect('my_festivals_index')

def remove_festival(request, festival_id):
    user = request.user
    festival = Festival.objects.get(id=festival_id)
    my_festivals = MyFestival.objects.get(user=user)
    my_festivals.festivals.remove(festival_id)
    return redirect('my_festivals_index')



def create_task(request, festival_id, my_festival):
    festival = Festival.objects.get(id=festival_id)
    print(festival)
    my_fest = MyFestival.objects.get(pk=my_festival)
    print(my_fest)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.festival_id = festival_id
            task.my_festival = my_fest
            task.save()
            return redirect('my_festivals_detail', festival_id=festival_id)
    else:
        form = TaskForm()
    return render(request, 'main_app/create_task.html', {'form': form})
