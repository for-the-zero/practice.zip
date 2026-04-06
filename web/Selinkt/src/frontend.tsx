import { createRoot } from "react-dom/client";
import { App } from "./App";
import { SketchProvider } from 'sketchbook-ui';
import 'sketchbook-ui/style.css';
import './style.css';
function start() {
    const root = createRoot(document.getElementById("root")!);
    root.render(<SketchProvider><App /></SketchProvider>);
};
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
} else {
    start();
};