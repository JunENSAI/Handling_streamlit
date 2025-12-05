import streamlit as st
import time

st.set_page_config(page_title="Sidebar", layout="wide")

st.title("Day 2: The Sidebar & Main Area")
st.markdown("---")

# Sidebar configuration : so it's the place that you set up what you want to see on the left side of your web app.
with st.sidebar:

    """ st.header(1. Control Panel) : => You see on the left side of your web app a header with the text 1. Control Panel

    st.text_input("Username", value="User") : => You see on the left side of your web app a text input box with the label Username and a default value User

    st.radio("Choose Mode", ["Light Analysis", "Heavy Computation"]) : => You see on the left side of your web app a radio button with the label Choose Mode and two options Light Analysis and Heavy Computation

    st.markdown("---") : => You see on the left side of your web app a horizontal line that separates the sections

    st.button("Run") : => You see on the left side of your web app a button with the label Run
    
    """
    st.header("1. Control Panel")
    st.write("This is the setup area.")

    username = st.text_input("Username", value="User")

    mode = st.radio("Choose Mode", ["Light Analysis", "Heavy Computation"])
    
    st.markdown("---")
    st.header("2. Actions")
    
    run_btn = st.button("Run")



st.subheader(f"Welcome, {username}!")

if run_btn:

    """

    when st.button("Run") is clicked, the following happens in the main area:

    A spinner appears with the message Running {mode}..., simulating a process that takes 1.5 seconds.

    After the process completes, a success message is displayed indicating the completion of the selected mode.

    Depending on the selected mode, an info or warning message is shown with the result of the analysis.

    Finally, a JSON object is displayed summarizing the user's input and the status of the operation.

    """

    with st.spinner(f"Running {mode}..."):
        time.sleep(1.5)
        
    if mode == "Light Analysis":
        st.success("Light Analysis Complete!")
        st.info("Result: The system is stable.")
    else:
        st.success("Heavy Computation Complete!")
        st.warning("Result: High load detected, but calculations finished.")
        
    st.json({
        "User": username,
        "Mode": mode,
        "Status": "Finished"
    })
else:

    st.info("Please configure the settings in the sidebar and click 'Run'.")

st.sidebar.markdown("---")
st.sidebar.caption("Streamlit sidebar and main area")