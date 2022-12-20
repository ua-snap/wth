<script setup>
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import proj4 from "proj4";
import p4l from "proj4leaflet";
import { onMounted } from "vue";
import { useMapStore } from "@/stores/map";

var mapStore = useMapStore();

// Trigger search.
function handleMapClick(event) {
  mapStore.latLng = [event.latlng.lat.toFixed(5), event.latlng.lng.toFixed(5)];
  console.log("mapstore.latLng", mapStore.latLng)
  mapStore.search();
  let layer;
  if (mapStore.searchResults) {
    layer = L.geoJSON(mapStore.searchResults);
    L.geoJSON(mapStore.searchResults).addTo(map);
  } else {
    //whatev
  }
}

onMounted(() => {
  map = L.map("map", getBaseMapAndLayers());
  map.on("click", handleMapClick);
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
