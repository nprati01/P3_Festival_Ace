from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TaskForm, SuitcaseForm
from .models import Festival, MyFestival, Task, Suitcase




# Create your views here.
def home(request):
    return render(request, 'home.html')

def festivals_index(request):
    festivals = Festival.objects.all()
    return render(request, 'festivals/index.html', {'festivals': festivals})

def festivals_detail(request, festival_id):
    festival = Festival.objects.get(id=festival_id)
    return render(request, 'festivals/detail.html', { 'festival': festival})

@login_required
def my_festivals_index(request):
    festivals = Festival.objects.filter(myfestival__user=request.user)
    return render(request, 'myfestivals/index.html', {'festivals': festivals})
@login_required
def my_festivals_detail(request, festival_id):
    my_festival = MyFestival.objects.get(user=request.user)
    festival = Festival.objects.get(pk=festival_id)
    tasks = Task.objects.filter(festival_id=festival_id, my_festival=my_festival.id)
    suitcases = Suitcase.objects.filter(festival_id=festival_id, my_festival=my_festival.id)
    task_form = TaskForm()
    suitcase_form = SuitcaseForm()
    return render(request, 'myfestivals/detail.html', { 'festival':festival, 'my_festival': my_festival, 'tasks': tasks, 'task_form': task_form, 'suitcases': suitcases, 'suitcase_form': suitcase_form })

@login_required
def add_festival(request, festival_id):
    festival = Festival.objects.get(id=festival_id)
    my_festivals, created= MyFestival.objects.get_or_create(user = request.user)
    my_festivals.festivals.add(festival)
    return redirect('my_festivals_index')




@login_required
def remove_festival(request, festival_id):
    user = request.user
    festival = Festival.objects.get(id=festival_id)
    my_festivals = MyFestival.objects.get(user=user)
    my_festivals.festivals.remove(festival_id)
    return redirect('my_festivals_index')

@login_required
def create_task(request, festival_id, my_festival):
    my_fest = MyFestival.objects.get(pk=my_festival)
    print(my_fest)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.festival_id = festival_id
            task.my_festival = my_fest
            task.save()
            print(task.id)
            return redirect('my_festivals_detail', festival_id=festival_id)
    else:
        form = TaskForm()
    return render(request, 'main_app/create_task.html', {'form': form})


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['completed', 'title', 'due_date']
    success_url = '/'
    def get_success_url(self):
        festival_id=self.object.festival.id
        return reverse('my_festivals_detail', kwargs={'festival_id':festival_id})


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = '/'
    def get_success_url(self):
        festival_id=self.object.festival.id
        return reverse('my_festivals_detail', kwargs={'festival_id':festival_id})


@login_required
def create_suitcase(request, festival_id, my_festival):
    my_fest = MyFestival.objects.get(pk=my_festival)
    if request.method == 'POST':
        form = SuitcaseForm(request.POST)
        if form.is_valid():
            suitcase = form.save(commit=False)
            suitcase.festival_id = festival_id
            suitcase.my_festival = my_fest
            suitcase.save()
            return redirect('my_festivals_detail', festival_id=festival_id)
    else:
        form = SuitcaseForm()
    return render(request, 'myfestivals/create_suitcase.html', {'form': form})

class SuitcaseUpdate(LoginRequiredMixin, UpdateView):
    model = Suitcase
    fields = ['item_name', 'quantity', 'status']
    success_url = '/'
    def get_success_url(self):
        festival_id=self.object.festival.id
        return reverse('my_festivals_detail', kwargs={'festival_id':festival_id})

class SuitcaseDelete(LoginRequiredMixin, DeleteView):
    model = Suitcase
    success_url = '/'
    def get_success_url(self):
        festival_id=self.object.festival.id
        return reverse('my_festivals_detail', kwargs={'festival_id':festival_id})


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
