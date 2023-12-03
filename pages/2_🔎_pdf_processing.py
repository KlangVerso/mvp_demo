from kv_image_pipeline import image_pipeline
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
    segment_path = os.path.relpath('best_segment_model.pt', start = os.curdir)
    my_pipe = image_pipeline.ImagePipeline(pdf_path='temp.pdf',
                                           file_name='testfile',
                                           output_dir_path="./temp",
                                           segment_model_path='./best_segmentation_model.pt')
    my_pipe.run_pipeline()


