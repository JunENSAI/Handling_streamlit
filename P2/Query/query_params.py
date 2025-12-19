import streamlit as st

st.set_page_config(page_title="URL Persistence")

st.title("Deep Linking Demo")

query_params = st.query_params
initial_view = query_params.get("view", "Home") # Default to "Home" if not specified

options = ["Home", "Search", "Settings"]

try:
    default_index = options.index(initial_view)
except ValueError:
    default_index = 0


# Sidebar Navigation
selected_nav = st.sidebar.radio("Navigation", options, index=default_index)

# Update the URL query parameters based on the selected navigation
if selected_nav != initial_view:
    st.query_params["view"] = selected_nav


if selected_nav == "Home":
    st.header("Home Page")
    st.write("Welcome! Look at the URL bar. It says `?view=Home`.")

elif selected_nav == "Search":
    st.header("Search Page")

    initial_query = query_params.get("query", "")

    def update_search_url():
        st.query_params["query"] = st.session_state.search_box
        st.query_params["view"] = "Search"

    search_term = st.text_input(
        "Search Database", 
        value=initial_query, 
        key="search_box",
        on_change=update_search_url
    )
    
    if search_term:
        st.write(f"Results for: **{search_term}**")
        st.write(f"if you cope the like below you see your search is persisted on the page reload:")
        st.code(f"http://localhost:8501/?view=Search&query={search_term}")

elif selected_nav == "Settings":
    st.header(" Settings")
    st.write("Nothing to configure here yet.")