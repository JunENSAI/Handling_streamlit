import streamlit as st

st.set_page_config(page_title="Callbacks")

st.title("Bidirectional Sync (Callbacks)")

# --- 1. INITIALIZE STATE ---

if "celsius" not in st.session_state:
    st.session_state.celsius = 0.0

if "fahrenheit" not in st.session_state:
    st.session_state.fahrenheit = 32.0

# --- 2. DEFINE CALLBACK FUNCTIONS ---

def update_from_celsius():
    """
    User changed Celsius. We calculate F and update state.
    """
    c = st.session_state.celsius
    st.session_state.fahrenheit = (c * 9/5) + 32

def update_from_fahrenheit():
    """
    User changed Fahrenheit. We calculate C and update state.
    """
    f = st.session_state.fahrenheit
    st.session_state.celsius = (f - 32) * 5/9

def reset_values():
    """
    Reset both to zero.
    """
    st.session_state.celsius = 0.0
    st.session_state.fahrenheit = 32.0

# --- 3. UI LAYOUT ---

col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    st.number_input(
        "Celsius (°C)",
        key="celsius",
        step=1.0,
        on_change=update_from_celsius
    )

with col2:
    st.number_input(
        "Fahrenheit (°F)",
        key="fahrenheit",
        step=1.0,
        on_change=update_from_fahrenheit
    )

with col3:
    st.write("##") # Spacer
    st.button("Reset", on_click=reset_values)


st.markdown("---")
st.write("Current Session State:")
st.json(st.session_state)