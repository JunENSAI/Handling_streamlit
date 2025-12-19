When a user hits "Refresh" (F5), Streamlit destroys the `session_state` and creates a new one. To remember a user across refreshes (or even after they close the tab), we must store data in the **Browser's Cookies**.

## 1. The Tool: Cookie Manager

Use a popular community library: `extra-streamlit-components`. Directly installed from `requirements.txt`.

---

## 2. Reading & Writing

The CookieManager acts as a bridge between Python (Server) and the Browser.

### Initialization

```python
import extra_streamlit_components as stx

# You only need to initialize this once
cookie_manager = stx.CookieManager()
```

### Writing a Cookie

When you set a cookie, Streamlit sends a signal to the browser. 

**Crucial Note:** The cookie is not immediately available in Python on the current run because the browser needs to receive the command, save it, and send it back.

```python
cookie_manager.set("user_token", "abc-123", key="set_cookie")
```

### Reading a Cookie

This reads what the browser sent in the request headers.

```python
token = cookie_manager.get("user_token")
```

### Deleting

```python
cookie_manager.delete("user_token")
```

---

## 3. The "Async" Challenge

Because Streamlit runs on the server and Cookies live in the browser, there is a latency.

- Python says "Set Cookie".

- Script finishes.

- Browser receives "Set Cookie".

- User refreshes.

- Python says "Get Cookie" $\rightarrow$ Now it gets the value.

- To handle this smoothly, we often force a st.rerun() or wait for the UI to update.

### Key Takeaways for "Persistence"

- **State Layering:**

    - **Level 1 (session_state):** Fast, handles variables while the user is active. Wiped on refresh.

    - **Level 2 (CookieManager):** Slow, persists across refreshes/days. Used only to restore Level

- **Implementation Pattern:** You rarely use cookie_manager.get() directly in your main logic. Instead, at the very top of your script, you do:

    - `token = cookie_manager.get('auth')`
    
    - `if token: $\rightarrow$ st.session_state['logged_in'] = True`

---
