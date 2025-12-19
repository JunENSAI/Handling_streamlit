import streamlit as st
import extra_streamlit_components as stx
import time

st.set_page_config(page_title="Cookies")

st.title("Browser Persistence Demo")

# --- 1. SETUP COOKIE MANAGER ---
cookie_manager = stx.CookieManager()

st.info("This app uses browser cookies. If you refresh the page, the data persists.")

# --- 2. FETCH CURRENT COOKIE ---
cookie_value = cookie_manager.get(cookie="username")

# --- 3. UI LOGIC ---

if cookie_value:

    st.success(f"Welcome back, **{cookie_value}**!")
    st.write("I remember you because I read your cookie.")
    
    if st.button("Logout (Delete Cookie)"):
        cookie_manager.delete("username")

        st.spinner("Logging out...")
        time.sleep(1)

        st.rerun()

else:
    st.warning("I don't know who you are. (No Cookie Found)")
    
    with st.form("login_form"):
        user_input = st.text_input("Enter your name to save:")
        submitted = st.form_submit_button("Save to Cookie")
        
    if submitted and user_input:

        cookie_manager.set("username", user_input)
        
        st.success("Cookie sent to browser! Refreshing...")
        time.sleep(1)
        st.rerun()

with st.expander("Debug: View All Cookies"):
    st.write(cookie_manager.get_all())