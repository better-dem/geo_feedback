from django.test import TestCase, TransactionTestCase
from survey.models import Project, FeedbackGoal, ProjectResponse, Question, QuestionResponse, TMCQResponse
from django.test import Client
from .forms import CreateProjectForm, ProjectResponseForm
from django.core.urlresolvers import reverse

class SurveyAppUnitTests(TestCase):
    def setup(self):
        pass
        
    def test_if_db_is_empty(self):
        num_projects =  Project.objects.all().count()
        self.assertEqual(num_projects, 0)

    def test_404(self):
        c = Client()
        response = c.post('/login/', {'username': 'john', 'password': 'smith'})
        self.assertEqual(response.status_code, 404)
        
    def test_get_index(self):
        c = Client()
        response = c.get('')
        self.assertEqual(response.status_code, 200)
        
    def test_create_project_form(self):
        """
        Test that form validation works
        """

        form = CreateProjectForm({'project_name':"bob"})
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error("polygon_field"))
        self.assertFalse(form.has_error("project_name"))

        form = CreateProjectForm({'project_name':"bob", "polygon_field": "1,2,3"})
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error("polygon_field"))
        self.assertFalse(form.has_error("project_name"))

        content = {'project_name':"bob", "polygon_field": "[[1.0,2.0],[3.0,4.0],[5.0,6.0]]"}
        form = CreateProjectForm(content)
        self.assertTrue(form.is_valid())
        self.assertFalse(form.has_error("polygon_field"))

        
        goals = FeedbackGoal.objects.all()
        for goal in goals:
            var_name = goal.name + "_pref"
            content[var_name] = True
        form = CreateProjectForm(content)
        self.assertTrue(form.is_valid())

    def test_create_project_view(self): 
        """
        Test that the view actually creates the desired database objects
        """

        c = Client()
        response = c.post(reverse('create_project'), {"project_name": "bob"}, follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.redirect_chain), 0)
        form = response.context["form"]
        self.assertEqual(len(form.errors.as_data()), 1)
        self.assertTrue(form.has_error("polygon_field"))

        # create a project with no feedback goals
        content = {'project_name':"bob", "polygon_field": "[[1.0,2.0],[3.0,4.0],[5.0,6.0]]"}
        response = c.post(reverse('create_project'), content, follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.redirect_chain), 0)
        self.assertEqual(response.templates[0].name, "survey/thanks.html")
        num_projects = Project.objects.all().count()
        self.assertEqual(num_projects, 1)
        project_id=1
        project = Project.objects.get(pk=project_id)
        self.assertEqual(project.feedback_goals.count(), 0)

        # create a project with all feedback goals
        goals = FeedbackGoal.objects.all()
        for goal in goals:
            var_name = goal.name + "_pref"
            content[var_name] = True
        response = c.post(reverse('create_project'), content, follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.redirect_chain), 0)
        self.assertEqual(response.templates[0].name, "survey/thanks.html")
        num_projects = Project.objects.all().count()
        self.assertEqual(num_projects, 2)
        project_id=2
        project = Project.objects.get(pk=project_id)
        self.assertEqual(project.feedback_goals.count(), len(goals))



        
