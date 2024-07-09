from kv_pdf_processor import pdf_splitter, pdf_to_image
import streamlit as st
import os

st.set_page_config(
    page_title="KlangVerso - PDF Processing",
    page_icon=":mag:",
)

st.markdown(
    """
    Please upload a single page PDF to see how our platform works. This page processes the file and
    prepares for OCR and copyrighting. """
)

pdf_file = st.file_uploader('Select an pdf file to be processed.')
file_name = st.text_input('Please enter a name for your file.')

if 'file_name' not in st.session_state:
    st.session_state.file_name = file_name

if pdf_file:
    with open("temp.pdf", 'wb') as pdf:
        pdf.write(pdf_file.getbuffer())
        pdf.close()

    with open("temp.pdf", 'rb') as pdf:
        num_chars = len(pdf.read())
        for file in os.listdir('./'):
            if file.endswith('.pdf'):
                pdf_to_image.convert_pdf_to_jpeg(pdf_path=file,
                                                 output_dir='.',
                                                 base_name=file_name)
                st.write(f'Successfully converted your pdf to an image.')
                st.session_state.file_name = file_name

else:  # User not authenticated
st.warning('Please log in to access this feature.')
