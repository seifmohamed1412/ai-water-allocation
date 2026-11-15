
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

_MODEL_PATH = (
    Path(__file__).resolve().parents[2]
    / "models"
    / "water_requirement_model.joblib"
)


def predict_irrigation(features):
    """
    Predict irrigation requirement in mm/day.

    Parameters
    ----------
    features : dict
        Mapping of the 38 expected processed feature names to numeric values,
        or a pandas DataFrame containing one row with those features.

    Returns
    -------
    float
        Predicted irrigation requirement in mm/day.
    """
    if not _MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model not found at {_MODEL_PATH}. Run train.py first."
        )

    bundle = joblib.load(_MODEL_PATH)
    model = bundle["model"]
    expected_features = bundle["features"]

    if isinstance(features, dict):
        row = pd.DataFrame([features])
    elif isinstance(features, pd.DataFrame):
        row = features.copy()
    else:
        raise TypeError("features must be a dict or pandas DataFrame.")

    if len(row) != 1:
        raise ValueError("Provide exactly one row of features.")

    missing = [col for col in expected_features if col not in row.columns]
    if missing:
        raise ValueError(f"Missing features: {', '.join(missing)}")

    row = row[expected_features]

    if row.isna().any().any():
        raise ValueError("Feature values cannot be missing.")

    prediction = float(model.predict(row)[0])
    return max(0.0, prediction)
