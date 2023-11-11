import streamlit as st
import os
from kv_audio_pipeline.audio_pipeline import AudioPipeline

st.set_page_config(
    page_title="KlangVerso - Audio Generation",
    page_icon="🔊",
)
st.markdown(
    """
    Now that we've processed the article and have made the appropriate edits, let's process the text and generate
    some audio. """
)
reader = st.radio(
    "Please Select your speaker",
    ["Davis", "Tony", "Amber", "Jenny"],
    captions=[])

audio_button = st.button('Generate Audio File.')

if audio_button:

    ap = AudioPipeline("", article_title='audio_out')
    ap.text = st.session_state['final_text']
    ap.initialize_speech_service(st.secrets["speech_api"], st.secrets["speech_region"])

    # Change reader, selected by radio buttons
    if reader=="Davis":
        ap.change_speaker('en-US-DavisNeural')
    elif reader == "Tony":
        ap.change_speaker('en-US-TonyNeural')
    elif reader == "Amber":
        ap.change_speaker('en-US-AmberNeural')
    else:
        ap.change_speaker('en-US-JennyNeural')

    # Name the article (.mp3) and generate the audio
    ap.configure_audio_output(file_name=f'{ap.article_title}.mp3')
    ap.generate_audio()

    progress_text = "Processing Audio File."

    audio_file = open(f'{ap.article_title}.mp3', 'rb')
    audio_data = audio_file.read()
    st.audio(audio_data, format='audio/mp3')
    st.download_button(label="Download Audio File",
                       data=f'{ap.article_title}.mp3',
                       file_name=f'{ap.article_title}.mp3')
