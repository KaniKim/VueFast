<template>
  <v-main>
    <v-container>
      <h1 align="center">Login Page</h1>
    </v-container>
    <br />
    <br />
    <v-container>
    <v-row justify="center" align="center"
      ><v-col md="4" lg="4" cols="4">
        <v-form ref="form" v-model="valid" lazy-validation>
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
            <v-btn
              :disabled="!valid"
              color="success"
              class="mr-4"
              @click="login"
            >
              Login
            </v-btn>
          </v-row>
        </v-form>
      </v-col>
    </v-row>
    </v-container>
  </v-main>

</template>

<script>
export default {
  data: () => ({
    valid: true,
    email: "",
    password: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
  }),
  watch: {
    group() {
      this.drawer = false;
    },
  },

  methods: {
    login() {
      const UserData = {
        username: this.email,
        password: this.password,
      };
      this.$store.dispatch("LOGIN", UserData).then(() => {
        this.$router.push("/my");
      });
    },
  },
};
</script>
