  var map = L.map('map').setView([37.8, -96], 4);

    var access_token = 'pk.eyJ1IjoiYXJtaW5sZW8iLCJhIjoiY2lvZW9tb2NhMDBuNHYxbTNmY2c4MGM4diJ9.x1lF40VKozmCAUUewHvTvQ';

    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiYXJtaW5sZW8iLCJhIjoiY2lvZW9tb2NhMDBuNHYxbTNmY2c4MGM4diJ9.x1lF40VKozmCAUUewHvTvQ', {
      maxZoom: 18,
      attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
        '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="http://mapbox.com">Mapbox</a>',
      id: 'mapbox.streets'
    }).addTo(map);

    //mapbox.streets
    //mapbox.satellite
    //mapbox.light
    //mapbox.dark
    //mapbox.outdoors
    //mapbox.emerald

////////////////////////////// INFO /////////////////////////////////////////////

    // control that shows state info on hover
    var info = L.control();

    info.onAdd = function (map) {
      this._div = L.DomUtil.create('div', 'info');
      this.update();
      return this._div;
    };

    info.update = function (props) {
      this._div.innerHTML = '<h4><a href=""><font size="4" color="blue">Interactive Atlas:</a></h4></font>' +  
      (props ? '<b>' + props.name + '</b><br />' + props.density + ' Incidents'
            : '<b>' + 'Example of Geographic Patterns in Cancer Death Rates in 2011.');
    };

    info.addTo(map);

    map.attributionControl.addAttribution('');


////////////////////////////////////////////////////////////////////////////////

    // get color depending on population density value
    function getColor(d) {
      return d > 200 ? '#67001e' :
             d > 187.5 ? '#800026' :
             d > 176.2  ? '#BD0026' :
             d > 166.7  ? '#E31A1C' :
             d > 148.5  ? '#FC4E2A' :
             d > 125.6   ? '#FD8D3C' :
             // d > 70000000   ? '#FEB24C' :
             // d > 40000000   ? '#FED976' :
             // d > 1          ? '#FFEDA0' :
                              '#FFFFFF';
    }

    // Style each state based on the density 
    function style(feature) {
      return {
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7,
        fillColor: getColor(feature.properties.density)
      };
    }

    // Function : Highligh the state on mouseover
    function highlightFeature(e) {
      var layer = e.target;

      layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 1.0
      });

      if (!L.Browser.ie && !L.Browser.opera) {
        layer.bringToFront();
      }

      info.update(layer.feature.properties);
    }

    var geojson;

    // Function : Reset the Highlight on mouseout
    function resetHighlight(e) {
      geojson.resetStyle(e.target);
      info.update();
    }

    // Function : Zoom to state on click 
    function zoomToFeature(e) {
      map.fitBounds(e.target.getBounds());
    }

    // Function : For each state use the functions of highlight, reset and zoom
    function onEachFeature(feature, layer) {
      layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: zoomToFeature
      });
    }

    // Read the data, for each state use the above functions
    geojson = L.geoJson(statesData, {
      style: style,
      onEachFeature: onEachFeature
    }).addTo(map);

    
////////////////////////////// LEGEND //////////////////////////////////////////

    var legend = L.control({position: 'bottomright'});

    legend.onAdd = function (map) {

      var div = L.DomUtil.create('div', 'info legend'),
        grades = [ 125.6, 148.4, 166.6, 176.1, 187.4, 200.9],
        labels = [],
        from, to;

      // labels.push('<i style="background: #FFFFFF"></i> ' + 0);
      labels.push(
          '<a href=""><font size="2" color="black">Rate per 100,000 population</a><br>');
      
      for (var i = 0; i < grades.length; i++) {
        from = grades[i];
        to = grades[i + 1];

        if(i>0) 
          from = from+0.1;
        
        labels.push(
          '<i style="background:' + getColor(from + 1) + '"></i> ' +
           from + (to ? '&ndash;' + to : '+'));
      }

      div.innerHTML = labels.join('<br>');
      return div;
    };

    legend.addTo(map);

////////////////////////////////////////////////////////////////////////////////
