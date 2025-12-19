Streamlit provides a native way to handle sensitive information (Database passwords, API keys) securely without exposing them in your source code.

## 1. The Secrets File (`secrets.toml`)

Locally (on your computer), secrets are stored in a file named `secrets.toml` located inside a hidden folder `.streamlit`.

**File Structure:**
```text
my_project/
├── .streamlit/
│   └── secrets.toml
├── app.py
└── .gitignore
```

### TOML Format

TOML is similar to INI or simple configuration files.

**Content of .streamlit/secrets.toml:**

```TOML
# Top level keys
project_name = "My Portfolio"

# Sections (Tables)
[database]
host = "localhost"
port = 5432
username = "admin"
password = "super_secret_password_123"

[credentials]
username = "Junior"
password = "streamlit_123"
```

---

## 2. Accessing Secrets in Python
Streamlit loads this file automatically into st.secrets. It acts like a dictionary.

```Python
import streamlit as st

# Accessing top level
st.write(st.secrets["project_name"])

# Accessing nested sections (Dict notation)
db_user = st.secrets["database"]["username"]
db_pass = st.secrets["database"]["password"]

# Attribute notation also works
db_host = st.secrets.database.host
```
---

## 3. Security (The .gitignore)

You MUST ensure git ignores this file. If you are using Git, create a .gitignore file in your root folder and add:

```Plaintext
.streamlit/secrets.toml
```

---