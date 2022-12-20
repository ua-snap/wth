import { ref, computed } from "vue";
import { defineStore } from "pinia";
import polys from "../assets/t2.json";

export const useMapStore = defineStore("map", () => {
  // the ref() function is core Vue3 reactive model stuff.
  // It wraps the value (here, `undefined` with a proxy so it's
  // reactive).
  // These declarations are equivalent to setting "state".
  const latLng = ref(undefined);
  const searchResults = ref(undefined);

  const isSearchActive = computed(() => {
    return latLng !== undefined;
  });

  // An action.
  function search() {
    searchResults.value = polys;
  }

  return { latLng, searchResults, isSearchActive, search };
});
