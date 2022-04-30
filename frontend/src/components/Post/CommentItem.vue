<template>
  <div>
    <div v-show="state === false">
      <v-row justify="center">
        <v-col cols="10">
          <v-card>
            <v-card-header-text>{{ data.body }}</v-card-header-text>
            <v-card-subtitle>
              temp <span>&bull;</span
              ><v-btn @click="state = 'editing'">edit</v-btn
              ><v-btn @click="stateOn = 'true'">add</v-btn></v-card-subtitle
            ><v-card v-for="(nex, i) in data.next" :key="i">
              <v-card-header-text>{{ nex }}</v-card-header-text>
              <v-card-subtitle>
                <v-icon @click="state = 'editing'"
                  >Save</v-icon
                ></v-card-subtitle
              >
            </v-card>
          </v-card>
        </v-col>
      </v-row>
    </div>
    <v-dialog v-model="state" width="500">
      <v-card class="overflow-x-hidden overflow-y-hidden">
        <v-row justify="center">
          <v-col cols="12">
            <v-text-field
              v-model="data.body"
              rows="1"
              placeholder="Update comment"
            >
            </v-text-field>
            <v-row>
              <v-col cols="4">
                <v-btn @click="saveEdit">Update</v-btn>
              </v-col>
              <v-col cols="4">
                <v-btn @click="resetEdit">Cancel</v-btn>
              </v-col>
              <v-col cols="4">
                <v-btn @click="deleteComment">Delete</v-btn>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-card>
    </v-dialog>
    <v-dialog v-model="stateOn" width="500">
      <v-card class="overflow-x-hidden overflow-y-hidden">
        <v-row justify="center">
          <v-col cols="12">
            <v-text-field
              v-model="data.bodyNe"
              rows="1"
              placeholder="Comment on comment"
            >
            </v-text-field>
            <v-row>
              <v-col cols="12">
                <v-btn @click="commentoComment">Save</v-btn>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import AxiosInst from "@/plugins/axios";

export default {
  props: {
    user: {
      required: true,
      type: Object,
    },
    id: {
      required: true,
      type: Object,
    },
    comment: {
      required: true,
      type: Array,
    },
  },
  data: function () {
    return {
      state: false,
      stateOn: false,
      data: {
        body: this.comment.content,
        bodNe: "",
        next: [],
        id: this.comment.id,
      },
    };
  },
  computed: {
    editable() {
      console.log(this.comment);
      return this.user.id === this.comment.id;
    },
    category() {
      return this.$route.params.object;
    },
  },
  methods: {
    resetEdit() {
      this.state = false;
      this.data.body = this.comment.body;
    },
    saveEdit() {
      this.state = false;

      this.$emit("comment-updated", {
        id: this.comment.id,
        body: this.data.body,
      });
    },
    deleteComment() {
      this.$emit("comment-deleted", {
        id: this.comment.id,
      });
    },
    commentoComment() {
      this.stateOn = false;
      this.data.next.push(this.data.bodyNe);
      AxiosInst.post(`http://localhost:8000/comment/next/${this.data.id}`, {
        content: this.data.bodyNe,
      })
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          alert(err);
        });
    },
  },
};
</script>
