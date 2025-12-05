import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="Topbar",
    #page_icon="", : you can add an icon here (for your browser tab or app icon) , it prints in the top left corner of the app
    layout="wide"
)

# Custom CSS to hide Streamlit default elements

st.markdown("""
<style>
    .reportview-container {
        margin-top: -2em;
    }
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    #stDecoration {display:none;}
</style>
""", unsafe_allow_html=True)

# Top navigation bar : horizontal menu

selected = option_menu(
    menu_title=None,
    options=["Home", "Upload", "Analytics", "Settings"],
    icons=["house", "cloud-upload", "graph-up-arrow", "gear"], #icon names from https://icons.getbootstrap.com/
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#f5f5f5"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#4CAF50"},
    }
)

if selected == "Home":
    st.title(f"You have selected {selected}")
    st.write("Welcome to the homepage.")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=300)


elif selected == "Upload":
    st.title("Data Upload")
    st.file_uploader("Drop your CSV here", type=["csv"]) # Allow only CSV files

elif selected == "Analytics":
    st.title("Dashboard")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Sales", "100K", "5%")
    with col2:
        st.metric("Profit", "20K", "-2%")

elif selected == "Settings":
    st.title("Configuration")
    st.text_input("API Key", type="password") # Hide input for sensitive data (type = password)
    st.button("Save Config")