from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^demo_map$', views.demo_map, name = 'demo_map'),
    url(r'^demo_poly_draw$', views.demo_poly_draw, name = 'demo_poly_draw'),
    url(r'^demo_poly_mark$', views.demo_poly_mark, name = 'demo_poly_mark')
]
