import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)
import json
from datasets import Dataset

from rag.chain import get_rag_chain
from rag.chain import retrieve_context

from evaluation.ragas_eval import run_ragas


# Load questions

with open(
    "evaluation/test_question.json",
    "r"
) as f:
    questions = json.load(f)
chain = get_rag_chain()

data = []
for item in questions:
    question = item["question"]
    ground_truth = item["ground_truth"]
    print("Processing:", question)

    answer = chain.invoke(
        question
    )

    docs = retrieve_context(
        question
    )
    contexts = [
        doc.page_content
        for doc in docs
    ]

    data.append(
        {
            "question": question,
            "answer": answer,
            "contexts": contexts,
            "ground_truth": ground_truth
        }
    )
dataset = Dataset.from_list(data)

result = run_ragas(dataset)
print(result)
df = result.to_pandas()
df.to_csv(
    "data/results.csv",
    index=False
)
print("✅ Evaluation completed")