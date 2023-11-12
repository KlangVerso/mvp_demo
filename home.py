import streamlit as st


st.set_page_config(
    page_title="KlangVerso - Home",
    page_icon="👋",
)

st.title("Welcome to KlangVerso!")

if 'final_text' not in st.session_state:  # create the state_session variable if it doesn't exist
    st.session_state['final_text'] = ""

st.markdown(
    """
    At **KlangVerso**, our goal is to help digitize print media by providing image processing and text to speech capabilities to everyone. Feel free to select from the options to the left to explore some of our capabilities. 
    """
)


