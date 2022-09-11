const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  configureWebpack: {
    module: {
      rules: [
        {
          test: /\.css$/,
          use: ["postcss-loader"],
        },
      ],
    },
  },
});
