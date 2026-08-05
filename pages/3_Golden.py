import os
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Create Goldens",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Create Goldens Dataset")

st.write(
    "Create question-answer pairs for RAG evaluation."
)

st.divider()

questions = st.text_area(
    "Questions (One per line)",
    height=200,
    placeholder="""
What is return policy?
What are the shipping charges?"""
)

answers = st.text_area(
    "Ground Truth Answers (One per line)",
    height=200
)

if st.button("💾 Save Goldens"):

    q = [i.strip() for i in questions.split("\n") if i.strip()]
    a = [i.strip() for i in answers.split("\n") if i.strip()]

    if len(q) != len(a):
        st.error("Questions and Answers count must match.")
        st.stop()

    df = pd.DataFrame({
        "question": q,
        "ground_truth": a
    })

    os.makedirs("data", exist_ok=True)

    df.to_csv(
        "data/goldens.csv",
        index=False
    )

    st.success("Goldens Dataset Saved Successfully!")

st.divider()

if os.path.exists("data/goldens.csv"):

    df = pd.read_csv("data/goldens.csv")

    st.subheader("Current Dataset")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )