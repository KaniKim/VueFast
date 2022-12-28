import {createVuetify} from "vuetify";
import * as components from "vuetify/components";

// eslint-disable-next-line no-undef
export default defineNuxtPlugin(nuxtApp => {
  const vuetify = createVuetify({
    components
  });

  nuxtApp.vueApp.use(vuetify);
});
