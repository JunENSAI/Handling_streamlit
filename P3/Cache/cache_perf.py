import streamlit as st
import pandas as pd
import time
import extra_streamlit_components as stx
import datetime
import plotly.express as px
import plotly.graph_objects as go

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


@st.cache_data(show_spinner=True)
def generate_complex_prediction(coin_name):
    """Simulates a heavy AI processing task."""
    time.sleep(3) # Simulate 3 seconds of heavy math
    
    # Simple logic just for demo
    if coin_name == "Bitcoin":
        return "BULLISH (Confidence: 87%)"
    elif coin_name == "Dogecoin":
        return "VOLATILE (Confidence: 45%)"
    else:
        return "STABLE (Confidence: 92%)"

def login_logic(username, password, remember_me):

    try:
        CORRECT_USER = st.secrets["auth"]["username"]
        CORRECT_PASS = st.secrets["auth"]["password"]
    except FileNotFoundError:
        st.error("Secrets file not found! Please create .streamlit/secrets.toml")
        return

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

from sqlalchemy import text

def show_main_app():

    conn = st.connection("portfolio_db", type="sql")

    # --- SIDEBAR ---
    with st.sidebar:
        st.title("User Profile")
        st.write(f"User: **{st.secrets['auth']['username']}**")
        st.caption(f"Method: {'Cookie' if cookie_manager.get('auth_token') else 'Session'}")
        st.markdown("---")
        if st.button("Log Out"):
            logout_logic()

    tab_btc, tab_doge, tab_eth = st.tabs(["Bitcoin", "Dogecoin", "Ethereum"])

    # TAB BITCOIN (READ + WRITE)

    with tab_btc:
        st.header("Bitcoin Analysis")
        
        # 1. FETCH
        df_btc = conn.query("SELECT * FROM bitcoin", ttl=600)
        
        if not df_btc.empty:
            # 2. PROCESS
            df_btc['date'] = pd.to_datetime(df_btc['date'])
            df_btc = df_btc.sort_values('date')
            
            # Calculate a 7-day Moving Average (Trend)
            df_btc['MA_7'] = df_btc['price'].rolling(window=2).mean()
            
            # Calculate simple metrics
            latest_price = df_btc.iloc[-1]['price']
            prev_price = df_btc.iloc[-2]['price'] if len(df_btc) > 1 else latest_price
            delta = ((latest_price - prev_price) / prev_price) * 100
            
            # 3. DISPLAY METRICS
            col1, col2, col3 = st.columns(3)
            col1.metric("Latest Price", f"${latest_price:,.2f}", f"{delta:.2f}%")
            col2.metric("Highest Price", f"${df_btc['price'].max():,.2f}")
            col3.metric("Lowest Price", f"${df_btc['price'].min():,.2f}")
            
            # 4. BUILD PLOTLY CHART (Graphic Handling)
            fig = go.Figure()

            # Layer 1: The Area Chart (Raw Price)
            fig.add_trace(go.Scatter(
                x=df_btc['date'], 
                y=df_btc['price'],
                mode='lines',
                name='Daily Price',
                fill='tozeroy',
                line=dict(color='#00FFCC')
            ))

            # Layer 2: The Line Chart (Moving Average)
            fig.add_trace(go.Scatter(
                x=df_btc['date'], 
                y=df_btc['MA_7'],
                mode='lines',
                name='Moving Avg (Trend)',
                line=dict(color='#FF00FF', width=3, dash='dot')
            ))

            fig.update_layout(
                title="Price vs Trend",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=True, gridcolor='#333'),
                hovermode="x unified"
            )

            # 5. RENDER
            st.plotly_chart(fig, width='stretch')

            st.markdown("---")
            st.subheader("AI Prediction Model")
            
            st.info("The first time you click this, it will take 3 seconds. The second time, it will be instant.")
            
            if st.button("Generate AI Report"):
                result = generate_complex_prediction("Bitcoin")
                st.success(f"AI Prediction: {result}")

        else:
            st.warning("No data found.")

    with tab_doge:
        st.header("Dogecoin Financials")
        df_doge = conn.query("SELECT * FROM dogecoin", ttl=600)
        st.bar_chart(
            df_doge.set_index("source")[["allocated", "spent"]],
            width='stretch'
        )

    with tab_eth:
        st.header("Ethereum Financials")
        df_eth = conn.query("SELECT * FROM ethereum", ttl=600)
        st.line_chart(
            df_eth.set_index("source")[["allocated", "spent"]],
            width='stretch'
        )

if st.session_state['logged_in']:
    show_main_app()
else:
    show_login_page()
