Writing to a database in Streamlit requires a specific cycle to ensure the user interface stays in sync with the database.

## 1. The "Write" Cycle

1.  **Input:** Collect data via a Form (to prevent partial writes).

2.  **Sanitization:** Prepare the data (format dates, numbers).

3.  **Execution:** Run the SQL `INSERT` command.

4.  **Refresh:** Clear the cache and rerun the app so the new data appears instantly.

---

## 2. Security: Parameterized Queries

**FATAL ERROR (SQL Injection Risk):**
Never use f-strings to insert user variables directly.
```python
# DON'T DO THIS
conn.query(f"INSERT INTO users VALUES ('{username}')")

# DO THIS
conn.query(
    "INSERT INTO users VALUES (:name)", 
    params={"name": username}
)
```

---

## 3. Handling the Cache

When you add a new row, the old `SELECT *` query stored in Streamlit's cache is now outdated. You typically don't need to manually `clear_cache()`. 

Instead, simply calling `st.rerun()` will re-fetch the data if the TTL (Time To Live) has expired, or you can force the query to run without cache for specific updates.

### Key Takeaways for "Handling Graphic + Connection"

- `st.rerun()`: This is mandatory after a write operation. If you don't call it, the database will have the new row, but the chart on the screen will still show the old data until you manually refresh the page.

- **Forms:** Using st.form ensures we don't send an incomplete SQL query while you are still typing the price.

---