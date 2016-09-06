from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^demo_map$', views.demo_map, name='demo_map')
]
