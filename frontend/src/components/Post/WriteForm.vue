<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col cols="12" md="6">
        <br />
        <v-content>
          <h1>Write Your Content</h1>
        </v-content>
        <br />
        <v-textarea
          filled
          auto-grow
          label="Title"
          rows="1"
          v-model="title"
          row-height="20"
        ></v-textarea>
        <v-textarea
          solo
          auto-grow
          name="input-7-4"
          v-model="content"
          label="Content"
        ></v-textarea>
        <v-text-field
          label="tags"
          v-model="currentInput"
          @keypress.enter="saveChip"
        >
        </v-text-field>
        <v-chip-group>
          <v-chip v-for="(chip, i) of chips" :key="chip.label"
            >{{ chip }}
            <v-icon @click="deleteChip(i)" small right>
              mdi-close-circle-outline
            </v-icon>
          </v-chip>
        </v-chip-group>
        <br />
        <br />
        <v-btn depressed elevation="2" @click="writePost">Submit</v-btn>
        <v-col cols="4">
          <v-select
            v-model="category_name"
            :items="category"
            filled
            label="Choose Category"
          ></v-select>
        </v-col>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import AxiosInst from "@/plugins/axios";
import Cookies from "js-cookie";

export default {
  data: function () {
    return {
      category_name: null,
      category: [
        { name: "life", value: "life" },
        { name: "work", value: "work" },
        { name: "balance", value: "balance" },
      ],
      chips: [],
      currentInput: "",
      title: "",
      content: "",
    };
  },
  methods: {
    saveChip() {
      const { chips, currentInput, set } = this;
      ((set && chips.indexOf(currentInput) === -1) || !set) &&
        this.currentInput !== "" &&
        chips.push(currentInput);
      this.currentInput = "";
    },
    deleteChip(index) {
      this.chips.splice(index, 1);
    },
    writePost() {
      const token = Cookies.get("access_token");
      AxiosInst.defaults.headers.common["Authorization"] = token;
      AxiosInst.post("http://localhost:8000/post", {
        title: this.title,
        content: this.content,
        tags: this.chips,
        category: this.category_name,
      })
        .then((res) => {
          console.log(res);
          alert(res.data.msg);
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>
