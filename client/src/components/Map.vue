<script setup>
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import proj4 from "proj4";
import p4l from "proj4leaflet";
import { watch, onMounted } from "vue";
import { useMapStore } from "@/stores/map";
import { storeToRefs } from "pinia";

var mapStore = useMapStore();
const { searchResults } = storeToRefs(mapStore);

// A few objects to share between methods
var layer; // the GeoJSON layer
var map;
var circle; // circle showing radius of search

var huc8Style = {
  opacity: 0.65,
  fillOpacity: 0.1,
  weight: 2,
};

var huc10Style = {
  opacity: 0.75,
  weight: 1,
  fillOpacity: 0.15,
  color: "#333333",
};

var huc12Style = {
  opacity: 0.9,
  weight: 1,
  color: "#449944",
  fillOpacity: 0.1,
};

// Trigger search.
function handleMapClick(event) {
  mapStore.latLng = [event.latlng.lat.toFixed(5), event.latlng.lng.toFixed(5)];
  if (circle) {
    map.removeLayer(circle);
  }
  circle = L.circle(mapStore.latLng, {
    radius: 40000,
    stroke: false,
    fillColor: "#888888",
    fillOpacity: 0.5,
  }).addTo(map);
  mapStore.search();
}

onMounted(() => {
  map = L.map("map", getBaseMapAndLayers());
  map.on("click", handleMapClick);
});

// When the searchResults are updated, refresh the map.
watch(searchResults, async () => {
  if (layer) {
    map.removeLayer(layer);
  }

  if (mapStore.searchResults) {
    layer = L.geoJSON(mapStore.searchResults, {
      style: function (feature) {
        switch (feature.properties.huclevel) {
          case 8:
            return huc8Style;
          case 10:
            return huc10Style;
          case 12:
            return huc12Style;
          default: // do nothing
        }
      },
    });
    layer.addTo(map);
  } else {
    // No results, clear the map...?
  }
});

function getBaseMapAndLayers() {
  var baseLayer = new L.tileLayer.wms(
    "https://gs.mapventure.org/geoserver/wms",
    {
      transparent: true,
      srs: "EPSG:3338",
      format: "image/png",
      version: "1.3.0",
      layers: [
        "atlas_mapproxy:alaska_osm_retina",
        "shadow_mask:iem_with_ak_aleutians_symmetric_difference",
      ],
    }
  );

  // Projection definition.
  var proj = new L.Proj.CRS(
    "EPSG:3338",
    "+proj=aea +lat_1=55 +lat_2=65 +lat_0=50 +lon_0=-154 +x_0=0 +y_0=0 +ellps=GRS80 +datum=NAD83 +units=m +no_defs",
    {
      resolutions: [4096, 2048, 1024, 512, 256, 128, 64],
    }
  );

  // Map base configuration
  var config = {
    zoom: 1,
    minZoom: 1,
    maxZoom: 6,
    center: [64.7, -152.5],
    scrollWheelZoom: false,
    crs: proj,
    continuousWorld: true,
    zoomControl: true,
    doubleClickZoom: false,
    attributionControl: false,
    layers: [baseLayer],
  };

  return config;
}
</script>

<template>
  <div id="map"></div>
</template>

<style scoped>
#map {
  height: 100vh;
  width: 100%;
}
</style>
