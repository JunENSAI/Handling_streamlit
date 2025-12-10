"Query Parameters" are the key-value pairs found at the end of a URL (e.g., `myapp.com/?view=settings&id=123`).

Streamlit allows you to read and write these parameters programmatically. This is essential for **Deep Linking**—sending a user directly to a specific part of your app.

## 1. The Interface (`st.query_params`)

We use dictionary-like `st.query_params`.*

### A. Reading Parameters

You access parameters like a dictionary. It returns values as strings.

```python
# URL: http://localhost:8501/?tab=dashboard
view = st.query_params.get("tab", "default_value")
# view == "dashboard"
```

### B. Writing Parameters

To update the URL without reloading the page, you simply assign a value.

```python
st.query_params["tab"] = "settings"
# URL updates instantly to: http://localhost:8501/?tab=settings
```

### C. Clearing Parameters

```python
st.query_params.clear()
```

---

## 2. The Logic Flow

To make this work effectively, you generally follow this pattern:

* **Read URL at startup:** Determine the initial state of widgets based on the URL.

* **Initialize Widgets:** Set the default or index of widgets using the values read from the URL.

* **Update URL on interaction:** When the user changes a widget, update the URL to match.

---
