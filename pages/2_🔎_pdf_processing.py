from kv_pdf_processor import pdf_splitter, pdf_to_image
import streamlit as st
import os
from io import BytesIO
import PIL.Image as image

st.set_page_config(
    page_title="KlangVerso - PDF Processing",
    page_icon=":mag:",
)
st.markdown(
    """
    Please feel free to upload a PDF (multi-page is okay!). This page will parse, process, and segment single
    page articles with ease."""
)

pdf_file = st.file_uploader('Select an pdf file to be processed.')

if pdf_file:

    with open("temp.pdf", 'wb') as pdf:
        pdf.write(pdf_file.getbuffer())
        pdf.close()

    pdf_splitter.split_pdf(file_path='temp.pdf', output_dir='./temp')
    if len(os.listdir('./temp')) > 4:
        st.write('This file is too large to process in this demo. Please select a smaller file.')
        for file in os.listdir('./temp'):
            os.remove(file)
    else:
        for files in os.listdir('./temp'):
            if files.endswith('.pdf'):
                pdf_to_image.convert_pdf_to_jpeg(pdf_path=files, output_dir='.')





