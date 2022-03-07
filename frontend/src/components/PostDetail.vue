<template>
  <v-container class="blue lighten-5">
    <v-row align="center" justify="center">
      <v-col cols="12" lg="10">
        <h1>{{ post.title }}</h1>
        <p>{{ post.modified_at }}, written by {{ post.owner }}</p>
      </v-col>
    </v-row>
    <v-row align="start" justify="center">
      <v-col cols="12" sm="8" lg="7">
        <v-card class="pa-2" tile>
          <p>{{ post.content }}</p>
          <div>
            <strong>Tags:</strong>
            <v-chip
              class="ma-2"
              outlined
              v-for="(tag, index) in post.tags"
              :key="index"
            >
              {{ tag }}
            </v-chip>
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
import axios from "axios";

export default {
  data: () => ({
    post: {},
  }),

  created() {
    console.log("created()...");
    this.fetchPostDetail();
  },

  methods: {
    fetchPostDetail() {
      console.log("fetchPostDetail()...");
      axios
        .get("/api/post/detail/2/")
        .then((res) => {
          console.log("POST DETAIL GET RES", res), (this.post = res.data);
        })
        .catch((err) => {
          console.log("POST DETAIL GET ERR.RESPONSE", err.response);
          alert(err.response.status + " " + err.response.statusText);
        });
    },
  },
};
</script>
