from django.shortcuts import render
from django.http import HttpResponse
from .forms import SimpleTestWidgetForm
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

def demo_poly_mark(request):
    return render(request,
                  'widgets/demo_poly_mark.html',
                  {'api_key' : os.environ["GOOGLE_MAPS_API_KEY"]})

def simple_test_widget(request):
	if request.method == 'POST':
		form = SimpleTestWidgetForm(request.POST)
		if form.is_valid():
			return HttpResponse("Form is Valid")
		else:
			return render(request, 'widgets/simple_test_widget.html',
				{'form': form})
	else:
		form = SimpleTestWidgetForm()
		return render(request, 'widgets/simple_test_widget.html',
			{'form': form})
