const { defineConfig } = require("@vue/cli-service");
const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

if (process.env.NODE_ENV === "production") {
  module.exports = defineConfig({
    transpileDependencies: true,
    outputDir: path.resolve(__dirname, "./dist"),
    pluginOptions: {
      vuetify: {
        // https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
      }
    },

    pages: {
      index: {
        template: "public/index.html",
        entry: "src/pages/main_home.js",
        filename: "home.html",
        title: "VueDjangoPhoto/home.html",
        minify: false
      },
      post_list: {
        template: "public/index.html",
        entry: "src/pages/main_post_list.js",
        filename: "post_list.html",
        title: "VueDjangoPhoto/post_list.html",
        minify: false
      },
      post_detail: {
        template: "public/index.html",
        entry: "src/pages/main_post_detail.js",
        filename: "post_detail.html",
        title: "VueDjangoPhoto/post_detail.html",
        minify: false
      },
      post_input: {
        template: "public/index.html",
        entry: "src/pages/main_post_input.js",
        filename: "post_input.html",
        title: "VueDjangoPhoto/post_input.html",
        minify: false
      }
    }
  });
} else {
  module.exports = defineConfig({
    transpileDependencies: true,
    outputDir: path.resolve(__dirname, "./dist"),
    pluginOptions: {
      vuetify: {
        // https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
      }
    },

    devServer: {
      proxy: "http://backend:8000"
    },

    configureWebpack: {
      plugins: [
        new HtmlWebpackPlugin({
          title: "home",
          template: "./dist/home.html",
          environment: process.env.NODE_ENV,
          chunks: ["vendor", "index"]
        })
      ]
    },

    pages: {
      index: {
        template: "public/index.html",
        entry: "src/pages/main_home.js",
        filename: "home.html",
        title: "VueDjangoPhoto/home.html",
        minify: false
      },
      post_list: {
        template: "public/index.html",
        entry: "src/pages/main_post_list.js",
        filename: "post_list.html",
        title: "VueDjangoPhoto/post_list.html",
        minify: false
      },
      post_detail: {
        template: "public/index.html",
        entry: "src/pages/main_post_detail.js",
        filename: "post_detail.html",
        title: "VueDjangoPhoto/post_detail.html",
        minify: false
      },
      post_input: {
        template: "public/index.html",
        entry: "src/pages/main_post_input.js",
        filename: "post_input.html",
        title: "VueDjangoPhoto/post_input.html",
        minify: false
      }
    }
  });
}
