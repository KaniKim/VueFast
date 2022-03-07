<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col cols="12" lg="10" outlined>
        <v-table theme="dark">
          <v-col cols="3">
            <v-toolbar-title>My CRUD</v-toolbar-title>
          </v-col>
          <v-col cols="3"> </v-col>
          <v-col cols="3">
            <v-btn color="primary" class="mb-2" @click="dialog = true">
              New Item
            </v-btn>
          </v-col>
          <tbody>
            <v-row align="start">
              <v-col cols="12" lg="12" outlined>
                <tr v-for="post in posts" :key="post">
                  <v-row aling="center" justify="center">
                    <v-col cols="4">{{ post.title }}</v-col>
                    <v-col cols="3">{{ post.description }}</v-col>
                    <v-col cols="3">{{ post.content }}</v-col>
                    <v-col cols="1" @click="editItem(post)">
                      <v-icon small class="mr-2"> mdi-pencil </v-icon>
                    </v-col>
                    <v-col cols="1">
                      <v-icon small @click="deleteItem(post)">
                        mdi-delete
                      </v-icon>
                    </v-col>
                  </v-row>
                </tr>
              </v-col>
            </v-row>
          </tbody>
          <template v-slot:no-data>
            <v-btn color="primary" @click="fetchPostList">Reset</v-btn>
          </template>
        </v-table>
      </v-col>
    </v-row>
    <v-container>
      <v-dialog v-model="dialog" persistent>
        <v-card width="500px">
          <v-card-title>
            <span class="text-h5">CRUD Sample</span>
          </v-card-title>
          <v-card-text>
            <v-row align="center" justify="center">
              <v-col cols="3">
                <v-text-field
                  v-model="editedItem.name"
                  label="Dessert name"
                ></v-text-field>
              </v-col>
              <v-col cols="3">
                <v-text-field
                  v-model="editedItem.calories"
                  label="Calories"
                  >{{
                }}</v-text-field>
              </v-col>
              <v-col cols="3">
                <v-text-field
                  v-model="editedItem.fat"
                  label="Fat (g)"
                ></v-text-field>
              </v-col>
              <v-col cols="3">
                <v-text-field
                  v-model="editedItem.carbs"
                  label="Carbs (g)"
                ></v-text-field>
              </v-col>
              <v-col cols="3">
                <v-text-field
                  v-model="editedItem.protein"
                  label="Protein (g)"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="close"> Cancel </v-btn>
            <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
    <v-dialog v-model="dialog">
      <v-card width="500px">
        <v-card-title>
          <span class="text-h5">CRUD Sample</span>
        </v-card-title>

        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  v-model="editedItem.name"
                  label="Dessert name"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  v-model="editedItem.calories"
                  label="Calories"
                  >{{
                }}</v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  v-model="editedItem.fat"
                  label="Fat (g)"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  v-model="editedItem.carbs"
                  label="Carbs (g)"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  v-model="editedItem.protein"
                  label="Protein (g)"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="close"> Cancel </v-btn>
          <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogDelete">
      <v-card width="500px">
        <v-card-title class="text-h5"
          >Are you sure you want to delete this item?</v-card-title
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="deleteItemConfirm"
            >OK</v-btn
          >
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>
<script>
import axios from "axios";

export default {
  name: "PostList",
  data: () => ({
    dialog: false,
    dialogDelete: false,
    headers: [
      { text: "제 목", value: "title" },
      { text: "요 약", value: "description" },
      { text: "수정일", value: "modified_at" },
      { text: "작성자", value: "owner" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    posts: [
      {
        name: 1,
        calories: "Django 3.0 Released",
        fat: "2019년 12월 장고 3.0 버전 발표함",
        carbs: "2020-07-13",
        protein: "shkim",
      },
      {
        name: "Ice cream sandwich",
        calories: 237,
        fat: 9.0,
        carbs: 37,
        protein: 4.3,
      },
      {
        name: "Eclair",
        calories: 262,
        fat: 16.0,
        carbs: 23,
        protein: 6.0,
      },
    ],
    editedIndex: -1,
    editedItem: {
      name: "",
      calories: 0,
      fat: 0,
      carbs: 0,
      protein: 0,
    },
    defaultItem: {
      name: "",
      calories: 0,
      fat: 0,
      carbs: 0,
      protein: 0,
    },
  }),

  created() {
    this.fetchPostList();
  },

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },

  methods: {
    fetchPostList() {
      console.log("fetchPostList()...");

      axios
        .get("/api/post/list/")
        .then((res) => {
          console.log("POST GET RES", res);
          this.posts = res.data;
        })
        .catch((err) => {
          console.log("POST GET ERR.RESPONSE", err.response);
          alert(err.response.status + " " + err.response.statusText);
        });
    },
    editItem(item) {
      this.editedIndex = this.posts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.posts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      this.posts.splice(this.editedIndex, 1);
      this.closeDelete();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.posts[this.editedIndex], this.editedItem);
      } else {
        this.posts.push(this.editedItem);
      }
      this.close();
    },
  },
};
</script>
