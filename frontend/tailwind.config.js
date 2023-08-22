// tailwind.config.js
export const defaultTailwindConfig = ({rootDir,  srcDir}) => ({
  purge: {
    content: [
      `${srcDir}/components/**/*.{vue,js,ts}`,
      `${srcDir}/layouts/**/*.vue`,
      `${srcDir}/pages/**/*.vue`,
      `${srcDir}/plugins/**/*.{js,ts}`,
      `${rootDir}/nuxt.config.js`,
      `${rootDir}/nuxt.config.ts`
    ]
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
});

