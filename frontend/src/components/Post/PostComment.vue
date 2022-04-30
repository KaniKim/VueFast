<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col cols="8">
        <br />
        <v-card rounded="xs" class="mx-auto" height="100" border="1">
          <v-card-header>
            <v-content>
              <h1>TITLE - {{ items.title }}</h1>
            </v-content>
          </v-card-header>
          <v-card-subtitle>
            <v-content>
              <h2>AUTHOR - {{ items.author }}</h2>
            </v-content>
          </v-card-subtitle>
        </v-card>

        <br />
        <v-card height="400" border="1">
          <v-card-content>
            <v-content
              ><p>{{ items.content }}</p></v-content
            >
          </v-card-content>
        </v-card>

        <comment-manager user="user"> </comment-manager>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import AxiosInst from "@/plugins/axios";
import commentManager from "@/components/Post/CommentManager";

export default {
  data: () => ({
    items: "",
    user: null,
  }),
  components: { commentManager },
  created() {
    AxiosInst.get(`http://localhost:8000/post/${this.category}`)
      .then((res) => {
        this.items = res.data;
        this.user = res.data.author;
        console.log(res.data);
      })
      .catch((err) => {
        alert(err);
      });
  },
  computed: {
    category() {
      return this.$route.params.object;
    },
  },
};
</script>
