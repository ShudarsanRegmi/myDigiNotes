# Fonts and Responsiveness(Responsive Typography)

## Units

### em(wrt to parent element)

- Relative to the font-size of the parent element.
- If the parent element has a font-size of 16px, 1em is equal to 16px.
- Nested elements multiply their `em` values by the parent's font size

```css
body {
  font-size: 16px;
}

h1 {
  font-size: 2em; /* 2 * 16px = 32px */
}

.container {
  font-size: 1.5em; /* 1.5 * 16px = 24px */
}

.container p {
  font-size: 1em; /* 1 * 24px (parent size) = 24px */
}

```

### rem (wrt to the parent element)

- Relative to the font-size of the root element (`html`).

- Consistent regardless of nesting, making it easier to maintain uniform sizes across different components.

```css
html {
  font-size: 16px; /* 1rem = 16px */
}

h1 {
  font-size: 2rem; /* 2 * 16px = 32px */
}

.container {
  font-size: 1.5rem; /* 1.5 * 16px = 24px */
}

.container p {
  font-size: 1rem; /* 1 * 16px = 16px (ignores parent size) */
}

```



### Different Usage Examples

### Using em for component level resizing

```css
.container {
  font-size: 1.2em; /* Relative to body or parent */
}

.container h1 {
  font-size: 2em; /* 2 * 1.2em = 2.4em of the root font size */
}

.container p {
  font-size: 1em; /* 1 * 1.2em = 1.2em of the root font size */
}
```

### rem ensures site-wide consistent scaling

- Relative to the root element, making it easier to control the global font sizes.
- Simplifies scaling text across the entire document. 

### Fluid Line Length for Improved Readability

```css
.container {
    max-width: 800px;
    width: 90%;
    margin: 0 auto;
}
```

By setting a maximum width for text containers and ensuring they adapt fluidly to different screen sizes, you can prevent lines of text from becoming excessively long or short, thereby enhancing readability across devices.

