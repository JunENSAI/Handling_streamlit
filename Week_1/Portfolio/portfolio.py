import streamlit as st
import pandas as pd
import numpy as np
import time


st.set_page_config(page_title="Portfolio", layout="centered")

# Custom CSS to modify aspects of the Streamlit app

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


st.title("Portfolio Dashboard")
st.markdown("This app is just to highlight your vision about all you have learned during this week.")

with st.sidebar:
    st.header("1.Login")
    username = st.text_input("Username", value="User")
    st.button("Connect")


    mode = st.radio("Choose your assess", ["Bitcoin", "Dogecoin", "Ethereum"])
    
    st.markdown("---")
    st.header("2. Actions")
    
    run_btn = st.button("OK")

st.subheader(f"Welcome, {username}!")

tab_bitcoin, tab_dogecoin, tab_ethereum = st.tabs(["Bitcoin", "Dogecoin", "Ethereum"])


if run_btn:

    with st.spinner(f"Running {mode}..."):
        time.sleep(1.5)
        
    if mode == "Bitcoin":
        with tab_bitcoin:
            st.header("Bitcoin Analysis")
            
            col1, col2 = st.columns(2)
            col1.metric("Rate","345/365","5%")
            col2.metric("New actions", "14", "-2%")
            
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["yahoo", "bloomberg", "wallstreet"])
            st.area_chart(chart_data)

            with st.expander("View Methodological Note"):
                st.write("""
                The analysis is based on historical price data from major financial news sources.
                The metrics reflect current market trends and user activity.
                """)
        st.success("Bitcoin Computation Complete!")
    elif mode == "Dogecoin":
        with tab_dogecoin:
            st.header("Dogecoin Financials")
            
            dogecoin_data = pd.DataFrame({
                "Source": ["Investors", "Exchanges", "Merchants"],
                "Allocated": [30000, 15000, 5000],
                "Spent": [25000, 10000, 2000]
            })

            st.bar_chart(dogecoin_data.set_index("Source"))

            with st.expander("Click to see raw budget data"):
                st.dataframe(dogecoin_data, width=True)
                st.caption("Data source: Crypto_Finance_Q3.csv")
        st.success("Dogecoin Computation Complete!")
        st.info("Result: Moderate volatility observed.")
    else:  # Ethereum
        with tab_ethereum:
            st.header("Ethereum Financials")
            
            ethereum_data = pd.DataFrame({
                "Source": ["Investors", "Exchanges", "Merchants"],
                "Allocated": [1200, 1500, 5000],
                "Spent": [250, 1000, 2200]
            })

            st.line_chart(ethereum_data.set_index("Source"))

            with st.expander("Click to see raw budget data"):
                st.dataframe(ethereum_data, width=True)
                st.caption("Data source: Crypto_Finance_Q4.csv")
        st.success("Ethereum Computation Complete!")
        st.info("Result: High volatility observed.")
