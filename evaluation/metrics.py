import pandas as pd
from datasets import Dataset

from rag.chain import get_rag_chain, retrieve_context


def create_dataset(goldens_path="data/goldens.csv"):
    df = pd.read_csv(goldens_path)
    chain = get_rag_chain()

    questions = []
    answers = []
    contexts = []
    ground_truths = []

    for _, row in df.iterrows():
        question = row["question"]
        ground_truth = row["ground_truth"]

        answer = chain.invoke(question)

        docs = retrieve_context(question)
        context = [doc.page_content for doc in docs]

        questions.append(question)
        answers.append(answer)
        contexts.append(context)
        ground_truths.append(ground_truth)

    dataset = Dataset.from_dict({
        "question": questions,
        "answer": answers,
        "contexts": contexts,
        "ground_truth": ground_truths
    })

    return dataset