import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        green: "#36E7A7",
        blue: "#33B6FF",
        red: "#EE436C",
        yellow: "#F8D762",
        purple: "#B04CFF",
        white: "#E3E7F5",
        black: "#1A1C27",
        "gray-5": "#252D3E",
        "gray-4": "#30384B",
        "gray-3": "#4D5B7A",
        "gray-2": "#65769C",
        "gray-1": "#9AA9CB",
      },
    },
  },
};
export default config;
