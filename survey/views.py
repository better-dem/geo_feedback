from django.shortcuts import render
from django.http import HttpResponse
from survey.models import Project, FeedbackGoal
from .forms import CreateProjectForm
import os

def index(request):
    return HttpResponse("Hello, world. You're at the survey index.")

def new_project(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)        
        if form.is_valid():
        	project = Project()
        	project.name = form.cleaned_data["project_name"]
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

def show_projects(request):
	projects = Project.objects.all()
	ids = [str(p.id) for p in projects]
	return HttpResponse(','.join(ids))

def show_project(request, project_id):
	project = Project.objects.get(pk=project_id)
	ans = project.name+ ":"
	for goal in project.feedback_goals.all():
		ans+=(goal.name + "  ")
	return HttpResponse(ans)

def demo_map(request):
    # View code here...
    return render(request,
                  'survey/demo_map.html',
                  {'api_key' : os.environ["GOOGLE_MAPS_API_KEY"]})
