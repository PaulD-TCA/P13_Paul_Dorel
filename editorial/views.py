from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def home(request):
    """Display the main web page."""
    template = loader.get_template('editorial/home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def project_presentation(request):
    """Display the project presentation page."""
    template = loader.get_template('editorial/project_presentation.html')
    context = {}
    return HttpResponse(template.render(context, request))
