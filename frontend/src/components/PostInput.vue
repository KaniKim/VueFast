<template>
  <v-container fluid>
    <v-row align="center" justify="center">
      <v-col cols="8" lg="8">
        <v-card tile>
          <br />
          <br />
          <v-row align="center" justify="center">
            <v-col cols="8" lg="8">
              <v-textarea
                label="title"
                no-resize
                rows="1"
                value="title"
              ></v-textarea>
            </v-col>
            <v-col cols="8" lg="8">
              <v-textarea
                clearable
                clear-icon="mdi-close-circle"
                label="content"
                value="This is clearable text."
              ></v-textarea>
            </v-col>
            <v-col cols="8" lg="8">
              <v-textarea
                label="tags"
                no-resize
                rows="1"
                value="title"
              ></v-textarea>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>