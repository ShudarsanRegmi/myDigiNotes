# useEffect Hook

`The useEffect hook in React is a powerful tool for handling side effects in functional components. Side effects are operations that affect something outside the scope of the function being executed, such as fetching data, subscribing to events, or manually changing the DOM.

**Syntax**:

```jsx
useEffect(function, dependencies)
```

**Return**

`undefined`

**Parameters:**

- function: After every re-render withs changed dependencies, React will first run the cleanup function (if you provided it) with the old values, and then run your setup function with the new values. After your component is removed from the DOM, React will run your cleanup function.
- dependencies: The list of all reactive values referenced inside of the `setup` code. Reactive values include props, state, and all the variables and functions declared directly inside your component body.

**Caveats**

- If you’re not trying to synchronize with some external system, you probably don’t need an Effect.
- If your Effect wasn’t caused by an interaction (like a click), React will generally let the browser paint the updated screen first before running your Effect. If your Effect is doing something visual (for example, positioning a tooltip), and the delay is noticeable (for example, it flickers), replace useEffect with useLayoutEffect.
- Even if your Effect was caused by an interaction (like a click), **React may allow the browser to repaint the screen before processing the state updates inside your Effect.** Usually, this works as expected. However, if you must block the browser from repainting the screen, you need to replace `useEffect` with [`useLayoutEffect`.](https://react.dev/reference/react/useLayoutEffect)
- Effects **only run on the client.** They don’t run during server rendering.

### Basic Usage

```jsx
import { useEffect } from 'react';

function ExampleComponent() {
  useEffect(() => {
    // Code to run on component mount and update

    return () => {
      // Cleanup code to run on component unmount or before the next effect
    };
  }, [/* Dependencies */]);
}
```

**Key Concepts**

- **Initial Effect:** The function passed to useEffect runs after the component renders. It's used to perform action such as fetching data or setting up subscriptions.
- **Dependencies Array: ** The second argument to useEffect is an array of dependencies. The effect runs only when one of the dependencies changes. If the array is empty ([]), the effect runs only once, after the initial render.
- **Cleanup Function**: If the effect returns a function, React calls it before the component unmounts and before running the effect again on subsequent renders. This is useful for cleaning up subscriptions, timers, or other resources to prevent memory leaks.

> Note: Use useEffect wisely to keep your components performant and readable. Consider breaking down complex effects into smaller, manageable pieces or custom hooks.

## Dependency array

- If no dependency is passed then the effect runs on every render
- If empty dependency array is pased [], then the components run the first render only
- If [prop,states...] are passed then the effect will run on first render and as well as with the change in states and prop(dependencies)

## Subscriptions

 A subscription refers to the process of setting up an ongoing connection or listener to a source of data or events. This connection continuously provides updates or notifications to the component, which then responds to these changes. 

**Example1 (Event Listeners)**

```jsx
useEffect(() => {
  function handleResize() {
    console.log('Window resized');
  }

  window.addEventListener('resize', handleResize);

  return () => {
    window.removeEventListener('resize', handleResize);
  };
}, []);

```

**Example2 (Web Socket Connection):**

```jsx
useEffect(() => {
  const socket = new WebSocket('ws://example.com/socket');

  socket.onmessage = (event) => {
    console.log('Message from server', event.data);
  };

  return () => {
    socket.close();
  };
}, []);
```

They are called subscriptions because they are the source of potentially continuously changing data.

## Different use cases of useEffect hook

### Fetching Data

```jsx
useEffect(() => {
  async function fetchData() {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    // Update state with the fetched data
  }

  fetchData();
}, []); // Empty array ensures this runs only once
```

### Setting up subscriptions

Subscriptions can be setup to data streams or event listeners

```jsx
useEffect(() => {
  function handleResize() {
    console.log('Window resized');
  }

  window.addEventListener('resize', handleResize);

  return () => {
    window.removeEventListener('resize', handleResize);
  };
}, []); // Empty array ensures this runs only once
```

### Clean up resources

Cleanup resources such as timers, subscriptions, or event listeners, when the component unmounts or before the effect runs. 

```jsx
useEffect(() => {
  const timer = setInterval(() => {
    console.log('Timer tick');
  }, 1000);

  return () => {
    clearInterval(timer);
  };
}, []); // Empty array ensures this runs only once

```

### Synchronise with props or state

Run the side effects in response to changes in state or props

```jsx
useEffect(() => {
  function doSomething() {
    console.log('State or prop changed');
  }

  doSomething();
}, [dependency]); // Effect runs when 'dependency' changes

```



### Animating components

Triggering animations or handle css class changes.

```jsx
useEffect(() => {
  const element = document.querySelector('.my-element');
  element.classList.add('animate');

  return () => {
    element.classList.remove('animate');
  };
}, []); // Empty array ensures this runs only once

```

### Handling custom hooks

Compose useEffect inside custom hooks for reusable side-effect logic. 

```jsx
function useCustomHook(dependency) {
  useEffect(() => {
    // Custom hook logic
  }, [dependency]);
}
```

### Conditionally running effects

Run effects conditionally based on certain conditions

```jsx
useEffect(() => {
  if (someCondition) {
    // Run the effect
  }
}, [someCondition]);
```

### Debouncing Input

Implementing debouncing logic for input fields

```jsx
useEffect(() => {
  const handler = setTimeout(() => {
    console.log('Input value:', value);
  }, 300); // Delay in milliseconds

  return () => {
    clearTimeout(handler);
  };
}, [value]); // Run the effect when 'value' changes
```

​	