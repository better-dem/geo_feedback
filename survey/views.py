from django.shortcuts import render
from django.http import HttpResponse
from survey.models import Project, FeedbackGoal
from .forms import CreateProjectForm, ProjectResponseForm
import os

def index(request):
    return HttpResponse("Hello, world. You're at the survey index.")

def new_project(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)        
        if form.is_valid():
            project = Project()
            project.name = form.cleaned_data["project_name"]
            project.polygon_coords = form.cleaned_data["polygon_field"]
            project.save()

            goals = FeedbackGoal.objects.all()
            for goal in goals:
                var_name = goal.name + "_pref"

                if form.cleaned_data[var_name]:
                    project.feedback_goals.add(goal)
            
            
            return HttpResponse("Form is valid")
        else:
            return render(request, 'survey/create_project.html', {'form': form })
    else:
        form = CreateProjectForm()
        return render(request, 'survey/create_project.html', {'form': form })

def project_response(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.method == 'POST':
        form = ProjectResponseForm(project, request.POST )        
        if form.is_valid():
            pass      
            
            return HttpResponse("Form is valid")
        else:
            return render(request, 'survey/create_project.html', {'form': form })
    else:
        form = ProjectResponseForm(project)
        return render(request, 'survey/create_project.html', {'form': form })


def show_projects(request):
    projects = Project.objects.all()
    ids = [str(p.id) for p in projects]
    return HttpResponse(','.join(ids))

def show_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    ans = project.name+ ":"
    ans += project.polygon_coords + "    "
    for goal in project.feedback_goals.all():
        ans+=(goal.name + "  ")
    return HttpResponse(ans)

