import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

// https://astro.build/config
export default defineConfig({
  integrations: [
    starlight({
      title: "Clusview",
      customCss: [
        './src/styles/starlight-override.css'
      ],
      logo: {
        src: "./src/assets/clusview_banner.svg",
        replacesTitle: true
      },
      sidebar: [
        {
          label: "Start Here",
          autogenerate: { directory: "starthere" },
        },
      ],
    }),
  ],
});
