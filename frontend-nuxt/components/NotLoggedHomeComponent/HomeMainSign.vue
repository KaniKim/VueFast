<template>
  <v-container fluid style="max-width: 60%;">
    <v-flex md8 sm8>
      <v-card class="elevation-6">
        <v-toolbar color="primary" dark fluid>
          <v-toolbar-title>Signup form</v-toolbar-title>
        </v-toolbar>
        <v-form id="check-login-form">
          <v-card-text>
            <v-col align="center">
              <v-text-field
                v-model="email"
                :rules="[required(email)]"
                label="Login"
                name="login"
                style="max-width: 80%;"
                type="text"
              ></v-text-field>
              <v-text-field
                v-model="nickname"
                :rules="[required(nickname)]"
                label="Nickname"
                name="nickname"
                style="max-width: 80%;"
                type="text"
              ></v-text-field>
              <v-text-field
                v-model="password"
                :rules="[required(password)]"
                label="Password"
                name="password"
                style="max-width: 80%;"
                type="password"
              ></v-text-field>
            </v-col>
          </v-card-text>
        </v-form>
        <v-card-actions>
          <v-btn
            block
            color="primary"
            form="check-login-form"
            size="large"
            type="submit"
            variant="elevated"
            @click.prevent="onSubmit"
          >
            Sign In
          </v-btn>
        </v-card-actions>
        <br>
      </v-card>
    </v-flex>
  </v-container>
</template>
<script>
import Axios from "@/api/default";
import router from "@/routes";

export default {
  data: () => ({
    email: null,
    password: null,
    nickname: null,
    isError: false,
    errMsg: "",
  }),

  methods: {
    onSubmit() {
      if (!this.email || !this.nickname || !this.password) {
        this.isError = true;
        this.errMsg = "Please input all form";
        return;
      }
      Axios.post("/user/", {
        email: this.email,
        password: this.password,
        name: this.nickname,
      })
        .then(res => {
          console.log(res);
          router.push("/login");
        })
        .catch(err => {
          console.log(err);
        });
    },
    required(v) {
      return !!v || "Field is Required";
    }
  }
};
</script>
