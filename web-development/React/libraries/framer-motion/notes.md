# Framer motion quick tutorial/revision notes

- Deeply animate throughout React trees via [variants](https://www.framer.com/motion/animation/#variants)

Motion can animate:

- Numbers: `0`, `10` etc.
- Strings containing numbers: `"0vh"`, `"10px"` etc.
- Colors: Hex, RGB, HSLA.
- Complex strings containing multiple numbers and/or colors (ie `"10px 0 #000"`)



When animating to a non-animatable value like `"block"`, this value will be set instantly. By setting this value within `transitionEnd`, this value will be set at the end of the animation.

```jsx
<motion.div
  animate={{
    x: 0,
    backgroundColor: "#000",
    boxShadow: "10px 10px 0 rgba(0, 0, 0, 0.2)",
    position: "fixed",
    transitionEnd: {
      display: "none",
    },
  }}
/>
```

### Properties for transform 

```
Translate shortcuts: x, y, z
Translate: translateX, translateY, translateZ
Scale: scale, scaleX, scaleY
Rotate: rotate, rotateX, rotateY, rotateZ
Skew: skew, skewX, skewY
Perspective: transformPerspective

# for transform origin
originX
originY
originZ
```

### transition prop

```jsx
 transition={{
        duration: 2,
        ease: "easeInOut",
        times: [0, 0.2, 0.5, 0.8, 1], # for keyframes
        repeat: Infinity,
        repeatDelay: 1
      }}
```

### animate prop

```jsx
 animate={{
        scale: [1, 2, 2, 1, 1],
        rotate: [0, 0, 180, 180, 0],
        borderRadius: ["0%", "0%", "50%", "50%", "0%"]
      }}
```



### Doing exit animations

```jsx
<AnimatePresence>
  {isVisible && (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    />
  )}
</AnimatePresence>
```

- If array is used as value then that will be considered as key frame. 

### A simple gesture animations

```jsx
<motion.button
  initial={{ opacity: 0.6 }}
  whileHover={{
    scale: 1.2,
    transition: { duration: 1 },
  }}
  whileTap={{ scale: 0.9 }}
  whileInView={{ opacity: 1 }}
/>
```

## Variants

Setting `animate` as an object is useful for simple, single-component animations. But sometimes we want to create animations that propagate throughout the DOM, and orchestrate those animations in a declarative way. We can do so with variants.

- Variants are sets of pre-defined targets.
- They're passed into `motion` components via the `variants` prop.
- If a `motion` component has children, changes in variant will flow down through the component hierarchy until a child component defines its own `animate` property.

```jsx
const variants = {
  visible: { opacity: 1 },
  hidden: { opacity: 0 },
}
<motion.div variants={variants} />

```

