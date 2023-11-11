import streamlit as st
import os
import kv_text_processing.img_to_text as itt

st.set_page_config(
    page_title="KlangVerso - Processing Text",
    page_icon="📝",
)
st.markdown(
    """
    Select the article that you would like to perform OCR on. You will have the option to modify the text to ensure
    that the text-to-speech functionality matches your expectations."""
)


def file_selector(folder_path='.'):
    files = []
    for file in os.listdir(folder_path):
        if file.endswith('.png'):
            files.append(file)
    if len(files)>=1:
        selected_filename = st.selectbox('Select a file', files)
        return os.path.join(folder_path, selected_filename)
    else:
        return "No Files Available"


filename = file_selector()
perf_ocr = st.button('Process My Article', key='perform_ocr')
if perf_ocr:
    article_txt = itt.extract_text_from_image(img_path=filename, file_name='my_article', save_file=False)
    cleaned_txt = itt.clean_extracted_text(article_txt)
#st.write(cleaned_txt)

    user_edited_txt = st.text_area(value=cleaned_txt, label='Your Selected Articles Text')
    save_edits = st.button(label="Save My Edits", key='save_edits')
    if save_edits:
        if 'final_text' not in st.session_state:  # create the state_session variable if it doesn't exist
            st.session_state['final_text'] = user_edited_txt
        else:  # update the user edited text
            st.session_state['final_text'] = user_edited_txt
