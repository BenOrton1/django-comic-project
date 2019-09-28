from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import CommitionForm
from .models import Commition
from django.contrib import messages
import os
import env
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
    estimate_string = """
{} has placed an order.\n with a deadline {}\nThey need {} character designes\n
they want {}\nThe setting is {}\nThey need {} pages\nDo they need a cover? {}
""".format(this_estimate.yourname, this_estimate.deadline, this_estimate.number_of_characters,
this_estimate.colour, this_estimate.setting,this_estimate.number_of_pages, this_estimate.cover)
    
    page_price=0
    total=0
    if this_estimate.cover == 'Yes':
        total += 40
    if this_estimate.colour == 'Line art only':
        page_price=10
    elif this_estimate.colour == 'Black and white':
        page_price=15
    else:
        page_price=25
    total_page_price = page_price*this_estimate.number_of_pages
    
    total += total_page_price
    
    send_mail(
    'New commition',
    estimate_string,
    this_estimate.email,
    [os.environ.get("EMAIL_ADDRESS")],
    fail_silently=False,)
    return render(request, "estimate.html", {'this_estimate':this_estimate, 'total':total})