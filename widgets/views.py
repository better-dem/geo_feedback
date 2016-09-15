from django.shortcuts import render
from django.http import HttpResponse
# from .forms import CreateProjectForm
import os

# Create your views here.
def demo_map(request):
    return render(request,
                  'widgets/demo_map.html',
                  {'api_key' : os.environ["GOOGLE_MAPS_API_KEY"]})

def demo_poly_draw(request):
    return render(request,
                  'widgets/demo_poly_draw.html',
                  {'api_key' : os.environ["GOOGLE_MAPS_API_KEY"]})
