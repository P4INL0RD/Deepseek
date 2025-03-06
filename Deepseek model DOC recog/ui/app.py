import streamlit as st
from backend.chat_backend import get_chat_response, summarize_file

st.title("DeepSeek Chatbot")
st.write("Ask me anything or upload a file for summarization!")

# File uploader
uploaded_file = st.file_uploader(
    "Upload a file (PDF, DOC, DOCX, TXT, CSV)", 
    type=["pdf", "doc", "docx", "txt", "csv"]
)

if uploaded_file:
    # Summarize the file and translate to Spanish
    translated_summary, doc_buffer = summarize_file(uploaded_file)
    st.write("Resumen del archivo (en español):")
    st.write(translated_summary)

    # Download button for the summarized .docx file
    st.download_button(
        label="Descargar Resumen en DOCX",
        data=doc_buffer,
        file_name="resumen.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

# Chat input
user_input = st.text_input("Enter your question here:")

if user_input:
    response = get_chat_response(user_input)
    st.write("Response:")
    st.write(response)