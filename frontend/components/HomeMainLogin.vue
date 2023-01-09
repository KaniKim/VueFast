<template>
  <div>
    <v-container fluid style="max-width: 60%;">
      <v-flex md8 sm8>
        <v-card class="elevation-6">
          <v-toolbar color="primary" dark fluid>
            <v-toolbar-title>Login form</v-toolbar-title>
          </v-toolbar>
          <v-form id="check-login-form" @submit.prevent="onSubmit">
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
              :loading="loading"
              block
              color="primary"
              form="check-login-form"
              size="large"
              type="submit"
              variant="elevated"
            >
              Sign In
            </v-btn>
          </v-card-actions>
          <br>
        </v-card>
      </v-flex>
    </v-container>
  </div>
</template>

<script>
import store from "../store";

export default {
  name: "HomeLog",
  data: () => ({
    email: null,
    password: null,
  }),

  methods: {
    onSubmit() {
      store.dispatch("login", {
        email: this.email,
        password: this.password
      })
        .then(res => {
          this.$router.push({path: "/"});
        });
    },
    required(v) {
      return !!v || "Field is Required";
    }
  }
};
</script>
