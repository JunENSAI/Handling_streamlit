As your application grows, you will run out of screen space. **Tabs** and **Expanders** allow you to group content logically and hide secondary information, keeping the UI clean.

## 1. Tabs (`st.tabs`)

Tabs create a horizontal navigation bar within your page. They are perfect for switching between different "contexts" or "views" of the same data without reloading the entire page layout.

### Syntax
`st.tabs` returns a list of container objects. You unpack them into variables.

```python
# define the labels
tab_titles = ["📈 Chart", "📄 Data", "⚙️ Settings"]
tab1, tab2, tab3 = st.tabs(tab_titles)

# Content for Tab 1
with tab1:
    st.header("Visual Analysis")
    st.line_chart([1, 2, 3])

# Content for Tab 2
with tab2:
    st.dataframe({"Data": [1, 2, 3]})
```

### Performance Note

Streamlit executes all the code inside every tab every time the script reruns, even if the tab is not currently visible.

- **Good:** Fast switching between tabs (content is pre-loaded).

-**Bad:** If you have heavy queries in Tab 2, the app will be slow even if the user is looking at Tab 1.

- **Fix:** Use conditional logic (if specific checks) or standard Python optimization if this becomes an issue.

---

## 2. Expanders (`st.expander`)

Expanders are collapsible containers. They are "closed" by default but can be toggled open by the user.

Use Cases

- **Documentation**: "How to use this app?"

- **Raw Data**: Showing the dataframe behind a chart.

- **Advanced Settings**: Options that 90% of users don't need to touch.

```python
# Basic usage
with st.expander("See explanation"):
    st.write("Here is the detailed explanation...")

# Default to open
with st.expander("Important Notice", expanded=True):
    st.warning("Please read this first!")
```

---

## 3. Nesting Strategy

You can combine these layouts to create complex interfaces.

- **Sidebar > Expander**: Great for grouping filters.

- **Tab > Column > Expander**: A highly organized dashboard.

### Key Takeaways for "Handling Tabs"

- **State Preservation:** If you interact with a widget in Tab 1 (e.g., click a button), Streamlit reruns. It remembers which tab was active and keeps you there. You don't need to manually handle "active tab" state.

- **Visual Hierarchy:** Always put the st.tabs call outside the with blocks. You create the containers first, then fill them.

---