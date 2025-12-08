By default, Streamlit is **reactive**. If you have a text input and you type the letter "A", the script reruns. You type "B", it reruns again. This is great for instant feedback (like a search bar), but terrible for data entry (like a registration page) or expensive computations.

**Forms** allow you to batch multiple user inputs and process them all at once only when a "Submit" button is clicked.

## 1. The Structure (`st.form`)

A form is a container. Everything inside this container will **NOT** trigger a script rerun when changed. The rerun only happens when the special `st.form_submit_button` is pressed.

```python
with st.form(key="my_form"):
    # These inputs won't trigger a reload
    name = st.text_input("Name")
    age = st.number_input("Age")
    
    # This button triggers the reload and unlocks the data
    submitted = st.form_submit_button("Submit")

if submitted:
    st.write(f"Hello {name}, you are {age}")
```

---

## 2. The Golden Rules of Forms

- Every form needs a key: It's best practice to name your form (e.g., key="login_form").

- Every form needs a Submit Button: If you forget st.form_submit_button, Streamlit will warn you.

- **No Interactivity Inside:** You cannot include a "regular" button inside a form. You cannot have dynamic logic inside a form (e.g., "If I check this box, show this other input immediately") because the script stops checking for updates inside the form until submitted.

---

## 3. Form vs. Session State

Forms are often used combined with st.session_state to create "edit modes" or robust data entry pipelines where you validate data after submission.

### Key Takeaways for "Handling Connection"

- Never connect to a database directly on a raw `st.text_input`. It would hit your database on every keystroke.

- Always wrap database "INSERT/UPDATE" operations inside a `st.form` or behind a standard `st.button` check to ensure the connection happens only once per submission.

---