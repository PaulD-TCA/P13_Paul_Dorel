from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage

# Create your views here.
def design_list(request):
    """Display the main web page."""
    template = loader.get_template('design/design_list.html')
    context = {}
    return HttpResponse(template.render(context, request))

def propose_design(request):
    """Upload files for a design."""
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    template = loader.get_template('design/propose_design.html')
    context = {}
    return HttpResponse(template.render(context, request))



def my_design(request):
    """Display the main web page."""
    template = loader.get_template('design/my_design.html')
    context = {}
    return HttpResponse(template.render(context, request))
