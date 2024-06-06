# useRef Hook

`useRef` is a React Hook that lets you reference a value that’s not needed for rendering.

The `useRef` Hook allows you to persist values between renders.

It can be used to access a DOM element directly.

yoIt can be used to store a mutable value that does not cause a re-render when updated.

refs are perfect for storing information that doesn’t affect the visual output of your component. 



**Syntax**

`const ref = useRef(initialValue)`

**Parameters:**

- **initialValue:** The value to be set for ref object's property iniitally

**Returns:**

Returns a value with single property  `current` 

`current`: Initially, it’s set to the `initialValue` you have passed. You can later set it to something else. If you pass the ref object to React as a `ref` attribute to a JSX node, React will set its `current` property

**Caveats**

- When you change the `ref.current` property, React does not re-render your component. React is not aware of when you change it because a ref is a plain JavaScript object.
- Do not write *or read* `ref.current` during rendering, except for [initialization.](https://react.dev/reference/react/useRef#avoiding-recreating-the-ref-contents) This makes your component’s behavior unpredictable.
- You can mutate the `ref.current` property. Unlike state, it is mutable. However, if it holds an object that is used for rendering (for example, a piece of your state), then you shouldn’t mutate that object.

**By using refs, you ensure that**

- You can **store information** between re-renders (unlike regular variables, which reset on every render).
- Changing it **does not trigger a re-render** (unlike state variables, which trigger a re-render).
- The **information is local** to each copy of your component (unlike the variables outside, which are shared).

## Different use cases

### Accessing an element in the DOM

```jsx
import React, { useRef } from 'react';

function TextInput() {
  const inputRef = useRef(null); // Create a ref to store the input DOM element

  const focusInput = () => {
    inputRef.current.focus(); // Focus the input field without re-rendering
  };

  return (
    <div>
      <input ref={inputRef} type="text" />
      <button onClick={focusInput}>Focus Input</button>
    </div>
  );
}
```

