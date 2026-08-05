import streamlit as st
import os

st.title("📂 Upload Documents")
UPLOAD_FOLDER = "data/documents"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
file = st.file_uploader(
    "Upload PDF Document",
    type=["pdf"]
)

if file:
    path = os.path.join(
        UPLOAD_FOLDER,
        file.name
    )
    with open(path, "wb") as f:
        f.write(file.getbuffer())
    st.success(f"{file.name} uploaded successfully!")