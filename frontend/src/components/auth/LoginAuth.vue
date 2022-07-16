<template>
<v-main>
    <v-form>
        <v-container>
        <v-row
        align="center"
        justify="center">
            <v-col
            cols="12"
            sm="6"
            >
            <v-text-field
                v-model="id"
                :rules="rules"
                counter="25"
                hint="This field is for id"
                label="ID"
            ></v-text-field>
            </v-col>
        </v-row>
        <v-row
        align="center"
        justify="center">
            <v-col
            cols="12"
            sm="6"
            >
            <v-text-field
                v-model="password"
                :rules="rules"
                counter="25"
                hint="This field is for id"
                label="Password"
            ></v-text-field>
            </v-col>
            </v-row>
            <v-row
        align="center"
        justify="center">
            <v-col
            cols="6"
            sm="6"
            >
        <v-btn
      variant="outlined"
      color="primary"
      block
    >
        Check Login
    </v-btn>
    </v-col>
            </v-row>
        </v-container>
    </v-form>
</v-main>
</template>

<script>
export default {
  data() {
    return {
      id: "ID Field",
      password: "PASSWORD Field",
      description: "Please Be Careful",
      rules: [v => v.length <= 25 || "Max 25 characters"]
    };
  }
};
</script>