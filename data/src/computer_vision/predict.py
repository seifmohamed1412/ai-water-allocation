
from pathlib import Path
from ultralytics import YOLO

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = PROJECT_ROOT / "models" / "best.pt"

OUTPUT_DIR = PROJECT_ROOT / "outputs" / "predictions"


def predict_image(image_path):
    image_path = Path(image_path)

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model not found: {MODEL_PATH}"
        )

    if not image_path.is_file():
        raise FileNotFoundError(
            f"Image not found: {image_path}"
        )

    model = YOLO(str(MODEL_PATH))

    results = model.predict(
        source=str(image_path),
        save=True,
        project=str(OUTPUT_DIR.parent),
        name=OUTPUT_DIR.name,
        exist_ok=True,
        conf=0.25
    )

    print("\nPrediction summary:")
    for result in results:
        if result.boxes is None or len(result.boxes) == 0:
            print("No fruit detected.")
            continue

        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            class_name = result.names[class_id]

            print(
                f"{class_name}: "
                f"{confidence:.2%} confidence"
            )

    print(f"\nAnnotated image saved in: {OUTPUT_DIR}")


if __name__ == "__main__":
    image_path = input("Enter the path to a fruit image: ").strip().strip('"')
    predict_image(image_path)
