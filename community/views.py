from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def messages(request):
    """Display the main web page."""
    template = loader.get_template('community/messages.html')
    context = {}
    return HttpResponse(template.render(context, request))

def my_offers(request):
    """Display the main web page."""
    template = loader.get_template('community/my_offers.html')
    context = {}
    return HttpResponse(template.render(context, request))
