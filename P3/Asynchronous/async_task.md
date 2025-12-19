When a task takes more than 1 second, you **must** provide visual feedback. If the screen freezes without feedback, users will click the button again (causing a crash) or close the tab.

## 1. The Basic Spinner (`st.spinner`)

Used when you don't know how long a task will take (e.g., a network request).

```python
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')
```
---

## 2. The Progress Bar (st.progress)

Used when you have a loop or known steps (e.g., processing 100 rows).

```python
my_bar = st.progress(0, text="Starting operation...")

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=f"Processing item {percent_complete}")
    
time.sleep(1)
my_bar.empty() # Remove the bar when done
```

---

## 3. The Status Container (st.status)

Introduced recently, this is the best way to handle multi-step processes (like an installation wizard or data audit). It creates an expander that updates its label as it moves through steps.

```python
with st.status("Downloading data...", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found 10GB of data.")
    
    st.write("Downloading...")
    time.sleep(1)
    
    status.update(label="Download complete!", state="complete", expanded=False)
```

---

## 4. True Asynchrony (asyncio)

Streamlit supports Python's async and await syntax.

```python
import asyncio

async def fetch_data():
    await asyncio.sleep(2)
    return "Data"

# You run it using asyncio.run() inside standard Streamlit
if st.button("Run Async"):
    val = asyncio.run(fetch_data())
    st.write(val)
```

*Note: While supported, mixing async loops with Streamlit's rerun model can be complex. For 95% of use cases, UI feedback (`st.status`) is preferred over actual async code.*

---

