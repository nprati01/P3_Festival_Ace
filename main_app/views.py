from django.contrib.auth import login
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import CreateView
from .models import Festival, MyFestival, Task




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
    festival = get_object_or_404(my_festival.festivals.all(), id=festival_id)
    return render(request, 'myfestivals/detail.html', {'festival': festival})

def add_festival(request, festival_id):
    user = request.user
    festival = Festival.objects.get(id=festival_id)
    my_festivals, created = MyFestival.objects.get_or_create(user=user)
    my_festivals.festivals.add(festival)
    return redirect('my_festivals_index')

def remove_festival(request, festival_id):
    user = request.user
    festival = Festival.objects.get(id=festival_id)
    my_festivals = MyFestival.objects.get(user=user)
    my_festivals.festivals.remove(festival_id)
    return redirect('my_festivals_index')

class TaskCreate(CreateView):
    model = Task
    fields = ['title', 'completed', 'due_date']
    template_name ='main_app/task_create.html'

    def form_valid(self, form):
        festival_id = self.kwargs['festival_id']
        my_festival = get_object_or_404(MyFestival, user=self.request.user, id=festival_id)
        form.instance.my_festival = my_festival
        return super().form_valid(form)

    def get_success_url(self):
        festival_id = self.kwargs['festival_id']
        return reverse('my_festivals_detail', festival_id=festival_id)
