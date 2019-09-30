from django import forms
from django.forms import ModelForm, Textarea,extras
from .models import Commition


class CommitionForm(forms.ModelForm):
    deadline = forms.DateField(widget=extras.SelectDateWidget)
    class Meta:
        model = Commition
        fields = (
            '__all__'
        )
        labels = {
            'yourname': ('Name'),
            'setting': ('Whats the basic plot and setting?'),
            'cover': ('Do you need cover art?'),
            'colour': ('What type of art do you need'),
            'number_of_characters': ('How many character designes do you need?'),
            'number_of_pages': ('how many pages is this ptoject'),
            'deadline': ('When is your deadline?'),
            'email': ('Whats your email address?'),
        }
        widgets = {
            'setting': Textarea(attrs={'cols': 80, 'rows': 10}),
        }