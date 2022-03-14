<template>
  <v-container fluid>
    <v-row align="center" justify="center">
      <v-col cols="8" lg="8">
        <v-card tile>
          <br />
          <br />
          <v-row align="center" justify="center">
            <v-col cols="8" lg="8">
              <v-text-field label="title" no-resize rows="1"></v-text-field>
            </v-col>
            <v-col cols="8" lg="8">
              <v-textarea
                clearable
                clear-icon="mdi-close-circle"
                label="content"
              ></v-textarea>
            </v-col>
            <v-col cols="8" lg="8">
              <v-text-field v-model="currentInput" @keypress.enter="saveChip">
              </v-text-field>
              <v-chip-group>
                <v-chip v-for="(chip, i) of chips" :key="chip.label"
                  >{{ chip }}
                  <v-icon @click="deleteChip(i)" small right>
                    mdi-close-circle-outline
                  </v-icon>
                </v-chip>
              </v-chip-group>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
export default {
  props: {
    set: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      chips: [],
      currentInput: "",
    };
  },
  methods: {
    saveChip() {
      const { chips, currentInput, set } = this;
      ((set && chips.indexOf(currentInput) === -1) || !set) &&
        chips.push(currentInput);
      this.currentInput = "";
    },
    deleteChip(index) {
      this.chips.splice(index, 1);
    },
  },
};
</script>
