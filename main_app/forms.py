from django import forms
from django.forms import ModelForm
from .models import Task, Suitcase
from tempus_dominus.widgets import DatePicker

class TaskForm(ModelForm):
    due_date = forms.DateField(widget=DatePicker(
    options={
        'useCurrent': True,
        'collapse': False,
        'minDate': '2023-04-20',
        'maxDate': '2030-04-20',

        # Calendar and time widget formatting

        'date': 'fa fa-calendar',
        'up': 'fa fa-arrow-up',
        'down': 'fa fa-arrow-down',
        'today': 'fa fa-calendar-check-o',
        'clear': 'fa fa-delete',

    },
    attrs={
        'append': 'fa fa-calendar',
        'icon_toggle': True,

    }
)
    )
    class Meta:
        model = Task
        fields = ['title','due_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Buy Flights'})
        self.fields['due_date'].widget.attrs.update({'class': 'form-control'})



class SuitcaseForm(ModelForm):
    class Meta:
        model = Suitcase
        fields = ['item_name', 'quantity', 'status']



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Shirts'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control', 'placeholder': '3'})
        self.fields['status'].widget.attrs.update({'class': 'form-select'})
