from django.shortcuts import get_object_or_404

def make_an_estimate(request):
    this_estimate = request.session.get('this_estimate',{})
    number_of_pages = {}
    return{'number_of_pages':number_of_pages,'this_estimate':this_estimate}