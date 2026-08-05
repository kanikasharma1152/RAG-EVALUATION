import os
import pandas as pd
import streamlit as st
from datasets import Dataset

from evaluation.ragas_eval import run_ragas
from rag.chain import get_rag_chain, retrieve_context


# File Paths

GOLDENS_FILE = "data/goldens.csv"
RESULTS_FILE = "data/results.csv"


# Streamlit UI
st.title("🚀 RAGAS Evaluation Pipeline")

# Check Dataset

if not os.path.exists(GOLDENS_FILE):
    st.error("❌ Goldens dataset not found.")
    st.stop()

goldens = pd.read_csv(GOLDENS_FILE)

st.info(
    f"📌 Total Evaluation Questions: {len(goldens)}"
)

# Start Evaluation Button

if st.button("🚀 Start Evaluation"):

    # Load RAG Chain

    with st.spinner("Loading RAG Pipeline..."):
        try:
            chain = get_rag_chain()

            st.success(
                "✅ RAG Chain Loaded"
            )

        except Exception as e:

            st.error(
                f"RAG Chain Error: {e}"
            )

            st.stop()
    ragas_rows = []

    progress_bar = st.progress(0)

    # Generate Answers

    for index, row in goldens.iterrows():
        question = row["question"]

        ground_truth = str(
            row["ground_truth"]
        )
        try:
            # Retrieve Documents
            docs = retrieve_context(
                question
            )

            contexts = [
                doc.page_content
                for doc in docs
            ]

            # Generate Answer

            answer = str(
                chain.invoke(question)
            )

        except Exception as e:
            answer = (
                f"Error: {str(e)}"
            )

            contexts = [
                "No relevant context found"
            ]
        ragas_rows.append(
            {

                "question": question,
                "answer": answer,
                "contexts": contexts,
                "ground_truth": ground_truth
            }
        )


        progress_bar.progress(
            (index + 1) / len(goldens)
        )

    st.success(
        "✅ Evaluation Dataset Created"
    )
    # Convert to HuggingFace Dataset

    dataset = Dataset.from_list(
        ragas_rows
    )
    # Check Dataset Structure
    st.write("Dataset Features")
    st.write(
        dataset.features
    )

    st.write(
        "Dataset Preview"
    )
    st.dataframe(
        pd.DataFrame(ragas_rows),
        use_container_width=True
    )
    # Run RAGAS
    with st.spinner(
        "Running RAGAS Metrics..."
    ):
        try:
            result = run_ragas(
                dataset
            )
            scores = result.to_pandas()

            # Save Results

            os.makedirs(
                "data",
                exist_ok=True
            )
            scores.to_csv(
                RESULTS_FILE,
                index=False
            )
            st.success(
                "🎉 RAGAS Evaluation Completed"
            )

            st.subheader(
                "📊 Evaluation Scores"
            )
            st.dataframe(
                scores,
                use_container_width=True
            )

            st.download_button(
                label="📥 Download Results CSV",
                data=scores.to_csv(
                    index=False
                ),
                file_name="ragas_results.csv",
                mime="text/csv"
            )
        except Exception as e:
            st.error(
                f"❌ RAGAS Error: {e}"
            )
            st.write(
                "Dataset Sent to RAGAS:"
            )
            st.write(
                dataset
            )