import streamlit as st
import time

st.set_page_config(page_title="Forms & Batch input", layout="wide")

st.title("Interactive vs Batch Processing")

col1, col2 = st.columns(2)


with col1:
    st.header("1. Standard Input")
    st.info("Try typing in the box below. Notice the 'Running' icon top-right every time you type.")
    
    live_text = st.text_input("Type here (Live):", key="live_input") # a key is important to remember input state

    time.sleep(0.5) 
    
    st.write(f"Processed: {live_text.upper()}")

with col2:
    st.header("2. Form Input")
    st.info("Type below. Nothing happens until you click Submit.")
    
    with st.form(key="profile_form"):

        firstname = st.text_input("First Name")
        lastname = st.text_input("Last Name")
        role = st.selectbox("Job Role", ["Data scientist", "Data engineer", "Data analyst"])
        
        # The form is sealed until this is clicked
        submit_btn = st.form_submit_button(label="Create Profile")
        
    # Logic OUTSIDE the form, executed only if submitted
    if submit_btn:
        st.success("Profile Submitted!")
        st.json({
            "Full Name": f"{firstname} {lastname}",
            "Role": role,
            "Status": "Active"
        })
        
st.markdown("---")
st.subheader("Why this matters?")
st.write("""
In column 1, if you type "Hello", Streamlit runs the `time.sleep(0.5)` **5 times** (once for H, e, l, l, o). That is 2.5 seconds of waiting.
              
In column 2, you type "Hello", select a role, and click Submit. The code runs **once**.
""")