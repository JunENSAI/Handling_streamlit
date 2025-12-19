Streamlit is secure by default because it renders text as "Plain Text". However, the moment you use `unsafe_allow_html=True`, you open a door for hackers.

## 1. The XSS Vulnerability (Cross-Site Scripting)

**XSS** happens when an attacker inputs a piece of JavaScript code into your app (e.g., as their username), and your app renders it, causing that script to run on *other* users' browsers (stealing their cookies/tokens).

### The Danger 

```python
# DANGEROUS: If user_input contains "<script>alert('Hacked')</script>"
st.markdown(f"Hello {user_input}", unsafe_allow_html=True)
```

### The Solution: Html Escaping

If you must use `HTML` (for custom styling), you must "Escape" the user input first. This converts special characters like `< into &lt;`, which the browser displays as text but does not execute as code.

```Python

import html

safe_input = html.escape(user_input)
st.markdown(f"<b>Hello {safe_input}</b>", unsafe_allow_html=True)
```

---

## 2. SQL Injection (Review)

- **Attack:** Inputting ' OR '1'='1 into a login field to bypass password checks.

- **Defense:** Always use `params={}`.

---

## 3. Data Leaks (Error Handling)

Never show raw Python error traces in Production.

- **Bad:** The user sees `ConnectionError: Password for user 'admin' failed at 192.168.1.5`.

- **Good:** The user sees `An internal error occurred`. Please contact support.

### Key Takeaways for "Handling Security"

- **Trust No One:** Every input (Database, API, User Form) is a potential threat.

- `st.write` is your friend: It handles escaping automatically. Only reach for `unsafe_allow_html=True` if you absolutely need a specific CSS layout, and always wrap variables in `html.escape()`.

---