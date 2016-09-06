from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    return HttpResponse("Hello, world. You're at the survey index.")


def demo_map(request):
    # View code here...
    return render(request,
                  'survey/demo_map.html',
                  {'api_key' : os.environ["GOOGLE_MAPS_API_KEY"]})
