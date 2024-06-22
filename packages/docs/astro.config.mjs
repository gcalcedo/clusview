import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

// https://astro.build/config
export default defineConfig({
  site: "https://gcalcedo.github.io",
  base: "/clusview",
  integrations: [
    starlight({
      title: "Clusview",
      customCss: ["./src/styles/starlight-override.css"],
      logo: {
        src: "./src/assets/clusview_banner.svg",
        replacesTitle: true,
      },
      sidebar: [
        {
          label: "Start Here",
          items: [{ label: "Getting Started", link: "/starthere/welcome" }],
        },
        {
          label: "Components",
          items: [
            {
              label: "Loaders",
              items: [
                {
                  label: "Loaders Overview",
                  link: "/components/loaders/overview",
                },
              ],
            },
          ],
        },
      ],
    }),
  ],
});
