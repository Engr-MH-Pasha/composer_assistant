import streamlit as st

def check_password():
    """Returns True if the user has a verified session, False otherwise."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.username = ""

    if st.session_state.authenticated:
        return True

    # Render login inputs in sidebar
    st.sidebar.title("🔐 Login Portal")
    user_id = st.sidebar.text_input("User ID", key="login_user")
    password = st.sidebar.text_input("Password", type="password", key="login_pass")

    if st.sidebar.button("Sign In", use_container_width=True):
        users_config = st.secrets.get("users", {})
        if user_id in users_config and users_config[user_id] == password:
            st.session_state.authenticated = True
            st.session_state.username = user_id
            st.rerun()
        else:
            st.sidebar.error("Invalid User ID or Password")

    return False

def render_logout():
    """Renders user info and logout button once authenticated."""
    st.sidebar.markdown(f"**Logged in as:** `{st.session_state.username}`")
    if st.sidebar.button("Log Out", use_container_width=True):
        st.session_state.authenticated = False
        st.session_state.username = ""
        st.rerun()