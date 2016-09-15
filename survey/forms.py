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

class ProjectResponseForm(forms.Form):

	def __init__(self, project, *args, **kwargs):
		super(ProjectResponseForm, self).__init__(*args, **kwargs)

		ans = project.name+ ":"
		for goal in project.feedback_goals.all():
			for question in Question.objects.filter(feedback_goal = goal):
				label = question.question_text
				var_name = "field_" + str(question.id)

				choices = []

				if not question.option1 == "":
					choices.append(("1", question.option1))
				if not question.option2 == "":
					choices.append(("2", question.option2))
				if not question.option3 == "":
					choices.append(("3", question.option3))
				if not question.option4 == "":
					choices.append(("4", question.option4))
				if not question.option5 == "":
					choices.append(("5", question.option5))
				
				self.fields[var_name] = forms.ChoiceField(label = label, required=False, choices = choices )
