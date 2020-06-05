var mymap = L.map('mapid').setView([19.95, 80.32-1], 6);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);

var geojsonMarkerOptions = {
radius: 8,
fillColor: "#ff7800",
color: "#000",
weight: 1,
opacity: 1,
fillOpacity: 0.8
};

const ptl = (feature, latlng) => {
        return L.circleMarker(latlng, geojsonMarkerOptions);
    }

function oef(feature, layer) {
if (feature.properties && feature.properties.address) {
    layer.bindPopup(feature.properties.address);
}
if(feature.properties.government == 'G'){
layer.setStyle({
    fillColor: "red",

});
}else{
layer.setStyle({
    fillColor: "green",

});
}
    }
    // Examine the text in the response
var geojsonLayer = new L.GeoJSON.AJAX("/static/data/uma_pi.geojson",{
    onEachFeature: oef,
    pointToLayer: ptl
}).addTo(mymap);



    
var info = L.control({position: 'topright'});

info.onAdd = function (mymap) {
    var div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
    div.innerHTML = `<span class="greendot"></span><div class="dottext">Private</div><hr>
    <span class="reddot"></span><div class="dottext">Government</div>`;
    return div;
};
info.addTo(mymap);