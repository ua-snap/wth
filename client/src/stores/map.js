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
  async function search(state) {
    
    let url = `http://localhost:5000?lat=${latLng.value[0]}&lng=${latLng.value[1]}&r=40000`
    console.log(url)
    let polys = await axios.get(url);
    searchResults.value = polys.data;
  }

  return { latLng, searchResults, isSearchActive, search };
});
