<template>
  <v-main>
    <v-content>
      <h1 align="center">Register Page</h1>
    </v-content>
    <br />
    <br />
    <v-row justify="center" align="center"
      ><v-col md="4" lg="4" cols="4">
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-text-field
            v-model="name"
            :counter="10"
            :rules="nameRules"
            label="Name"
            required
          ></v-text-field>

          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
          ></v-text-field>

          <v-text-field
            type="password"
            v-model="password"
            label="Password"
            required
          ></v-text-field>
          <v-row justify="center">
            <v-checkbox
              v-model="checkbox"
              :rules="[(v) => !!v || 'You must agree to continue!']"
              label="Do you agree?"
              required
            ></v-checkbox>

            <v-btn
              :disabled="!valid"
              color="success"
              class="mr-4"
              @click="register"
            >
              Register
            </v-btn>
          </v-row>
        </v-form>
      </v-col>
    </v-row>
  </v-main>
</template>

<script>
import AxiosInst from "@/plugins/axios";

export default {
  data: () => ({
    valid: true,
    name: "",
    nameRules: [
      (v) => !!v || "Name is required",
      (v) => (v && v.length <= 10) || "Name must be less than 10 characters",
    ],
    email: "",
    password: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
  }),

  methods: {
    register() {
      AxiosInst.post("http://localhost:8000/user", {
        name: this.name,
        email: this.email,
        password: this.password,
      })
        .then((res) => {
          if (res.status === 200) {
            this.$router.replace("/");
          }
        })
        .catch(() => {
          alert("Email is already existed");
        });
    },
  },
};
</script>
