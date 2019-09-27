from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import CommitionForm
from .models import Commition
from django.contrib import messages
from django.conf import settings
from django.forms.models import model_to_dict
from django.utils import timezone


def hire(request, pk=None):
    """A view that displays the hire page"""
    initial={'number_of_pages': request.session.get('number_of_pages', None)}
    commition = get_object_or_404(Commition, pk=pk) if pk else None
    form = CommitionForm(request.POST or None, initial=initial)
    if request.method == "POST":
        form = CommitionForm(request.POST, request.FILES, instance=commition)
        if form.is_valid():
            form = form.save()
            return redirect(make_estimate, commition.pk)
    return render(request, "hire.html", {'form':form})
    

def make_estimate(request, pk):
    this_estimate = get_object_or_404(Commition, pk=pk)
    return render(request, "estimate.html", {'this_estimate':this_estimate})
            