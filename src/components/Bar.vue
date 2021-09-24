<template>
  <v-app-bar app>
    <v-btn text @click="toHome">
      <v-icon>mdi-home</v-icon>
      <span>MMS</span>
    </v-btn>
    <v-spacer/>
    <span>本週收益: {{benifit}}</span>
  </v-app-bar>
</template>
<script>

export default {
  data(){
    return{
      benifit: 0
    }
  },
  methods: {
    toHome(){
      if(this.$router.history.current.path !== '/'){
        this.$router.push('/')
      }
    }
  }
}
</script>
<style scoped>

</style>