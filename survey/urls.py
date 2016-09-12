from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^create_project$', views.new_project, name = 'create_project'),
    url(r'^show_projects$', views.show_projects, name = 'show_projects'),
    url(r'^demo_map$', views.demo_map, name = 'demo_map')
]
