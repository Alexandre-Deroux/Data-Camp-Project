from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier

pipe = make_pipeline(
        StandardScaler(),
        XGBClassifier(eval_metric="mlogloss", random_state=42)
    )

def get_estimator():
      return pipe
