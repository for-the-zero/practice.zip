import tailwindPlugin from "bun-plugin-tailwind";
import { rmSync } from "fs";

rmSync("./dist", { recursive: true, force: true });

await Bun.build({
  entrypoints: ["./src/index.html"],
  outdir: "./dist",
  target: "browser",
  minify: true,
  root: "./src",
  plugins: [tailwindPlugin],
});
