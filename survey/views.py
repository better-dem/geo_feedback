from django.shortcuts import render
from django.http import HttpResponse
from survey.models import Project, FeedbackGoal, ProjectResponse, Question, QuestionResponse, TMCQResponse
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
            return render(request, 'survey/generic_form.html', {'form': form, 'action_path' : request.path})
    else:
        form = CreateProjectForm()
        return render(request, 'survey/generic_form.html', {'form': form, 'action_path' : request.path })

def project_response(request, project_id):
    project = Project.objects.get(pk=project_id)
    title = project.name

    if request.method == 'POST':
        form = ProjectResponseForm(project, request.POST )        
        if form.is_valid():
            pr = ProjectResponse()
            pr.project = project
            pr.save()
            
            for key in form.cleaned_data:
                if "field_prf_" in key:
                    question_id = key.lstrip("field_prf_")
                    question = Question.objects.get(pk=question_id)
                    try:
                        tmcq = question.tmcq
                    except:
                        raise Exception("Invalid question type. Only TMCQ supported")
                    else:
                        qr = TMCQResponse()
                        qr.project_response = pr
                        qr.question = question
                        qr.option_index = int(form.cleaned_data[key])
                        qr.save()
                        
            return HttpResponse("Form is valid")
        else:
            return render(request, 'survey/generic_form.html', {'form': form, 'action_path' : request.path, 'form_title' : title})
    else:
        form = ProjectResponseForm(project)
        return render(request, 'survey/generic_form.html', {'form': form, 'action_path' : request.path, 'form_title' : title})


def show_projects(request):
    projects = Project.objects.all()
    ids = [str(p.id) for p in projects]
    return HttpResponse(','.join(ids))

def show_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    
    num_responses = ProjectResponse.objects.filter(project=project).count()
    
    ans = project.name+ ":"
    ans += "Number of responses: " + str(num_responses) + "    "
    ans += project.polygon_coords + "    "
    for goal in project.feedback_goals.all():
        ans+=(goal.name + "  ")
    return HttpResponse(ans)

