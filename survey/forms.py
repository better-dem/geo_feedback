from django import forms
from survey.models import FeedbackGoal, TMCQ, Question
from widgets.forms import DrawPolygonField

class CreateProjectForm(forms.Form):
	
	project_name = forms.CharField(max_length=100)
	polygon_field = DrawPolygonField(label="Region of interest")
	
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

				try:
					tmcq = question.tmcq

					label = question.question_text
					var_name = "field_" + str(question.id)

					choices = []

					if not tmcq.option1 == "":
						choices.append(("1", tmcq.option1))
					if not tmcq.option2 == "":
						choices.append(("2", tmcq.option2))
					if not tmcq.option3 == "":
						choices.append(("3", tmcq.option3))
					if not tmcq.option4 == "":
						choices.append(("4", tmcq.option4))
					if not tmcq.option5 == "":
						choices.append(("5", tmcq.option5))
					
					self.fields[var_name] = forms.ChoiceField(label = label, required=False, choices = choices )
				except:
					raise Exception("Invalid question type. Only TMCQ supported")
