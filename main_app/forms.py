from django.forms import ModelForm
from .models import Task, Suitcase

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed', 'due_date']
class SuitcaseForm(ModelForm):
    class Meta:
        model = Suitcase
        fields = ['item_name', 'quantity', 'status']
