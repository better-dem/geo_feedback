// (code inspired by the following, license copied below): http://codepen.io/jhawes/post/creating-a-real-estate-polygon-tool
// Copyright (c) 2015 by Jeremy Hawes (http://codepen.io/jhawes/pen/ujdgK)
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

function getPolygonCoords() {
	var len = my_polygon.getPath().getLength();
	var htmlStr = "";
	for (var i = 0; i < len; i++) {
		htmlStr += "new google.maps.LatLng(" + 
			my_polygon.getPath().getAt(i).toUrlValue(5) + 
			"), ";
	}
	console.log(htmlStr);
	//document.getElementById('info').innerHtml = htmlStr;
}
var numAvailable = 5;
var numClicked = 0;
var colorArray = ['green', 'blue', 'yellow', 'gray', 'magenta'];
var markerArray = []

function addMarker(e, polygon, map) {
	console.log("Here");
	if (numClicked >= numAvailable) {
		console.log("Exceeds number of allowed markers");
		return;
	}
	if (google.maps.geometry.poly.containsLocation(e.latLng, polygon)) {
		var markerColor = colorArray[numClicked];
		var marker = new google.maps.Marker({
			position: e.latLng,
			map: map,
			draggable: true,
			icon: {
				path: google.maps.SymbolPath.CIRCLE,
				fillColor: markerColor,
				fillOpacity: 0.2,
				strokeColor: 'white',
				strokeWeight: 0.5,
				scale: 10 
			}
		});
		markerArray.push(marker);
		numClicked++;
	}
}

function initMap() {
	// Initialize map to certain coordinates
	var my_center = new google.maps.LatLng(37.38, -122.0);
	var map_options = {
		zoom : 12,
		center: my_center,
        mapTypeId: 'terrain'
    };
	var map = new google.maps.Map(document.getElementById("poly-mark-map"), map_options); 
	// Initilalize polygon drawing

	var orig_coords = [
		new google.maps.LatLng(37.41626,-122.03691), 
		new google.maps.LatLng(37.37835,-122.0527), 
		new google.maps.LatLng(37.39867,-121.97889)
	];

  	// Styling and controls
  	my_polygon = new google.maps.Polygon({
  		paths : orig_coords,
  		draggable : false,
  		strokeColor : '#FF0000',
  		strokeOpacity : 0.8,
  		strokeWeight : 2,
  		fillOpacity: 0.0,
  		map: map
  	});
  	google.maps.event.addListener(my_polygon, 'click', function(e) {
		addMarker(e, my_polygon, map);
	});
}

