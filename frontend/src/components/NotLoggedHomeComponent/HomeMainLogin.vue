<template>
  <v-row>
    <v-col align-self="center">
      <v-card class="overflow-hidden" color="primary">
        <v-toolbar flat>
          <v-toolbar-title>Login</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-text-field label="Email"></v-text-field>
          <v-text-field clearable label="Password"></v-text-field>
          <br>
          <v-btn type="submit" variant="elevated">LogIn</v-btn>
        </v-toolbar>
      </v-card>
    </v-col>
  </v-row>
</template>
