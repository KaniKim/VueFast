export default {
  modules: [
    "@nuxtjs/tailwindcss"
  ],
  css: [
    "~/assets/css/style.css"
  ],
  tailwindcss: {
    cssPath: "~/assets/css/style.css",
    configPath: "tailwind.config",
    exposeConfig: false,
    injectPosition: 0,
    viewer: true,
  },
  buildModules: [
    [
      "@nuxtjs/tailwindcss",
      "@nuxt/typescript-build",
      {
        typeCheck: {
          typescript: {
            extensions: {
              vue: true
            }
          }
        }
      }
    ]
  ]
};
