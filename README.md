# Handling_streamlit
Learn to build a reactive dashboard with streamlit. Through all component that must be required on a project.

## Advices :

Before you start you need to :

- Create a virtual environnement to make sure that the packages does not collapse with other dependencies

```bash
python3 -m venv name_env
```

- Activate the virtual environnement that you name :

```bash
source path/name_env/bin/activate
```
- Install the packages required for this repo :

```bash
pip install -r requirements.txt
```
---

## **Week 1 — UI Anatomy (Layouts & Navigation)**  

**Goal:** Master visual structure: sidebars, tabs, containers, and custom navigation.

### **Day 1 — Environment & Execution Flow**
- **Topic:** Setup, running apps, top-down execution model.  

- **Task:** Build a *Hello World* app and test hot-reloading.

### **Day 2 — Sidebar (`st.sidebar`)**
- **Topic:** Moving inputs/navigation to the sidebar.  

- **Deep Dive:** Differences between `st.sidebar.button` and `st.button`.  

- **Code Focus:** `with st.sidebar:` vs. object notation.

### **Day 3 — Columns & Containers**
- **Topic:** `st.columns`, `st.container`.  

- **Task:** Build a responsive dashboard layout (e.g., 3 KPI tiles in a row).

### **Day 4 — Tabs & Expanders**
- **Topic:** `st.tabs`, `st.expander` for structured UI organization. 

- **Project:** Settings panel with separate tabs (User Info, App Settings).

### **Day 5 — Top Bar & Custom Navigation**
- **Topic:** `st.set_page_config` (title, icon, layout).  

- **Note:** No native Streamlit navbar. Use `streamlit-option-menu` or CSS.  

- **Task:** Create a custom top navigation bar.

### **Day 6 — CSS Injection & Styling**
- **Topic:** Using `st.markdown(..., unsafe_allow_html=True)`.

- **Task:** Modify sidebar background or hide the hamburger menu via CSS.

### **Day 7 — Week 1 Project**

**Project:** Static Portfolio website with:  

- Sidebar navigation  

- Tabs for projects  

- Custom layout and CSS  

---

## **Week 2 — State, Persistence & Interactivity** 

**Goal:** Manage refresh behavior, control interactions, preserve user context.

### **Day 8 — Session State Basics**
- **Topic:** `st.session_state`.  

- **Task:** Persistent counter that doesn't reset on every interaction.

### **Day 9 — Forms & Batch Input**
- **Topic:** `st.form`, `st.form_submit_button`.  

- **Task:** User Registration form processed only on submit.

### **Day 10 — Callbacks**
- **Topic:** `on_change`, `on_click`.  

- **Task:** Celsius <--> Fahrenheit bidirectional value sync.

### **Day 11 — Persistence Level 1: Query Parameters**
- **Topic:** `st.query_params`.  

- **Task:** Maintain URL state (`?view=settings`) across refresh.

### **Day 12 — Persistence Level 2: Cookies & Local Storage**

- **Problem:** `st.session_state` dies on browser refresh.  

- **Solution:** Use `extra-streamlit-components` cookie manager.  

- **Task:** Implement simple cookie read/write.

### **Day 13 — Authentication Logic**
- **Topic:** Cookie-based session recovery.  

- **Task:** Mock login that persists after refresh.

### **Day 14 — Week 2 Project**

**Project:** Continue Portfolio App from Week_1 with:  

- Persistent tasks (session_state)  

- Cookie-based login persistence  

---

## **Week 3 — Data, Databases & Async Handling**  

**Goal:** Connect to SQL, separate backend logic, and optimize performance.

### **Day 15 — Secrets Management**
- **Topic:** `.streamlit/secrets.toml`.  

- **Task:** Securely set database credentials.

### **Day 16 — SQL Connection**
- **Topic:** `st.connection` vs SQLAlchemy.  

- **Task:** Connect to Postgres and run `SELECT *`.

### **Day 17 — Writing Data (Backend Layer)**
- **Topic:** Insert/Update logic in a separate `db_manager.py`. 

- **Task:** Create a form that inserts a new user.

### **Day 18 — Visualization Pipeline**
- **Topic:** Pandas → Plotly/Altair.  

- **Task:** Query DB, compute Moving Average, render chart.

### **Day 19 — Caching for Performance**
- **Topic:** `st.cache_data`, `st.cache_resource`. 

- **Task:** Optimize heavy SQL query.

### **Day 20 — Async & Long-Running Tasks**
- **Topic:** `st.spinner`, `st.progress`, `st.status`.  

- **Task:** Simulate 5-second data job with progress display.

### **Day 21 — Week 3 Capstone**

**Project:** Continue Portfolio App from Week_2 with : 

- SQL_connection

- Cached metrics  

- Plotly visualization

---

## **Week 4 — Security, Deployment**  

**Goal:** Validate inputs, secure queries, build authentication, and deploy.

### **Day 22 — Input Validation (Regex)**
- **Topic:** Email/password validation.  

- **Task:** Enable "Submit" only when fields match regex.

### **Day 23 — Security Best Practices**
- **Topics:**  
  - SQL Injection prevention via parameterized queries  

  - Avoiding XSS when using `unsafe_allow_html=True`  

### **Day 24 — Authentication Packages**
- **Topic:** `streamlit-authenticator` with hashed passwords (bcrypt).  

- **Task:** Implement full login system.

### **Day 25 — Fragments & Partial Reruns**
- **Topic:** `st.fragment`.  

- **Task:** Rerun only a chart instead of the entire page.

### **Day 26 — Mutability & Data Editing**
- **Topic:** `st.data_editor`.  

- **Task:** Editable table that syncs updates to DB.

### **Day 27 — Testing**
- **Topic:** `streamlit.testing` (AppTest).  

- **Task:** Script for headless UI testing.

### **Day 28 — Deployment**
- **Topic:** Streamlit Cloud vs Docker.

- **Task:** Build Dockerfile for the app.

---

## **Days 29–30 — Project: SaaS-Lite App**
**Requirements:**  

- Login/Signup (Auth + Cookies)  

- Sidebar navigation  

- SQL data input  

- Cached dashboard visualizations  

- Export report button  

---

