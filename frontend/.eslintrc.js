module.exports = {
  env: {
    node: true,
    es2021: true
  },
  extends: ["eslint:recommended", "plugin:vue/essential"],
  parserOptions: {
    ecmaVersion: "2020"
  },
  plugins: ["vue"],
  rules: { "vue/multi-word-component-names": 0 }
};
