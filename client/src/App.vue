<script>
import Map from "@/components/Map.vue";
import SearchResults from "@/components/SearchResults.vue";

export default {
  components: { Map, SearchResults },
};
</script>

<template>
  <div class="columns">
    <div class="column is-one-third">
      <SearchResults />
    </div>
    <div class="column">
      <Map />
    </div>
  </div>
</template>

<style scoped></style>
