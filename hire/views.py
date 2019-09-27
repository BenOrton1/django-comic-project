from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import CommitionForm
from .models import Commition
from django.contrib import messages
from django.conf import settings
from django.forms.models import model_to_dict
from django.utils import timezone


def hire(request, pk=None):
    """A view that displays the hire page"""
    form = CommitionForm(request.POST)
    if request.method == "POST":
        form = CommitionForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            return redirect(make_estimate, form.pk)
    return render(request, "hire.html", {'form':form})
    

def make_estimate(request, pk):
    this_estimate = get_object_or_404(Commition, pk=pk)
    return render(request, "estimate.html", {'this_estimate':this_estimate})
            