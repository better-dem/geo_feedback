from django import forms
import os
import sys



class DrawPolygonWidget(forms.Widget):
	class Media:
		css = {
			'all' : ('css/poly_style.css',)
		}
		js = ('js/demo_poly_draw.js', "https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js")
	def render(self, *args, **kwargs):
		api_key = os.environ["GOOGLE_MAPS_API_KEY"]
		div_id = 'poly_map'
		input_name = 'poly_coords'
		render_html = """
	    <div class='map_widget' id="{}"></div>
	    <input type='text' name='{}' value='' />
	    <script type="text/javascript">
    		var cb_poly_draw_{} = create_map_function('{}', '{}');
    	</script>
    	<script async defer
      		src="https://maps.googleapis.com/maps/api/js?key={}&callback=cb_poly_draw_{}">
    	</script>
		"""
		render_html_with_id = render_html.format(div_id,
			input_name,
			div_id,
			div_id,
			input_name,
			api_key,
			div_id)
		return render_html_with_id


class DrawPolygonField(forms.Field):
	def __init__(self,
		required= True,
		widget=DrawPolygonWidget(),
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

class SimpleTestWidgetForm(forms.Form):

	widget_name = forms.CharField(max_length=100)
	widget = DrawPolygonWidget()
	sys.stderr.write(str(widget.media))
	sys.stderr.write("here")
	sys.stderr.flush()
	polygon_field = DrawPolygonField(label="Test Polygon Field");

