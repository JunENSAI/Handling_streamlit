# Handling_streamlit
Learn to build a reactive dashboard with streamlit. Through all component that must be required on a project.

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
**Project:** Multi-page To-Do List App with:  
- Persistent tasks (session_state)  
- Cookie-based login persistence  

---