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
        # print response.content
        self.assertEqual(response.status_code, 200)
        
    def test_create_project_view(self): 
        c = Client()
        response = c.post('/create_project', {"project_name": "bob"}, follow = True)
        print response.redirect_chain
        cx = response.context
        print "type:"
        print type(cx)
        print dir(cx)
        print
        print "form:"
        form = cx.dicts[-1]["form"]
        print dir(form)

        # print "form errors?"
        # print form.has_error()

        print "polygon error messages:"
        print cx.dicts[-1]["form"].fields["polygon_field"].error_messages
        print "name error messages:"
        print cx.dicts[-1]["form"].fields["project_name"].error_messages

        
        self.assertEqual(response.status_code, 200)
    """   

        print
        response = c.post(reverse('create_project'), {'project_name': 'test', 'polygon_field': 'test_val'})
        print response.context
        print [f.errors for f in response.context[-1]["fields"]]
        self.assertEqual(response.status_code, 300)
        
        print response.content
        self.assertEqual(response.status_code, 200)
        num_projects =  Project.objects.all().count()
        print num_projects
        self.assertEqual(num_projects, 1)
        
      
    def test_forms(TestCase):
        form_data = { 'project_name': 'test', 'polygon_field': 'test_val', 'Aesthetics_pref': True, 'Transportation_pref': True }
        form = CreateProjectForm(data = form_data)
        self.assert
        
  
    def test_create_project_view_2(self): 
        c = Client()
        response = c.post('/create_project', { 'project_name': 'test', 'polygon_field': 'test_val', 'Aesthetics_pref': True, 'Transportation_pref': True }, follow = True)
        # print response.redirect_chain
        print response.content
        self.assertEqual(response.status_code, 200)
        num_projects =  Project.objects.all().count()
        print num_projects
        self.assertEqual(num_projects, 1)
     """
        