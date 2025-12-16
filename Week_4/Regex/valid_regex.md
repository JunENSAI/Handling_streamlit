Validation should happen on the **Frontend** (before sending data) to provide immediate feedback and save server resources.

## 1. The Tool: Python's `re` module

Streamlit doesn't have built-in regex validators on widgets, so we use Python's standard library.

```python
import re

email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
password_pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$"
```
---

## 2. Validation Strategies

### A. The "Submit Blocking" Strategy

The form cannot be processed until the regex matches.

```Python
email = st.text_input("Email")

if st.button("Submit"):
    if not re.match(email_pattern, email):
        st.error("Invalid Email Format!")
    else:
        st.success("Processing...")
```

### B. The "Live Feedback" Strategy (Better UX)

Using st.warning that appears immediately (requires session_state or just checking the variable outside the form).

```Python

email = st.text_input("Email")
if email and not re.match(email_pattern, email):
    st.warning("Please enter a valid email address.")
```

---

## 3. Sanitization (The hidden step)

Validation checks the format. Sanitization cleans the input. Even if an input passes regex, always strip whitespace.

```Python
clean_email = email.strip().lower()
```

### Key Takeaways for "Handling Security"

- User Feedback: **Regex** isn't just for security; it's for User Experience. Telling the user exactly why their password failed (e.g., "Missing a number") is better than a generic "Error" message.

- Layered Defense: **Regex** stops the "dumb" attacks (invalid formats). Parameterized Queries stop the "smart" attacks (SQL Injection).

---
