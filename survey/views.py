from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the survey index.")


def demo_map(request):
    # View code here...
    return render(request, 'survey/demo_map.html')
