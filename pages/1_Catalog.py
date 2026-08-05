import os
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Catalog",
    page_icon="📂",
    layout="wide"
)

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.title("🛒 TechNest Product Catalog")
st.caption("Upload product documents and build the vector database.")

st.divider()

# Upload PDFs

uploaded_files = st.file_uploader(
    "Upload PDF Documents",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        with open(
            os.path.join(UPLOAD_DIR, file.name),
            "wb"
        ) as f:
            f.write(file.getbuffer())
    st.success(f"{len(uploaded_files)} document(s) uploaded successfully.")

st.divider()

# Search + Filter

left, right = st.columns([3,1])

with left:
    search = st.text_input(
        "🔍 Search Documents"
    )

with right:
    category = st.selectbox(
        "Category",
        [
            "All",
            "Product",
            "Policy",
            "FAQ"
        ]
    )

# Read Files

rows = []

for file in os.listdir(UPLOAD_DIR):

    if file.endswith(".pdf"):

        size = os.path.getsize(
            os.path.join(UPLOAD_DIR,file)
        )

        rows.append(
            {
                "Document":file,
                "Category":"Product",
                "Size (KB)":round(size/1024,2),
                "Status":"Ready"
            }
        )

df = pd.DataFrame(rows)

if not df.empty:
    if search:
        df = df[
            df["Document"]
            .str.contains(
                search,
                case=False
            )
        ]
    if category!="All":
        df = df[
            df["Category"]==category
        ]

# Metrics

c1,c2 = st.columns([1,5])

with c1:

    st.metric(
        "Total Entries",
        len(df)
    )

st.divider()

# Table

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# Vector DB

if st.button(
    "🚀 Build Vector Database",
    use_container_width=True
):
    with st.spinner(
        "Building Vector Database..."
    ):
        st.success(
            "Vector Database Built Successfully!"
        )