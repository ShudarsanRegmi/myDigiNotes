# Webpack

> Webpack is a powerful JavaScript module bundler that compiles and bundles multiple modules, assets, and dependencies into optimized output files for web applications.



### Need for webpack

> There are problems with managing JavaScript projects this(https://webpack.js.org/guides/getting-started/) way:
>
> - It is not immediately apparent that the script depends on an external library.
> - If a dependency is missing, or included in the wrong order, the application will not function properly.
> - If a dependency is included but not used, the browser will be forced to download unnecessary code.

## Basic setup

```bash
mkdir webpack-demo
cd webpack-demo
npm init -y
npm install webpack webpack-cli --save-dev
```



Note:  Note that webpack will not alter any code other than `import` and `export` statements. If you are using other [ES2015 features](http://es6-features.org/), make sure to [use a transpiler](https://webpack.js.org/loaders/#transpiling) such as [Babel](https://babeljs.io/) via webpack's [loader system](https://webpack.js.org/concepts/loaders/).

## Directory Structure

```diff
webpack-demo
  |- package.json
  |- package-lock.json
  |- webpack.config.js
+ |- /dist
+   |- index.html
  |- /src
    |- index.js
```

### pacWebpack config

```javascript
const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist'),
  },
};
```

### A sample package.json file

```json
 {
   "name": "webpack-demo",
   "version": "1.0.0",
   "description": "",
   "private": true,
   "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack"
   },
   "keywords": [],
   "author": "",
   "license": "ISC",
   "devDependencies": {
     "webpack": "^5.4.0",
     "webpack-cli": "^4.2.0"
   },
   "dependencies": {
     "lodash": "^4.17.20"
   }
 }
```

### Compiling with config file

```bash
npx webpack --config webpack.config.js	
```

Note: --config option in case name is other than webpack.config.js

### Running Build script

```bash
npm run build
```

### Loaders

Webpack enables use of loaders to preprocess files. This allows you to bundle any static resource way beyond JavaScript. You can easily write your own loaders using Node.js.

