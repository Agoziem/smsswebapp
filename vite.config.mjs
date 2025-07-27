import { defineConfig } from "vite";
import { resolve } from "path";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  base: "/static/",
  resolve: {
    alias: {
      "@": resolve(__dirname, "static"), // NOT static/js
    },
  },
  plugins: [tailwindcss()], // <-- move this here
  build: {
    manifest: "manifest.json",
    outDir: resolve("./assets"),
    rollupOptions: {
      input: {
        main: resolve("./static/js/index.js"),
      },
    },
  },
});
