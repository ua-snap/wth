import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

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
  async function search() {
    let polys = await axios.get("http://localhost:5000");
    searchResults.value = polys.data;
  }

  return { latLng, searchResults, isSearchActive, search };
});
