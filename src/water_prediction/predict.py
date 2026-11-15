from pathlib import Path
import argparse
import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = ROOT / "models" / "water_requirement_model.joblib"
TARGET = "IR_mm"


def predict(input_path, output_path):
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Trained model not found: {MODEL_PATH}\n"
            "Run train.py first."
        )

    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input CSV not found: {input_path}")

    bundle = joblib.load(MODEL_PATH)
    model = bundle["model"]
    features = bundle["features"]

    df = pd.read_csv(input_path)

    if df.empty:
        raise ValueError("Input CSV is empty.")

    missing = [col for col in features if col not in df.columns]
    if missing:
        raise ValueError(
            "Input CSV is missing required features:\n"
            + ", ".join(missing)
        )

    X = df[features].copy()

    if X.isna().any().any():
        raise ValueError("Input features contain missing values.")

    predictions = model.predict(X)

    # Irrigation requirements cannot be negative.
    predictions = np.maximum(predictions, 0)

    output = df.copy()
    output["predicted_IR_mm_day"] = predictions

    if TARGET in df.columns:
        y_true = df[TARGET]
        metrics = {
            "MAE_mm_day": float(mean_absolute_error(y_true, predictions)),
            "RMSE_mm_day": float(
                np.sqrt(mean_squared_error(y_true, predictions))
            ),
            "R2": float(r2_score(y_true, predictions)),
        }

        print("\nEvaluation metrics:")
        for name, value in metrics.items():
            print(f"{name}: {value:.4f}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output.to_csv(output_path, index=False)

    print(f"\nRows predicted: {len(output):,}")
    print(f"Output saved to: {output_path}")
    print("\nFirst 5 predictions:")
    print(output[["predicted_IR_mm_day"]].head().to_string(index=False))


def main():
    parser = argparse.ArgumentParser(
        description="Predict irrigation requirement in mm/day."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to a CSV containing all 38 model features.",
    )
    parser.add_argument(
        "--output",
        default="data/reports/results/predictions.csv",
        help="Path for the output CSV.",
    )
    args = parser.parse_args()

    predict(args.input, args.output)


if __name__ == "__main__":
    main()
