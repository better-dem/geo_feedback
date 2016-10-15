from __future__ import unicode_literals
from django.db import models

class FeedbackGoal(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)

class Project(models.Model):
    name = models.CharField(max_length = 100)
    feedback_goals = models.ManyToManyField(FeedbackGoal)
    polygon_coords = models.CharField(max_length = 500)

    def get_questions(self):
        ans = []
        for goal in self.feedback_goals.all():
            for question in Question.objects.filter(feedback_goal = goal):
                ans.append(question)
        return ans

class Question(models.Model):
    feedback_goal = models.ForeignKey('FeedbackGoal', on_delete=models.CASCADE)
    question_text = models.CharField(max_length = 200)

#Text Multi Choice Question
class TMCQ(Question):
    option1 = models.CharField(max_length = 100)
    option2 = models.CharField(max_length = 100)
    option3 = models.CharField(max_length = 100)
    option4 = models.CharField(max_length = 100)
    option5 = models.CharField(max_length = 100)

class ProjectResponse(models.Model):
    project = models.ForeignKey(
            'Project',
            on_delete = models.CASCADE,
        )
    creation_time = models.DateTimeField(auto_now_add=True)
    #ip_address = models.CharField(max_length = 30)

class QuestionResponse(models.Model):
    project_response = models.ForeignKey(
            'ProjectResponse',
            on_delete = models.CASCADE,
        )
    question = models.ForeignKey(
            'Question',
            on_delete = models.CASCADE,
        )

class TMCQResponse(QuestionResponse):
    option_index = models.IntegerField()
