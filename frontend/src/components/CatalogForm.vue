<template>
  <Form @submit="onSubmit" :validation-schema="schema">
    <Field v-slot="{ field, errors }" v-model="name" name="name">
      <div class="p-col-12">
        <div class="p-inputgroup">
          <InputText
            placeholder="Name"
            :class="{ 'p-valid': errors.length > 0 }"
            v-bind="field"
          />
        </div>
        <small class="p-error" v-if="errors.length"> Name is invalid </small>
      </div>
    </Field>
  </Form>
</template>
<script>
import * as yup from "yup";
import axios from "axios";
import { APIURL } from "@/constants";

const schema = yup.object().sahpe({
  name: yup.string().required(),
  description: yup.string().required(),
  imageURL: yup.string().url().required(),
});

export default {
  name: "BookingForm",
  data() {
    return {
      name: "",
      description: "",
      imageURL: "",
      schema,
    };
  },
  methods: {
    async onsubmit(value) {
      const { name, description, imageURL } = value;
      await axios.post(`${APIURL}/catalog`, {
        name,
        description,
        imageURL,
      });
      this.$emit("catalog-form-close");
    },
  },
};
</script>