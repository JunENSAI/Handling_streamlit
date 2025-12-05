By default, Streamlit arranges elements in a single vertical column. To build dashboards or dense interfaces, you need to control the horizontal space (`st.columns`) and logical grouping (`st.container`).

## 1. The Grid System (`st.columns`)

`st.columns` allows you to split the workspace into side-by-side containers.

### Syntax
You can define columns by specifying an integer (number of columns) or a list of numbers (relative width ratios).

```python
# Option A: 3 Equal columns
col1, col2, col3 = st.columns(3)

# Option B: Custom Ratios (20% - 80%)
sidebar_col, main_col = st.columns([1, 4])
```

### Usage Patterns

Just like the Sidebar, the best way to write content into a column is using the `with` context manager.

```python
with col1:
    st.image("cat.jpg")
    st.button("Like")
```

#### Important Constraint: 
You cannot nest st.columns inside another `st.columns`. If you need a grid inside a grid, you generally have to rethink your design or use custom HTML/CSS components, although Streamlit recently relaxed this constraint slightly in specific container contexts, deep nesting is still not supported natively.

---

### 2. Logical Grouping (`st.container`)

`st.container` creates an invisible frame that holds elements together.

#### Why use a Container?

- **Logical Organization**: It keeps code clean by grouping related widgets.

- **Out-of-Order Rendering**: You can define a container at the top of your script, do some heavy computation, and then write results into that top container after the computation is finished.

- **Styling (Border)**: You can add a border to a container to visually separate a section.

```python
# Create a container with a border
stats_panel = st.container(border=True)

with stats_panel:
    st.write("This is inside a boxed container.")
```
---

## 3. Responsiveness

Streamlit layouts are responsive by default.

- **Desktop**: Columns appear side-by-side.

- **Mobile**: Columns automatically stack vertically to fit the narrow screen.

You do not need to write **@media** queries; Streamlit handles the breakpoint automatically.

### Key Takeaways for "Adjustment/Placement"

- layout="wide": In `st.set_page_config`, this is essential if you want your columns to stretch across the whole screen. Without it, your columns will be squeezed into the center.

- Ratios: Using [2, 1] means the first column takes 66% and the second 33%. This is critical for Main Content vs. Helper Content layouts.

---