<template>
  <div>
  <br />
  <br />
  <br />
  <v-row justify="center">
    <v-col cols="6">
      <div id="app">
        <v-table height="300px">
          <thead>
            <tr>
              <th class="text-left">Number</th>
              <th class="text-left">Category</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(item, i) in slides"
              :key="i"
              style="cursor: pointer"
              @click="cateProfile(item)"
            >
              <td>{{ i + 1 }}</td>
              <td>{{ item }}</td>
            </tr>
          </tbody>
        </v-table>
      </div>
    </v-col>
  </v-row>
    </div>
</template>

<script>
import AxiosInst from "@/plugins/axios";

export default {
  data: () => ({
    slides: null,
  }),

  created() {
    AxiosInst.get("http://localhost:8000/category")
      .then((res) => {
        this.slides = res.data;
      })
      .catch((err) => {
        alert(err);
      });
  },
  methods: {
    cateProfile(cate) {
      window.location.href = "http://localhost:8080/category/post/" + cate;
    },
  },
};
</script>
