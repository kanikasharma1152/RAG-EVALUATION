import pandas as pd


def save_results(result):

    df = result.to_pandas()

    df.to_csv(
        "data/results.csv",
        index=False
    )

    return df