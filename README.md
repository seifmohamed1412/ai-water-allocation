# AI Water Allocation

An AI-powered smart irrigation system designed to help farmers make better irrigation decisions using machine learning and computer vision.

## Overview

Agriculture consumes a significant amount of freshwater, making efficient irrigation an important challenge. Traditional irrigation practices may lead to water waste or insufficient watering.

**AI Water Allocation** aims to address this challenge by combining machine learning, computer vision, and irrigation optimization to support data-driven agricultural decisions.

The system is designed to analyze agricultural data, estimate crop water requirements, identify crop conditions, and support optimized irrigation planning.

## Project Objectives

- Predict crop water requirements using machine learning.
- Analyze crop images using computer vision.
- Optimize irrigation schedules and water allocation.
- Provide useful insights through a unified system.

## System Architecture

The project consists of several interconnected components:

1. **Data Preparation:** Collecting and preparing agricultural, soil, irrigation, and image datasets.
2. **Computer Vision:** Analyzing crop images to identify fresh and rotten produce.
3. **Water Requirement Prediction:** Estimating irrigation requirements using machine learning.
4. **Irrigation Optimization:** Using prediction outputs to support efficient irrigation planning.
5. **Dashboard and Economic Analysis:** Presenting results and relevant agricultural insights.

## Machine Learning Components

### 1. Water Requirement Prediction

An Extra Trees Regressor was selected to predict irrigation requirements.

- Target variable: `IR_mm`
- Prediction unit: mm/day
- Input features: 38
- Training samples: 58,700
- Validation samples: 8,490
- Test samples: 16,520

**Test performance:**

| Metric | Result |
|---|---:|
| MAE | 0.5312 |
| RMSE | 0.7618 |
| R² | 0.9601 |

The model was also compared against a previous-day baseline and achieved lower MAE and RMSE.

**Important:** The target values are derived from the dataset's irrigation calculation methodology. These results measure how well the model reproduces those targets; they do not independently establish real-world water savings or field accuracy.

### 2. Computer Vision

The computer vision component uses YOLO to analyze fruit images and distinguish between fresh and rotten produce.

The repository includes:
- Training, validation, and testing images.
- Corresponding image labels.
- Trained model weights.
- Training metrics and evaluation visualizations.

## Repository Structure

```text
ai-water-allocation/
│
├── data/
│   ├── raw/
│   │   ├── computer_vision/
│   │   └── crop_recommendation/
│   │
│   └── processed/
│       └── irrigation/
│
├── docs/
│   └── datasets/
│
├── models/
│   ├── computer_vision/
│   └── water_requirement_model.joblib
│
├── reports/
│   ├── computer_vision/
│   └── results/
│
├── src/
│   ├── computer_vision/
│   └── water_prediction/
│
├── requirements.txt
└── README.md
```

## Datasets

The project currently includes:

- **Irrigation Dataset:** Processed agricultural data used for water requirement prediction.
- **Crop Recommendation Dataset:** Crop-related and soil suitability data.
- **Fruits Fresh and Rotten Dataset:** Labeled fruit images used for computer vision training.

Dataset documentation is available in `docs/datasets/`.

## Installation

Clone the repository:

```bash
git clone <REPOSITORY_URL>
cd ai-water-allocation
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

### Water Requirement Prediction

Train the model:

```bash
python src/water_prediction/train.py
```

Use the prediction module:

```python
from src.water_prediction import predict_irrigation
```

Refer to the source code for the expected input format and prediction function arguments.

### Computer Vision

Open the notebook:

```text
src/computer_vision/computer_vision.ipynb
```

Run it using Jupyter Notebook or JupyterLab.

The trained YOLO weights are available under `models/computer_vision/`.

## Team Contributions

| Team Member | Responsibility |
|---|---|
| Ahmed Hamdy | Data collection and preparation |
| Saeed | Computer vision |
| Seif | Water requirement prediction |
| Ahmed Youssef | Irrigation optimization |
| Ziad Desoky | Dashboard and economic analysis |

## Project Status

The repository currently contains the irrigation prediction implementation, computer vision training artifacts, datasets, and supporting documentation. Other system components are being integrated.

## Technologies

- Python
- Pandas and NumPy
- Scikit-learn
- YOLO / Ultralytics
- PyTorch
- OpenCV
- Matplotlib and Seaborn
- Jupyter Notebook

---

Developed as a collaborative AI and machine learning project.