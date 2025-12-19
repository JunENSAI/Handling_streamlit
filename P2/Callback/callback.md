In the standard Streamlit flow, you check widget values inside the main script body (e.g., `if st.button(...)`).

With **Callbacks**, you tell Streamlit: "When this specific widget changes, run this specific function **first**, update the Session State, and *then* rerun the script."

## 1. Syntax

Most input widgets support these parameters:

* `on_change=my_function`: Triggers when the value changes (Text Input, Slider, Selectbox).

* `on_click=my_function`: Triggers when clicked (Button).

* `args=(a, b)`: Arguments to pass to your function.

* `kwargs={'x': 1}`: Keyword arguments to pass.

```python
def clear_text():
    st.session_state.my_text = ""

# When button is clicked, 'clear_text' runs immediately
st.button("Reset", on_click=clear_text)
st.text_input("Type here", key="my_text")
```
---

## 2. The Execution Flow

- User interacts with widget.
             
- Callback Function runs. (Updates Session State here).

- Script Reruns from top to bottom.

- UI updates reflecting the new State.

---

## 3. Why use Callbacks?

- **Clean Code:** It separates "Logic" (functions) from "UI" (layout).

- **Synchronization:** Essential for bidirectional syncing (e.g., changing Celsius updates Fahrenheit AND changing Fahrenheit updates Celsius).

- **Input Clearing:** It is the only reliable way to clear/reset an input box programmatically.

### Key Takeaways for "Handling Synchronization"

- **The key is dual-purpose:** It sets the initial value of the widget (reading from state) AND saves the new value to state.

- **No Infinite Loops:** Streamlit is smart enough to know that if the callback updates the state, it shouldn't re-trigger the other callback recursively in the same run.

---