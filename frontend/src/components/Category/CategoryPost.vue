<template>
  <div>
  <br />
  <br />
  <br />
  <v-row justify="center">
    <v-col cols="12" sm="6">
      <v-table dark>
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-left">Num</th>
              <th class="text-left">Title</th>
              <th class="text-left">Author</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(item, i) in items"
              :key="i"
              @click="catePost(this.objet[i])"
            >
              <td>{{ i + 1 }}</td>
              <td>{{ item.title }}</td>
              <td>{{ item.author }}</td>
            </tr>
          </tbody>
        </template>
      </v-table>
    </v-col>
  </v-row>
    </div>
</template>

<script>
import AxiosInst from "@/plugins/axios";

export default {
  data: () => ({
    items: null,
    objet: {},
  }),

  created() {
    AxiosInst.get("http://localhost:8000/post", {
      params: {
        category_name: this.$route.params.cate,
      },
    })
      .then((res) => {
        this.items = res.data;
        const len = this.items.length;
        for (let i = 0; i < len; i++) {
          this.objet[i] = this.items[i].obj;
        }
      })
      .catch((err) => {
        alert(err);
      });
  },
  methods: {
    catePost(cate) {
      window.location.href = "http://localhost:8080/category/post/id/" + cate;
    },
  },
};
</script>
