import rampwf as rw
import pandas as pd
from pathlib import Path
from sklearn.model_selection import StratifiedShuffleSplit

problem_title = 'Municipal Farming Activity Prediction'

data_path = Path("data") / "X_train.csv"
df = pd.read_csv(data_path)
_prediction_label_names = sorted(df["target"].unique().tolist())

# A type (class) which will be used to create wrapper objects for y_pred
Predictions = rw.prediction_types.make_multiclass(
    label_names=_prediction_label_names
)

# An object implementing the workflow
workflow = rw.workflows.Estimator()

score_types = [
    rw.score_types.Accuracy(name='accuracy', precision=4),
]


def get_cv(X, y):
    cv = StratifiedShuffleSplit(n_splits=8, test_size=0.2, random_state=42)
    return cv.split(X, y)


# read data
def load_data(path='.', file='X_train.csv'):
    path = Path(path) / "data"
    X_df = pd.read_csv(path / file)

    y = X_df['target']
    X_df = X_df.drop(columns=['target'])

    return X_df, y

def get_train_data(path='.'):
    file = 'X_train.csv'
    return load_data(path, file)

def get_test_data(path='.'):
    file = 'X_test.csv'
    return load_data(path, file)
