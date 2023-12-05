import streamlit as st
import streamlit_authenticator as stauth

st.set_page_config(
    page_title="KlangVerso - Home",
    page_icon="👋",
)

st.title("Welcome to KlangVerso!")

if 'final_text' not in st.session_state:  # create the state_session variable if it doesn't exist
    st.session_state['final_text'] = ""
# Add session state variables for Authentication
if 'name' not in st.session_state: st.session_state.name = ""
if 'auth_status' not in st.session_state: st.session_state.auth_status = None
if 'username' not in st.session_state: st.session_state.username = ""

st.markdown(
    """
    At **KlangVerso**, our goal is to help digitize print media by providing image processing and text to speech 
    capabilities to everyone. Feel free to select from the options to the left to explore some of our capabilities.
    
    Please log in to continue: 
    """
)
authenticator = stauth.Authenticate(
    dict(st.secrets['credentials']),
    st.secrets['cookie']['name'],
    st.secrets['cookie']['key'],
    st.secrets['cookie']['expiry_days']
)
name, authentication_status, username = authenticator.login('Login', 'main')

st.session_state.name = name
st.session_state.auth_status = authentication_status
st.session_state.username = username

if st.session_state.auth_status:
    st.write(f'Welcome back *{st.session_state["name"]}*! Please feel free to explore the other features.')
    authenticator.logout('Logout', 'main', key='unique_key')

elif authentication_status == None:
    st.warning('Please enter your username and password')
else:
    st.error('Username/password is incorrect')
