<template>
  <div>
    <div>
      <v-row justify="center">
        <v-col cols="10">
          <br />
          <div class="d-flex">
            <v-text-field
              class="mx-2 rounded-lg"
              v-model="data.body"
              rows="1"
              placeholder="Add a comment"
            >
            </v-text-field>
            <v-chip class="short" large @click="saveComment">
              <v-icon large right>
                mdi-checkbox-multiple-marked-circle-outline
              </v-icon></v-chip
            >
          </div>
        </v-col>
      </v-row>
    </div>
    <div class="overflow-y-auto overflow-x-hidden" style="height: 120px">
      <br />
      <comment
        v-for="comment in comments"
        :key="comment._id"
        :user="comment.author"
        :comment="comment"
        :id="comment._id"
        @comment-updated="updateComment($event)"
        @comment-deleted="deleteComment($event)"
      >
      </comment>
    </div>
  </div>
</template>
<style>
.short {
  width: 60px;
  height: 60px !important;
}
</style>
<script>
import comment from "./CommentItem";
import AxiosInst from "@/plugins/axios";
export default {
  components: {
    comment,
  },
  props: {
    user: {
      required: true,
      type: Object,
    },
  },
  data: () => ({
    data: {
      body: "",
    },
    comments: [],
  }),
  created() {
    AxiosInst.get(`http://localhost:8000/comment/${this.category}`)
      .then((res) => {
        console.log(res.data);
        this.comments = res.data;
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
  methods: {
    updateComment($event) {
      let index = this.comments.findIndex((element) => {
        return element.id === $event.id;
      });

      this.comments[index].body = $event.body;
    },
    deleteComment($event) {
      let index = this.comments.findIndex((element) => {
        return element.id === $event.id;
      });

      this.comments.splice(index, 1);
    },
    saveComment() {
      let newComment = {
        content: this.data.body,
      };

      AxiosInst.post(`http://localhost:8000/comment/${this.category}`, {
        content: this.data.body,
      })
        .then((res) => {
          console.log(res.data);
          this.comments.push(newComment);
        })
        .catch((err) => {
          alert(err);
        });

      this.data.body = "";
    },
  },
};
</script>
