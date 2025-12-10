Building a login system in Streamlit requires a specific "Check Order" at the very top of your script.

## 1. The Logic Flow

To solve the "Refresh = Disconnect" problem, we prioritize our checks:

1.  **Check RAM (`session_state`):** Is the user *already* logged in during this active run? If yes, show the App.

2.  **Check Browser (`cookie`):** If not in RAM, is there a valid token in the browser cookies?

    * **If Yes:** Validate token $\rightarrow$ Update RAM $\rightarrow$ Show App.

    * **If No:** Show Login Form.

---

## 2. Security Note (Hashing)

**Never** store plain-text passwords in your code or cookies.

* **In Code:** Store the *Hash* of the password.

* **In Cookie:** Store a random session token (or JWT), never the password itself.

We will simulate the validation logic, but in a real app, you would compare inputs against a database hash.

---

## 3. The "Switchboard" Pattern

To keep the code clean, we define two main functions: `login_page()` and `main_app()`. The top of the script acts as a switchboard deciding which one to run.

```python
if st.session_state['logged_in']:
    main_app()
else:
    login_page()
```

### Key Takeaways for "Handling Connection"

- **The Wait:** When you click "Log Out", cookie_manager.delete sends a signal. The browser processes it. The `st.rerun()` is crucial to immediately refresh the Python script so it notices the cookie is gone.

- **Logic Separation:** Notice how `show_main_app()` contains the entire Sidebar and Dashboard code. This ensures that nothing is rendered unless the auth check passes.

---