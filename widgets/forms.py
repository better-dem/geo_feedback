from django import forms
from django.core.exceptions import ValidationError
import os
import sys
import json
import traceback

api_key = os.environ["GOOGLE_MAPS_API_KEY"]


def validate_polygon(point_array):
	if point_array is None:
		raise ValidationError("Error parsing point array", code="invalid")
	for point in point_array:
		if(len(point) != 2):
			raise ValidationError("Point must compose of latitude and longitude",
				code="invalid")
		for p in point:
			if not type(p) is float:
				raise ValidationError("One of the coordinates is not float",
					code='invalid')

	if len(point_array) < 3:
		raise ValidationError("At least three points required for polygon",
			code='invalid')

def is_polygon(point_array_string):
	try:
		point_array = json.loads(point_array_string)
		validate_polygon(point_array)
		return True
	except:
		return False


class DrawPolygonWidget(forms.Widget):
	class Media:
		css = {
			'all' : ('css/poly_style.css',)
		}
		js = ("js/demo_poly_draw.js",
			"https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js",
			"https://maps.googleapis.com/maps/api/js?key={}".format(api_key),)
	def render(self, name, value, *args, **kwargs):
		div_id = 'poly_map_' + kwargs['attrs']['id']
		input_name = name
		input_id = kwargs['attrs']['id']
		if value is None or not is_polygon(value):
			value = 'null'

		render_html = """
	    <div class='map_widget' id="{}"></div>
	    <input type='text' name='{}' id='{}' value='' />

	    <script type="text/javascript">
		    google.maps.event.addDomListener(window, 'load', map_function('{}', '{}', {}));
		</script>
		"""
		render_html_with_id = render_html.format(div_id,
			input_name,
			input_id,
			div_id,
			input_id, value)
		return render_html_with_id

	def __init__(self, *args, **kwargs):
		super(DrawPolygonWidget, self).__init__(*args, **kwargs)


class DrawPolygonField(forms.Field):

	def __init__(self,
		required= True,
		widget=DrawPolygonWidget,
		label=None,
		initial=None,
		help_text="",
		validators=[validate_polygon],
		*args,
		**kwargs):
		super(DrawPolygonField, self).__init__(required=required,
			widget=widget,
			label=label,
			initial=initial,
			help_text=help_text,
			validators=validators,
			*args,
			**kwargs)

	def to_python(self, value):
		# Convert to expected python value (list of lists of latlngs)
		value = super(DrawPolygonField, self).to_python(value)
		try:
			json_array = json.loads(value)
		except:
			raise ValidationError("Unable to parse input: '{}'".format(value),
				code="invalid")
		return json_array

	def validate(self, value):
		super(DrawPolygonField, self).validate(value)

	def widget_attrs(self, widget):
		attrs = super(DrawPolygonField, self).widget_attrs(widget)
		return attrs

class SimpleTestWidgetForm(forms.Form):

	widget_a = forms.CharField(max_length=100)
	widget_b = forms.CharField(max_length=100)
	polygon_field = DrawPolygonField(label="Test Polygon Field")
	polygon_field_2 = DrawPolygonField(label="Test Polygon Field 2")

