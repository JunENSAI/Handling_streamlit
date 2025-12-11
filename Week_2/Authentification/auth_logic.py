import streamlit as st
import extra_streamlit_components as stx
import time
import datetime 

st.set_page_config(page_title="Secure Login")


cookie_manager = stx.CookieManager(key="auth_cookie_manager")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'logout_clicked' not in st.session_state:
    st.session_state['logout_clicked'] = False

def login_logic(username, password, remember_me):
    CORRECT_USER = "admin"
    CORRECT_PASS = "streamlit123"

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
    
    cookie_manager.delete("auth_token")
    
    st.spinner("Logging out...")
    time.sleep(1)
    st.rerun()

if not st.session_state['logged_in'] and not st.session_state['logout_clicked']:
    
    auth_token = cookie_manager.get("auth_token")
    if auth_token == "valid_token_123":
        st.session_state['logged_in'] = True
    else:
        pass

def show_login_page():
    st.title("Locked Area")
    st.write("Please log in.")
    
    with st.form("login_form"):
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        remember = st.checkbox("Remember Me", value=True)
        submitted = st.form_submit_button("Log In")
    
    if submitted:
        login_logic(user, pwd, remember)

def show_main_app():
    st.title("Welcome, Admin!")
    st.sidebar.success("Logged In")

    st.info(f"You are logged in via: {'Cookie' if cookie_manager.get('auth_token') else 'Session'}")
    
    if st.button("Log Out"):
        logout_logic()

if st.session_state['logged_in']:
    show_main_app()
else:
    show_login_page()