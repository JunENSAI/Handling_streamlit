import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(layout="wide", page_title="Columns and Containers")

st.title("Executive Dashboard") # Title of the dashboard (on the main area)
st.markdown("modify the column widths using the sidebar sliders")

with st.sidebar:
    """ 
    You can adjust the layout of the dashboard using the sliders below.

    The left column displays charts, while the right column shows system logs.

    When you adjust the widths, the changes will reflect immediately on the main page.
    """

    st.header("Settings")

    left_width = st.slider("Left Column Width", 1, 5, 2)
    right_width = st.slider("Right Column Width", 1, 5, 3)


st.subheader("Daily Metrics")

kpi1, kpi2, kpi3, kpi4 = st.columns(4) #create 4 equal-width columns

# st.metric displays a number with optional delta. So when you affect a negative delta to a metric, it will be shown in red.

with kpi1:
    st.metric(label="Total Revenue", value="$1,000", delta="12%") 
with kpi2:
    st.metric(label="New Users", value="20", delta="-2%")
with kpi3:
    st.metric(label="Bounce Rate", value="15%", delta="0.5%", delta_color="inverse")
with kpi4:
    if st.button("Refresh Data"):
        st.toast("Data refreshed!")

st.markdown("---")

col_charts, col_logs = st.columns([left_width, right_width]) #create 2 columns with adjustable widths (via the sidebar sliders)

with col_charts:
    with st.container(border=True):
        st.subheader("Sales Performance")

        # Generate random sales data
 
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['Product A', 'Product B', 'Product C']
        )
        
        st.line_chart(chart_data)
        st.caption("Figure 1: Sales trends over the last 20 days.")

with col_logs:
    # create a container for all of the logs (with a border).
    with st.container(border=True):
        st.subheader("System Logs")
        st.info("10:00 AM - Server started")
        st.warning("10:05 AM - High latency detected") # the color of the warning message is yellow
        st.error("10:15 AM - Connection timeout (User #99)") # the color of the error message is red
        st.success("10:20 AM - Issue resolved") # the color of the success message is green
        
        status_holder = st.container()

        time.sleep(1)

        with status_holder:
            st.write(" **Ok after 10:20 AM**")