<script>
import Map from "../components/Map.vue";

export default {
  components: { Map },
};

</script>

<template>
  <div>
    <section class="section">
      <div class="container">
        <h1 class="title is-1">Where the HUC?</h1>
        <h2 class="subtitle is-3">🎁 A geospatial gift project by SNAP</h2>
        <div class="content is-size-4">
          <p>
            Pick a point on the map and find hydrological units (HUC-8, HUC-10
            and HUC-12), protected areas and other polygons of interest. Adjust
            the search radius to find nearby places.
          </p>
        </div>
      </div>
    </section>
    
    <Map />  

    <footer>
      Thanks to all our collaborators who help us bring science to people who
      can use it.
    </footer>
  </div>
</template>
