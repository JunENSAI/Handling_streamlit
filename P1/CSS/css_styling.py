import streamlit as st

st.set_page_config(page_title="Styling", layout="centered")

# --- CSS INJECTION ---
# We define a large string containing the CSS
css_style = """
<style>
    /* 1. Main Background - Dark Blue */
    .stApp {
        background-color: #0E1117;
    }
    
    /* 2. Sidebar - Slightly Lighter */
    [data-testid="stSidebar"] {
        background-color: #262730;
    }
    
    /* 3. Custom Font (Importing from Google) */
    @import url('[https://fonts.googleapis.com/css2?family=Orbitron&display=swap](https://fonts.googleapis.com/css2?family=Orbitron&display=swap)');
    
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif !important;
        color: #00FFCC !important; /* Neon Green Title */
    }
    
    /* 4. Styling Buttons */
    /* We target the button inside the stButton div */
    .stButton > button {
        background-color: transparent;
        color: #00FFCC;
        border: 2px solid #00FFCC;
        border-radius: 20px;
        transition: all 0.3s ease;
    }

    /* Hover effect for buttons : it when you pass your mouse on the connect bouton it produces a color change */
    
    .stButton > button:hover {
        background-color: #00FFCC;
        color: #0E1117;
        box-shadow: 0 0 10px #00FFCC;
    } 

    /* 5. Customizing Metrics */
    [data-testid="stMetricValue"] {
        font-size: 50px;
        color: #FF00FF; /* Neon Pink */
        font-family: 'Orbitron', sans-serif;
    }
    
    /* 6. Custom Border for Input fields */
    .stTextInput > div > div > input {
        border-color: #00FFCC;
    }
</style>
"""

st.markdown(css_style, unsafe_allow_html=True)


st.title("CYBER-DASH 2077")
st.markdown("This app demonstrates advanced CSS styling to override Streamlit defaults.")

with st.sidebar:
    st.header("System Access")
    st.text_input("Netrunner ID")
    st.button("Connect")

col1, col2 = st.columns(2)

with col1:
    st.metric(label="System Integrity", value="98%", delta="Stable")

with col2:
    st.metric(label="Network Load", value="45 TB", delta="-12%")

st.subheader("Data Stream")
st.button("Initiate Override")

with st.expander("View System Logs"):
    st.write("Log entry 001: Connection established.")
    st.write("Log entry 002: CSS injection successful.")