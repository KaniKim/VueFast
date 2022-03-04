<template>
  <v-container class="blue lighten-5">
    <v-row align="center" justify="center">
      <v-col cols="12" lg="10">
        <h1>Post title here</h1>
        <p>2020-07-10, written by kanikim</p>
      </v-col>
    </v-row>
    <v-row align="start" justify="center">
      <v-col cols="12" sm="8" lg="7">
        <v-card class="pa-2" tile>
          <p>I study Vue.js and FastAPI</p>
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
          <div>
            <strong>Tags:</strong>
            <v-chip class="ma-2" outlined>python </v-chip>
            <v-chip class="ma-2" outlined>fastapi+ </v-chip>
          </div>
        </v-card>
      </v-col>
      <v-col cols="12" sm="4" lg="3">
        <v-card class="pa-2" tile>
          One of three columns <br />
          Hello
        </v-card>
        <br />
        <v-card class="pa-2" tile> One of three columns </v-card>
        <br />
        <v-card class="pa-2" tile>
          <h2>Tag Cloud</h2>
          <v-chip class="ma-2" color="green" text-color="white">
            <v-avatar left class="green darken-4"> 1 </v-avatar>python
          </v-chip>
          <v-chip class="ma-2" color="green" text-color="white">
            <v-avatar left class="green darken-4"> 3 </v-avatar>django
          </v-chip>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
</script>
