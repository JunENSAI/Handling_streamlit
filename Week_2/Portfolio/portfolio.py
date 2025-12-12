import streamlit as st
import pandas as pd
import numpy as np
import time
import extra_streamlit_components as stx
import datetime 


st.set_page_config(page_title="Portfolio", layout="wide")

css_style = """
<style>
    /* Main Background */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #262730;
    }
    
    /* Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron&display=swap');
    
    h1, h2, h3, .css-10trblm {
        font-family: 'Orbitron', sans-serif !important;
        color: #00FFCC !important; /* Neon Green Title */
    }
    
    /* Buttons */
    .stButton > button {
        background-color: transparent;
        color: #00FFCC;
        border: 2px solid #00FFCC;
        border-radius: 20px;
        transition: all 0.3s ease;
        width: 100%; /* Boutons pleine largeur dans sidebar */
    }

    .stButton > button:hover {
        background-color: #00FFCC;
        color: #0E1117;
        box-shadow: 0 0 10px #00FFCC;
    } 

    /* Metrics */
    [data-testid="stMetricValue"] {
        font-size: 50px;
        color: #FF00FF; /* Neon Pink */
        font-family: 'Orbitron', sans-serif;
    }
    
    /* Inputs */
    .stTextInput > div > div > input {
        border-color: #00FFCC;
        color: white;
    }
    
    /* Cacher le menu hamburger et footer par défaut */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

cookie_manager = stx.CookieManager(key="auth_cookie_manager")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'logout_clicked' not in st.session_state:
    st.session_state['logout_clicked'] = False


def login_logic(username, password, remember_me):
    CORRECT_USER = "Junior"
    CORRECT_PASS = "streamlit_123"

    if username == CORRECT_USER and password == CORRECT_PASS:
        st.session_state['logged_in'] = True
        st.session_state['logout_clicked'] = False
        st.success("Login Successful!")
        
        if remember_me:
            expires = datetime.datetime.now() + datetime.timedelta(days=1)
            cookie_manager.set("auth_token", "valid_token_123", expires_at=expires, key="set_auth_token")
        
        time.sleep(1)
        st.rerun()
    else:
        st.error("Incorrect username or password")

def logout_logic():
    st.session_state['logout_clicked'] = True
    st.session_state['logged_in'] = False

    try:
        cookie_manager.delete("auth_token")
    except KeyError:
        pass

    with st.sidebar:
        st.spinner("Logging out...")
    
    time.sleep(1)
    st.rerun()

if not st.session_state['logged_in'] and not st.session_state['logout_clicked']:
    auth_token = cookie_manager.get("auth_token")
    if auth_token == "valid_token_123":
        st.session_state['logged_in'] = True
    else:
        time.sleep(0.1)


def show_login_page():
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        st.title("Locked Area")
        st.markdown("### Portfolio Access")
        
        with st.form("login_form"):
            user = st.text_input("Username")
            pwd = st.text_input("Password", type="password")
            remember = st.checkbox("Remember Me", value=True)
            
            st.markdown("---")
            submitted = st.form_submit_button("Log In")
        
        if submitted:
            login_logic(user, pwd, remember)
        
        st.info("Logins: Junior / streamlit_123")


def show_main_app():
    with st.sidebar:
        st.title("👤 User Profile")
        st.write(f"User: **Junior**")
        st.caption(f"Method: {'Cookie' if cookie_manager.get('auth_token') else 'Session '}")
        
        st.markdown("---")
        if st.button("Log Out"):
            logout_logic()

    tab_btc, tab_doge, tab_eth = st.tabs(["Bitcoin", "Dogecoin", "Ethereum"])

    with tab_btc:
        st.header("Bitcoin Analysis")
        
        col1, col2 = st.columns(2)
        col1.metric("Rate","345/365","5%")
        col2.metric("New actions", "14", "-2%")
        
        st.markdown("### Trend Analysis")
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Yahoo", "Bloomberg", "WallSt"])
        st.area_chart(chart_data)

        with st.expander("View Methodological Note"):
            st.write("The analysis is based on historical price data.")

    with tab_doge:
        st.header("Dogecoin Financials")
        dogecoin_data = pd.DataFrame({
            "Source": ["Investors", "Exchanges", "Merchants"],
            "Allocated": [30000, 15000, 5000],
            "Spent": [25000, 10000, 2000]
        })
        st.bar_chart(dogecoin_data.set_index("Source"), width='stretch')

    with tab_eth: 
        st.header("Ethereum Financials")
        ethereum_data = pd.DataFrame({
            "Source": ["Investors", "Exchanges", "Merchants"],
            "Allocated": [1200, 1500, 5000],
            "Spent": [250, 1000, 2200]
        })
        st.line_chart(ethereum_data.set_index("Source"), width='stretch')

if st.session_state['logged_in']:
    show_main_app()
else:
    show_login_page()