import streamlit as st
import pandas as pd
import numpy as np
import time


st.set_page_config(page_title="Portfolio ", layout="centered")

css_style = """
<style>
    .stApp { background-color: #0E1117; }
    [data-testid="stSidebar"] { background-color: #262730; }
    .stButton > button {
        background-color: transparent; color: #00FFCC; border: 2px solid #00FFCC; border-radius: 20px;
    }
    .stButton > button:hover {
        background-color: #00FFCC; color: #0E1117;
    } 
    [data-testid="stMetricValue"] { color: #FF00FF; font-size: 50px; }
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# --- 1. INITIALIZE SESSION STATE ---
# We need to remember TWO things:
# 1. Has the user clicked "OK"?
# 2. What crypto mode was selected when they clicked "OK"?

if 'data_loaded' not in st.session_state:
    st.session_state['data_loaded'] = False

if 'active_mode' not in st.session_state:
    st.session_state['active_mode'] = None


# --- SIDEBAR ---
with st.sidebar:
    st.header("1.Login")
    # Adding a key automatically saves this to session_state
    username = st.text_input("Username", value="User", key="user_name") 
    st.button("Connect")

    # The user selects a mode, but we don't lock it in until they click OK
    current_selection = st.radio("Choose your asset", ["Bitcoin", "Dogecoin", "Ethereum"])
    
    st.markdown("---")
    
    # When this button is clicked, we UPDATE the state
    if st.button("OK"):
        st.session_state['data_loaded'] = True
        st.session_state['active_mode'] = current_selection


st.subheader(f"Welcome, {st.session_state.user_name}!")

tab_bitcoin, tab_dogecoin, tab_ethereum = st.tabs(["Bitcoin", "Dogecoin", "Ethereum"])

if st.session_state['data_loaded']:
    
    # We use the SAVED mode (active_mode), not the currently selected radio button (current_selection).
    # This prevents the graph from changing immediately if the user just clicks the radio button without clicking OK.
    mode = st.session_state['active_mode']

    if mode == "Bitcoin":
        with tab_bitcoin:
            st.header("Bitcoin Analysis")
            col1, col2 = st.columns(2)
            col1.metric("Rate","345/365","5%")
            col2.metric("New actions", "14", "-2%")
            
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["yahoo", "bloomberg", "wallstreet"])
            st.area_chart(chart_data)

            # NOW TRY CLICKING THIS: It won't disappear!
            with st.expander("View Methodological Note"):
                st.write("""
                The analysis is based on historical price data.
                The metrics reflect current market trends.
                """)
                
    elif mode == "Dogecoin":
        with tab_dogecoin:
            st.header("Dogecoin Financials")
            dogecoin_data = pd.DataFrame({
                "Source": ["Investors", "Exchanges", "Merchants"],
                "Allocated": [30000, 15000, 5000],
                "Spent": [25000, 10000, 2000]
            })
            st.bar_chart(dogecoin_data.set_index("Source"))
            
    else: 
        with tab_ethereum:
            st.header("Ethereum Financials")
            ethereum_data = pd.DataFrame({
                "Source": ["Investors", "Exchanges", "Merchants"],
                "Allocated": [1200, 1500, 5000],
                "Spent": [250, 1000, 2200]
            })
            st.line_chart(ethereum_data.set_index("Source"))
            
    if st.button("Reset Analysis"):
        st.session_state['data_loaded'] = False
        st.rerun()

else:
    st.info("select an asset and click 'OK' in the sidebar.")