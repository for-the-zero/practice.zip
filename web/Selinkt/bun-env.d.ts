declare module "*.svg" {
    const path: `${string}.svg`;
    export = path;
}
declare module "*.module.css" {
    const classes: { readonly [key: string]: string };
    export = classes;
}
declare module '*.css' {
    const content: string;
    export default content;
}

interface link{
    name: string;
    url: string;
};
interface queryfmt {
    title: string;
    desc: string;
    links: link[];
    tgb: boolean;
};