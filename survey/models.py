from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
    # has_aesthetic_feedback_goal = models.BooleanField( default = False )
    # has_transportation_feedback_goal = models.BooleanField( default = False )
    

class FeedbackGoal(models.Model):
	name = model.CharField(max_length=30)
	description = model.CharField(max_length=200)
	detail = model.TextField()

    
