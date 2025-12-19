Streamlit uses the `st.connection` factory to talk to databases. It sits on top of **SQLAlchemy**, which means it supports almost any SQL database (Postgres, MySQL, SQLite, Snowflake).

## 1. The Secrets Configuration

Streamlit looks for a specific section in your `secrets.toml` called `[connections.<name>]`.

### Option A: PostgreSQL (Production Standard)
If you have a Postgres server running, your `.streamlit/secrets.toml` should look like this:

```toml
[connections.my_database]
dialect = "postgresql"
host = "localhost"
port = "5432"
username = "postgres"
password = "mypassword"
database = "portfolio_db"
```

### Option B: SQLite (Local/Easy for Testing)

If you don't have a Postgres server installed, we can use a local file.

```toml
[connections.portfolio_db]
url = "sqlite:///portfolio.db"
```

---

## 2. The Code Interface
Connecting is a 2-step process:

```Python
# 1. Initialize Connection (Cached Resource)
conn = st.connection("my_database", type="sql")

# 2. Run Query (Cached Data)
df = conn.query("SELECT * FROM bitcoin_prices", ttl=600)
```

### Key Concepts

- `type="sql":` Tells Streamlit to use the generic SQL handler.

- `ttl=600:` "Time To Live". This is crucial. It means "Run this query once, and keep the result in memory for 600 seconds (10 mins)". If a user refreshes the page 10 seconds later, Streamlit does not hit the database again; it serves the memory cache. This makes your app fast and saves DB costs.

---

## 3. Steps before running Practical session

- Firstly, in your terminal you need to run `db.py`
```bash
python3 db.py
```
- Secondly in the SQL_connection folder add `.streamlit/secrets.toml`. This contains the minimal configuration for the app.

- Finally run the webapp with : 
```bash
streamlit run sql_connection.py
```
---