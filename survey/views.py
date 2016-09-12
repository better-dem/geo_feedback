from django.shortcuts import render
from django.http import HttpResponse
from survey.models import Project
from .forms import CreateProjectForm
import os

def index(request):
    return HttpResponse("Hello, world. You're at the survey index.")

def new_project(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)        
        if form.is_valid():
        	project = Project()
        	project.has_aesthetic_feedback_goal = form.cleaned_data["aesthetic_pref"]
        	project.has_transportation_feedback_goal = form.cleaned_data["transportation_pref"]
        	project.save()
        	return HttpResponse("Form is valid")
        else:
            return render(request, 'survey/create_project.html', {'form': form })
    else:
        form = CreateProjectForm()
        return render(request, 'survey/create_project.html', {'form': form })

def show_projects(request):
	projects = Project.objects.all()
	ids = [str(p.id) for p in projects]
	return HttpResponse(','.join(ids))

def demo_map(request):
    # View code here...
    return render(request,
                  'survey/demo_map.html',
                  {'api_key' : os.environ["GOOGLE_MAPS_API_KEY"]})
