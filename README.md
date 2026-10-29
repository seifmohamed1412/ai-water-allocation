# AI Water Allocation

AI-powered smart irrigation system that predicts crop water requirements and optimizes irrigation schedules using crop, soil, weather, and computer vision data.

## Project Overview

The goal of this project is to develop an intelligent irrigation system that determines:

- How much water each field needs
- When each field should be irrigated
- How available water should be distributed between fields
- The expected water and economic savings

The system combines machine learning, computer vision, and optimization techniques to make irrigation decisions based on changing field conditions.

## System Pipeline

```text
Crop / Soil / Weather Data
          +
Computer Vision Data
          ↓
Water Requirement Prediction
          ↓
Irrigation Optimization
          ↓
Water Allocation & Schedule
          ↓
Dashboard & Economic Analysis
```

## Main Components

1. **Data Collection & Preparation**
   - Collect and clean crop, soil, weather, irrigation, and related agricultural data.
   - Prepare the datasets for machine learning.

2. **Computer Vision**
   - Analyze agricultural images.
   - Extract useful information such as crop type, crop condition, or vegetation/stress indicators.

3. **Water Requirement Prediction**
   - Predict the amount of water required by each field.
   - Compare and evaluate different machine learning models.

4. **Irrigation Optimization**
   - Allocate available water between fields.
   - Optimize irrigation quantity and timing while respecting constraints.

5. **Dashboard & Economic Analysis**
   - Display irrigation recommendations.
   - Show water usage, savings, costs, and other relevant results.

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Machine Learning
- Computer Vision
- Optimization
- Streamlit
- Roboflow

## Data Sources

Agricultural computer vision datasets will be explored and selected from Roboflow Universe.

Additional weather, soil, irrigation, and agricultural datasets will be selected based on project requirements and data availability.

## Project Status

🚧 In development

## Team

| Member | Responsibility |
|---|---|
| Ahmed Hamdy | Data Collection & Preparation |
| Saeed | Computer Vision |
| Seif | Water Requirement Prediction |
| Ahmed Youssef | Irrigation Optimization |
| Ziad Desoky | Dashboard & Economic Analysis |

# Irrigation Dataset Documentation

## Purpose

This dataset is used to train a machine-learning model to estimate daily crop irrigation requirements for the AI Water Allocation course project.

## Data sources

- **Weather data:** NASA POWER.
- **Crop coefficients and evapotranspiration methodology:** FAO-56 reference methodology.
- **Crop images:** Roboflow Universe fruit freshness dataset, used separately for the computer vision component.
- **Crop recommendation data:** `crop_recommendation.csv`, used only if needed for an additional crop recommendation feature.

See the dataset guide in `docs/irrigation_dataset_guide_ar.pdf` for the detailed methodology and references. Verify the original dataset licence and attribution requirements before redistribution.

## Target variable

The target is `IR_mm`, representing the calculated daily irrigation requirement in millimetres.

The target is derived using:

- Crop evapotranspiration: `ETc = Kc × ET0`
- Effective rainfall: `rain_eff = 0.8 × rain` when rainfall is at least 5 mm; otherwise, `rain_eff = 0`
- Irrigation requirement: `IR_mm = max(ETc - rain_eff, 0)`

The model therefore learns to approximate a formula-derived estimate. The target is **not a set of actual field irrigation measurements**, and model accuracy against this target does not establish accuracy against real farm water consumption.

## Missing soil data

Soil properties were intended to be collected from SoilGrids, but usable soil-property values were not obtained for this dataset. Consequently, soil features are absent from the current processed dataset.

The model cannot directly account for differences in soil texture, water-holding capacity, drainage, or other soil-specific factors.

## Dataset limitations

- Weather data has limited spatial resolution and may not represent individual fields precisely.
- Crop coefficients and crop-stage assumptions require validation for local agricultural conditions.
- The simplified effective-rainfall formula does not fully represent soil-water dynamics or irrigation-system losses.
- Flooded crops such as rice may require additional modelling of flooding and percolation.
- The dataset should be treated as an educational modelling dataset, not a validated operational irrigation recommendation system.

## Data splitting

The documented split is chronological:

- Training: 2015–2021
- Validation: 2022
- Testing: 2023–2024

These year ranges should be verified against the original dates or the dataset-generation script.

## Intended use

This dataset supports a course project exploring irrigation prediction and water allocation. Predictions should be interpreted as estimates under the dataset's assumptions rather than verified real-world irrigation requirements.

