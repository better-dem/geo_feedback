from django import forms
import os
import sys

api_key = os.environ["GOOGLE_MAPS_API_KEY"]


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
		sys.stderr.write("render_args:")
		sys.stderr.write(str(name) + 
			' ' + str(value) + ' ' + str(args))
		sys.stderr.write(" render_kwargs:")
		sys.stderr.write(str(kwargs))
		sys.stderr.flush()
		if value is None:
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
		sys.stderr.write("init_args:")
		sys.stderr.write(str(args))
		sys.stderr.write(" init_kwargs:")
		sys.stderr.write(str(kwargs))
		sys.stderr.flush()


class DrawPolygonField(forms.Field):
	def __init__(self,
		required= True,
		widget=DrawPolygonWidget,
		label=None,
		initial=None,
		help_text="",
		*args,
		**kwargs):
		super(DrawPolygonField, self).__init__(required=required,
			widget=widget,
			label=label,
			initial=initial,
			help_text=help_text,
			*args,
			**kwargs)

	# def clean(self, value):
	# 	super(DrawPolygonField, self).clean(value)

	def validate(self, value):
		super(DrawPolygonField, self).validate(value)
		if (value == None or value == "Test None"):
			raise ValidationError("None value encountered", code='invalid')
		else:
			return value

	def widget_attrs(self, widget):
		attrs = super(DrawPolygonField, self).widget_attrs(widget)
		return attrs

class SimpleTestWidgetForm(forms.Form):

	widget_a = forms.CharField(max_length=100)
	widget_b = forms.CharField(max_length=100)
	polygon_field = DrawPolygonField(label="Test Polygon Field")
	polygon_field_2 = DrawPolygonField(label="Test Polygon Field 2")

