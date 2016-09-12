from django import forms
from survey.models import FeedbackGoal

class CreateProjectForm(forms.Form):
	
	project_name = forms.CharField(max_length=100)

	def __init__(self,  *args, **kwargs):
		super(CreateProjectForm, self).__init__(*args, **kwargs)
		goals = FeedbackGoal.objects.all()
		for goal in goals:
			var_name = goal.name + "_pref"
			label = goal.description 
			self.fields[var_name] = forms.BooleanField(label = label, required=False)