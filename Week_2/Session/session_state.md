Streamlit's execution model is **Stateless**. This means that every time you interact with the app (click, type, scroll), the entire script re-runs from top to bottom. By default, variables are reset on every run.

**Session State** (`st.session_state`) is a dictionary-like object that persists across these re-runs for a specific user session.

## 1. The Problem: The "Flash" of Data

In a standard Python script:
```python
counter = 0
if st.button("Increment"):
    counter += 1
st.write(counter)
```

**Result:**  The counter never goes above 1. Why? Every time you click "Increment", the script restarts, sets counter = 0, increments it to 1, and stops.

## 2. The Solution: st.session_state

Think of st.session_state as the "Long-Term Memory" of your app.

- **Pattern 1:** Initialization

You must check if a variable exists before using it, otherwise, you'll get a KeyError.

```python
# Check if 'count' exists in memory. If not, create it.
if 'count' not in st.session_state:
    st.session_state['count'] = 0
```

- **Pattern 2:** Reading & Writing

You access it just like a Python dictionary or an attribute.

```python
# Reading
current_value = st.session_state['count'] 

# Writing
st.session_state['count'] = current_value + 1
```

## 3. Widget State (The key parameter)

Every widget (input, button, checkbox) can automatically save its value to Session State using the key parameter.

```python
# This text input is linked to st.session_state['my_user_name']
st.text_input("Enter Name", key="my_user_name")

# You can now access this value anywhere, even before the widget code line (in the next rerun)
st.write(f"Stored Name: {st.session_state.my_user_name}")
```

## 4. The "Trigger" Pattern (Fixing your Portfolio)

A common requirement is: "Click a button to load data, and keep it loaded."

- **Wrong Way:**

```python
if st.button("Load"):
    show_data() # Vanishes on next click
```

- **Correct Way:**

```python
# 1. Initialize state
if 'data_loaded' not in st.session_state:
    st.session_state['data_loaded'] = False

# 2. Update state on click
if st.button("Load"):
    st.session_state['data_loaded'] = True

# 3. Check STATE, not BUTTON
if st.session_state['data_loaded']:
    show_data() # Stays visible!
```