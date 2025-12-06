Streamlit does not have a "Style Editor." To change the look and feel, we use `st.markdown` with the `unsafe_allow_html=True` parameter. This allows us to write raw `<style>` blocks that the browser interprets.

## 1. The Mechanism

```python
st.markdown("""
    <style>
        /* Your CSS goes here */
        p {
            color: red;
        }
    </style>
""", unsafe_allow_html=True)
```

## 2. Targeting Streamlit Elements

Streamlit's HTML is complex and class names can be auto-generated (e.g., **css-1d391kg**). However, there are stable ways to target key areas using Attribute Selectors (data-testid).

| Target            | CSS Selector                      | Description                                               |
|-------------------|-----------------------------------|-----------------------------------------------------------|
|Main background    | `.stApp`                          | The main container of the application                     |
|Sidebar            |[data-testid=""stSidebar""]        | The sidebar container                                     |
|Header             |header                             |The top colored decoration bar                             |
|Buttons            | `.stButton` > button              |Targeting the button element inside Streamlit's wrapper    |
|Metrics            |[data-testid=""stMetricValue""]    |The big number in a metric widget                          |

---

## 3. Importing Fonts

You can load fonts from Google Fonts just like in standard web development.

```css
@import url('[https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap](https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap)');

html, body, [class*="css"]  {
    font-family: 'Roboto', sans-serif;
}
```

---

## 4. Limitations

- **No Scoped CSS:** CSS injected this way is global. It affects the entire page.

- **Fragility:** If Streamlit updates their internal HTML structure, your CSS might break. Always test after upgrading the Streamlit library.

### Key Takeaways for "Graphic Handling" (Visuals)

- `!important:` You will often need to use this CSS tag (e.g., `color: red !important;`) to force your style to override Streamlit's specific default styles.

- **Inspect Element:** To find what to style, right-click your running Streamlit app in the browser, select "Inspect", and look for the class names or data-testid attributes.

---

