import streamlit as st
import pandas as pd
import numpy as np

# layout="centered" : Centers the content of the Streamlit app on the page (instead of stretching it full width).

st.set_page_config(page_title="Tabs & Expanders", layout="centered")

st.title("Team Dashboard")

tab_overview, tab_budget, tab_team = st.tabs(["Overview", "Budget", "Team"]) # Create three tabs (Overview, Budget, Team) which contain different sections of the dashboard

# st.expander : A collapsible container that can hide or show its content when clicked (like a information box that can be expanded or collapsed).

with tab_overview:
    st.header("Project Status")
    st.success("Current Phase: Development") # Display a success message indicating the current project phase (so maybe in a dynamic dashboard this could change based on project status)
    
    col1, col2 = st.columns(2)
    col1.metric("Tasks Completed", "12/50", "2")
    col2.metric("Days Remaining", "14", "-2")
    
    st.markdown("### Weekly Progress")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Design", "Dev", "Test"])
    st.area_chart(chart_data) # Display an area chart showing progress in different phases

    with st.expander("View Methodological Note"):
        st.write("""
        The progress is calculated based on Jira tickets moved to 'Done'.
        The 'Design' phase includes UX and UI tasks.
        """)

with tab_budget:
    st.header("Financials")
    
    budget_data = pd.DataFrame({
        "Department": ["R&D", "Marketing", "HR", "Legal"],
        "Allocated": [50000, 20000, 15000, 5000],
        "Spent": [45000, 12000, 14000, 1000]
    })

    st.bar_chart(budget_data.set_index("Department"))

    with st.expander("Click to see raw budget data"):
        st.dataframe(budget_data, width=True)
        st.caption("Data source: Finance_Q3.csv")

with tab_team:
    st.header("Team Allocation")
    
    team_members = ["Alice (Lead)", "Bob (Dev)", "Charlie (Design)"]

    for member in team_members:
        with st.expander(member): # Create an expander for each team member (contain their details)
            st.write(f"Contact: {member.split()[0].lower()}@company.com")
            st.button(f"Email {member.split()[0]}", key=member)