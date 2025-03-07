from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

DATA_PATH = Path('data')

if __name__ == '__main__':
    if not DATA_PATH.exists():
        DATA_PATH.mkdir()

    print('Loading the data...', end='', flush=True)
    data = pd.read_csv('data_municipal_farming_areas_2008_2023_agencybio.csv', low_memory=False)

    X = data.drop(columns=["production_principale", "activites", "code_activites"])
    y = data["code_activites"]

    for col in X.select_dtypes(include=['object']).columns:
        X[col] = X[col].astype(str)
        X[col] = X[col].astype("category").cat.codes

    y = y.astype("category").cat.codes
    X["target"] = y

    X_train, X_test = train_test_split(
        X, test_size=0.2, random_state=42, stratify=y
    )

    X_train.to_csv(DATA_PATH / 'X_train.csv', index=False)
    X_test.to_csv(DATA_PATH / 'X_test.csv', index=False)
    print('Done')