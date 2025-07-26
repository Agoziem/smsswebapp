import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  base: "/static/",
  build: {
    manifest: "manifest.json",
    outDir: resolve("./assets"),
    rollupOptions: {
      input: {
        main: resolve("./static/js/main.js"),
      }
    }
  }
})