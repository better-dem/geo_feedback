from django import forms
from survey.models import FeedbackGoal

class CreateProjectForm(forms.Form):
    goals = ...
    for goal in goals:
    	var_name = goal.name+"_pref"
    	CreateProjectForm.__dict__[var_name] = forms.BooleanField(label=goal.name+"_pref"

    #aesthetic_pref = forms.BooleanField(label='Aesthetic Preference', required=False)
    #transportation_pref = forms.BooleanField(label='Transportation Preference', required=False)



