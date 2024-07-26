# Notes for streamlit library in python


## Data Flow
- **Data Flow:** Streamlit's architecture allows you to write apps the same way you write plain Python scripts. To unlock this, Streamlit apps have a unique data flow: any time something must be updated on the screen, Streamlit reruns your entire Python script from top to bottom.
bottom.

This can happen in two situations:

* Whenever you modify your app's source code.
* Whenever a user interacts with widgets in the app. For example, when dragging a slider, entering text in an input box, or clicking a button.

- Whenever a callback is passed to a widget via the on_change (or on_click) parameter, the callback will always run before the rest of your script.
