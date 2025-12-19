Streamlit reruns your *entire* script on every interaction. If you have a function that takes 5 seconds to run, your app will have a 5-second lag on every click.

**Caching** saves the result of a function. If the function is called again with the same parameters, Streamlit skips the execution and returns the saved result instantly.

---

## 1. The Two Types of Cache

Streamlit (since version 1.18) separates caching into two distinct decorators:

### A. `st.cache_data` (For Data & Computations)

Use this for functions that return data you could serialize (save to a file).

* **Examples:** SQL queries returning DataFrames, CSV loading, mathematical transformations, API responses.

* **Behavior:** It creates a copy of the data on every call to prevent mutation bugs.

```python
@st.cache_data(ttl=3600)  # Cache for 1 hour
def fetch_sales_data(region):
    time.sleep(5) 
    return pd.read_sql(f"SELECT * FROM sales WHERE region='{region}'", conn)
```

### B. `st.cache_resource` (For Global Objects)

Use this for objects that cannot be saved to a file or should be shared across all users/sessions.

- **Examples**: Database connections, ML Models (TensorFlow/PyTorch), Thread pools.

- **Behavior**: It returns the exact same object (reference) to everyone. It is not copied.

```python
@st.cache_resource
def load_heavy_model():
    # Loading a 5GB AI model takes time!
    model = DeepLearningModel.load("v2.pt")
    return model
```

---

## 2. The Mechanics (Hashing)

Streamlit decides whether to run the function or use the cache by hashing three things:

- **The Code:** If you change one character in the function body, the cache invalidates.

- **The Parameters:** func(1) and func(2) are stored separately.

- **The Name:** The function name.

---

## 3. The ttl (Time To Live) parameter

In a real-time dashboard, you don't want data cached forever.

- **ttl=600:** Keep data for 600 seconds. After that, the next user who visits triggers a fresh reload.

### Key Takeaways for "Handling Asynchronization/Treatment"

- **Blocking:** Streamlit is synchronous. A 3-second function freezes the UI for 3 seconds. Caching "unblocks" subsequent runs by skipping the work.

- `show_spinner=True`: This provides immediate visual feedback to the user ("Running...") so they don't think the app crashed while waiting for the cache miss.

---
