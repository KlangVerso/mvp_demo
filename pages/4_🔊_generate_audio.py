import streamlit as st
import requests
import os
from kv_audio_pipeline.audio_pipeline import AudioPipeline

st.set_page_config(
    page_title="KlangVerso - Audio Generation",
    page_icon="🔊",
)

if st.session_state.auth_status:

    st.markdown(
        """
        Now that we've processed the article and have made the appropriate edits, we will generate your audio. 
        """
    )

    CHUNK_SIZE = 1024

    reader = st.radio(
        "Please Select your speaker",
        ["Natasha", "Hades", "Oswald", "Sally", 'Readwell', 'Bob'])

    lookup = {"Natasha": '4FBBpmx622VobH9OdpgF',
              "Hades": 'DJbOYlp8OGXMXhVoUq9P',
              "Oswald": 'JpgaTdf1skAcigpNBjTi',
              "Sally": 'l87cDE0TXiy9JBLtsHco',
              "Readwell": 'lHWbfJgUCFayYFtgQfwX',
              "Bob": 'vg2Cu0P5DjGx26Zbt1rf'}

    audio_button = st.button('Generate Audio File.')

    if audio_button:

        url = f"https://api.elevenlabs.io/v1/text-to-speech/{lookup[reader]}"

        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": f"{st.secrets['speech']['eleven_labs_api']}",
        }

        data = {
            "text": f"{st.session_state.text}",
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }

        response = requests.post(url, json=data, headers=headers)
        with open(f'{st.session_state.file_name}.mp3', 'wb') as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
            f.close()

        st.audio(f'{st.session_state.file_name}.mp3')
        st.download_button(label="Download Audio File",
                           data=f'{st.session_state.file_name}.mp3',
                           file_name=f'{st.session_state.file_name}.mp3')

else:  # User not authenticated
    st.warning('Please log in to access this feature.')
