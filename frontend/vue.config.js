const { defineConfig } = require("@vue/cli-service");
const path = require("path");
module.exports = defineConfig({
  transpileDependencies: true,

  outputDir: path.resolve(__dirname, "./dist"),

  pluginOptions: {
    vuetify: {
      // https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
    }
  },
  pages: {
    home: {
      template: "public/index.html",
      entry: "src/pages/main_home.js",
      filename: "home.html",
      title: "VueDjangoPhoto/home.html",
      minify: false
    },
    post_list: {
      template: "public/index.html",
      entry: "src/pages/main_home.js",
      filename: "post_list.html",
      title: "VueDjangoPhoto/post_list.html",
      minify: false
    },
    post_detail: {
      template: "public/index.html",
      entry: "src/pages/main_home.js",
      filename: "post_detail.html",
      title: "VueDjangoPhoto/post_detail.html",
      minify: false
    }
  }
});
