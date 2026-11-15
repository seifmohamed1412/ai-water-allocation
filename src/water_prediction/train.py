from pathlib import Path
import json
import joblib
import numpy as np
import pandas as pd

from sklearn.dummy import DummyRegressor
from sklearn.ensemble import ExtraTreesRegressor, RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "processed"
MODEL_DIR = ROOT / "models"
REPORT_DIR = ROOT / "reports" / "results"

TARGET = "IR_mm"
SEED = 42


def load_split(name):
    path = DATA_DIR / f"{name}_processed.csv"
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    df = pd.read_csv(path)

    if TARGET not in df.columns:
        raise ValueError(f"Target '{TARGET}' missing from {path}")

    if df.empty:
        raise ValueError(f"Dataset is empty: {path}")

    if df.isna().any().any():
        raise ValueError(f"Missing values found in {path}")

    X = df.drop(columns=[TARGET])
    y = df[TARGET]

    if not all(pd.api.types.is_numeric_dtype(dtype) for dtype in X.dtypes):
        raise ValueError(f"Non-numeric input features found in {path}")

    return X, y


def calculate_metrics(y_true, predictions):
    return {
        "MAE_mm_day": float(mean_absolute_error(y_true, predictions)),
        "RMSE_mm_day": float(np.sqrt(mean_squared_error(y_true, predictions))),
        "R2": float(r2_score(y_true, predictions)),
    }


def main():
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    X_train, y_train = load_split("train")
    X_valid, y_valid = load_split("valid")
    X_test, y_test = load_split("test")

    if list(X_train.columns) != list(X_valid.columns):
        raise ValueError("Train and validation features do not match.")

    if list(X_train.columns) != list(X_test.columns):
        raise ValueError("Train and test features do not match.")

    print(f"Training rows: {len(X_train):,}")
    print(f"Validation rows: {len(X_valid):,}")
    print(f"Test rows: {len(X_test):,}")
    print(f"Features: {len(X_train.columns)}")
    print(f"Target: {TARGET} (mm/day)")

    models = {
        "dummy_mean": DummyRegressor(strategy="mean"),
        "random_forest": RandomForestRegressor(
            n_estimators=200,
            min_samples_leaf=2,
            random_state=SEED,
            n_jobs=-1,
        ),
        "extra_trees": ExtraTreesRegressor(
            n_estimators=200,
            min_samples_leaf=2,
            random_state=SEED,
            n_jobs=-1,
        ),
    }

    results = []
    fitted_models = {}

    for name, model in models.items():
        print(f"\nTraining {name}...")
        model.fit(X_train, y_train)

        valid_predictions = model.predict(X_valid)
        metrics = calculate_metrics(y_valid, valid_predictions)

        results.append({
            "model": name,
            "split": "validation",
            **metrics,
        })
        fitted_models[name] = model

        print(
            f"Validation MAE: {metrics['MAE_mm_day']:.4f} mm/day | "
            f"RMSE: {metrics['RMSE_mm_day']:.4f} mm/day | "
            f"R2: {metrics['R2']:.4f}"
        )

    validation_results = [
        row for row in results if row["split"] == "validation"
    ]
    best_result = min(
        validation_results,
        key=lambda row: row["RMSE_mm_day"],
    )
    best_name = best_result["model"]
    best_model = fitted_models[best_name]

    test_predictions = best_model.predict(X_test)
    test_metrics = calculate_metrics(y_test, test_predictions)

    results.append({
        "model": best_name,
        "split": "test",
        **test_metrics,
    })

    model_path = MODEL_DIR / "water_requirement_model.joblib"
    joblib.dump(
        {
            "model": best_model,
            "features": list(X_train.columns),
            "target": TARGET,
            "target_unit": "mm/day",
            "selected_model": best_name,
            "validation_metrics": best_result,
            "test_metrics": test_metrics,
        },
        model_path,
    )

    results_path = REPORT_DIR / "water_prediction_metrics.csv"
    pd.DataFrame(results).to_csv(results_path, index=False)

    summary = {
        "selected_model": best_name,
        "target": TARGET,
        "target_unit": "mm/day",
        "feature_count": len(X_train.columns),
        "validation_metrics": best_result,
        "test_metrics": test_metrics,
        "model_path": str(model_path),
        "metrics_path": str(results_path),
    }

    summary_path = REPORT_DIR / "water_prediction_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print("\n========== FINAL RESULTS ==========")
    print(f"Selected model: {best_name}")
    print(f"Test MAE:  {test_metrics['MAE_mm_day']:.4f} mm/day")
    print(f"Test RMSE: {test_metrics['RMSE_mm_day']:.4f} mm/day")
    print(f"Test R2:   {test_metrics['R2']:.4f}")
    print(f"\nSaved model: {model_path}")
    print(f"Saved metrics: {results_path}")
    print(f"Saved summary: {summary_path}")


if __name__ == "__main__":
    main()
