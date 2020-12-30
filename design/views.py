from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from .models import Design

from .forms import DesignForm, NameForm

# Create your views here.
def design_list(request):
    """Display the design list."""
    current_user = request.user.id
    designs = Design.objects.all().exclude(user_id=current_user)
    template = loader.get_template('design/design_list.html')
    context = {'designs': designs,}
    return HttpResponse(template.render(context, request))

def upload_design(request):
    """Upload files for a design."""
    if request.method == 'POST':
        current_user = request.user.id
        form = DesignForm(request.POST, request.FILES)
        if form.is_valid():
            data_design_name = form.cleaned_data['design_name']
            data_design_image = form.cleaned_data['design_image']
            data_plan_2d = form.cleaned_data['plan_2d']
            data_plan_3d = form.cleaned_data['plan_3d']
            data_assembly_instruction = form.cleaned_data['assembly_instruction']
            data_description = form.cleaned_data['description']
            data_category = form.cleaned_data['category']
            user = User.objects.get(id=request.user.id)
            data_to_save = Design(design_name=data_design_name,
                design_image=data_design_image, plan_2d=data_plan_2d,
                plan_3d=data_plan_3d, assembly_instruction=data_assembly_instruction,
                description=data_description, category=data_category, user_id=user)
            data_to_save.save()
            return redirect('home')
    else:
        form = DesignForm()
    return render(request, 'design/upload_design.html', {'form':form})

def my_design(request):
    """Display the user designs."""
    current_user = request.user.id
    designs = Design.objects.filter(user_id=current_user)
    template = loader.get_template('design/my_design.html')
    context = {'designs': designs,}
    return HttpResponse(template.render(context, request))

def results(request):
    """Display the results of a query."""
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            search_string = form.cleaned_data['your_name']
            words = list(search_string.split(" "))
            for word in words:
                designs = Design.objects.filter(design_name__icontains=search_string)
            template = loader.get_template('design/design_list.html')
            context = {
            'designs':designs,
            }
            return HttpResponse(template.render(context, request))
    template = loader.get_template('design/design_list.html')
    context = {}
    return HttpResponse(template.render(context, request))
