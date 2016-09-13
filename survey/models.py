from __future__ import unicode_literals

from django.db import models

# Create your models here.

class FeedbackGoal(models.Model):
	name = models.CharField(max_length = 30)
	description = models.CharField(max_length = 200)

class Project(models.Model):
	name = models.CharField(max_length = 100)
	feedback_goals = models.ManyToManyField(FeedbackGoal)


    
