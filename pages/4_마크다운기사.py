import streamlit as st
from pathlib import Path



def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

st.markdown('# 📊 markdown')

intro_markdown = read_markdown_file("data/post_md/edited3.md")
st.markdown(intro_markdown, unsafe_allow_html=True)