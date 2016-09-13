from django.core.management.base import BaseCommand, CommandError
from survey.models import FeedbackGoal

class Command(BaseCommand):
    help = 'Populate feedback goals'

    def handle(self, *args, **options):
        FeedbackGoal.objects.all().delete()

        aesthetics = FeedbackGoal()
        aesthetics.name = "Aesthetics"
        aesthetics.description = "Obtain aesthetic preferences: Selecting this option will cause relevant survey questions to be displayed"
        aesthetics.save()

        transportation = FeedbackGoal()
        transportation.name = "Transportation"
        transportation.description = "Obtain transportation preferences: Selecting this option will cause relevant survey questions to be displayed"
        transportation.save()