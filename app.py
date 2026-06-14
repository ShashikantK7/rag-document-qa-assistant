import streamlit as st

st.set_page_config(page_title='RAG Document Q&A Assistant')

st.title('📄 RAG Document Q&A Assistant')
st.write('Phase 1 setup complete. PDF upload and RAG pipeline coming next.')

uploaded_file = st.file_uploader('Upload a PDF', type=['pdf'])

if uploaded_file:
    st.success(f'Uploaded: {uploaded_file.name}')
