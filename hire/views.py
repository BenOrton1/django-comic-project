from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import CommitionForm
from .models import Commition
from django.contrib import messages
from django.conf import settings
from django.forms.models import model_to_dict
from django.utils import timezone
from django.core.mail import send_mail

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
    estimateString =str(this_estimate)
    Total=0
    if this_estimate.cover == 'Yes':
        Total += 40
    if this_estimate.colour == 'Line art only':
        PagePrice=10
    elif this_estimate.colour == 'Black and white':
        PagePrice=15
    else:
        PagePrice=25
    TotalPagePrice = PagePrice*this_estimate.number_of_pages
    
    Total += TotalPagePrice
    
    print(PagePrice)
    send_mail(
    'Subject here',
    estimateString,
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,)
    return render(request, "estimate.html", {'this_estimate':this_estimate, 'Total':Total})
            