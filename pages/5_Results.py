import os
import pandas as pd
import streamlit as st

RESULTS_FILE = "data/results.csv"

st.title("📊 Evaluation Results")

if not os.path.exists(RESULTS_FILE):
    st.warning("No evaluation results found.")

else:
    df = pd.read_csv(RESULTS_FILE)
    st.dataframe(
        df,
        use_container_width=True
    )

    st.download_button(
        "📥 Download CSV",
        df.to_csv(index=False),
        "results.csv",
        "text/csv"
    )