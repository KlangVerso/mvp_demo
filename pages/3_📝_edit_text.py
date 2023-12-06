import streamlit as st
import os
import kv_text_processing.img_to_text as itt

st.set_page_config(
    page_title="KlangVerso - Edit Your Text",
    page_icon="📝",
)

if st.session_state.auth_status:

    st.markdown(
        """
        Select the article that you would like to work with. You will have the option to modify the text to ensure
        that the text-to-speech functionality matches your expectations."""
    )

    text = ""
    if 'text' not in st.session_state:
        st.session_state.text = text

    def file_selector(folder_path='.'):
        files = []
        for file in os.listdir(folder_path):
            if file.endswith('.jpeg'):
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
        st.session_state.text = cleaned_txt
        os.remove('temp.pdf')

    st.session_state.text = st.text_area(value=st.session_state.text,
                                         label='Your Selected Articles Text',
                                         height=500)


else:  # user isn't authenticated
    st.warning('Please log in to access this feature.')
