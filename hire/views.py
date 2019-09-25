from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import CommitionForm
from django.contrib import messages
from django.conf import settings
from django.forms.models import model_to_dict
from django.utils import timezone


def hire(request):
    """A view that displays the hire page"""
    initial={'number_of_pages': request.session.get('number_of_pages', None)}
    form = CommitionForm(request.POST or None, initial=initial)
    if request.method == 'POST':
        if form.is_valid():
            request.session['number_of_pages'] = form.cleaned_data['number_of_pages']
            return redirect(reverse('make_estimate'))
    return render(request, "hire.html", {'form':form})
    

def make_estimate(request):
    number_of_pages = request.session['number_of_pages']
    return render(request, "estimate.html",{"number_of_pages":number_of_pages})
            