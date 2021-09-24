<template>
  <v-app>
    <bar/>
    <drawer/>

    <v-main>
    </v-main>
  </v-app>
</template>

<script>
import Bar from './components/Bar.vue'
import Drawer from './components/Drawer.vue'

export default {
  name: 'App',
  components: {
    Bar,
    Drawer
  },
  data: () => ({
    //
  }),
};
</script>
