# Project Plan

## Project

AI Water Allocation — AI-powered smart irrigation system that predicts crop water requirements and optimizes irrigation schedules.

## Team Responsibilities

| Member | Responsibility |
|---|---|
| Ahmed Hamdy | Data Collection & Preparation |
| Saeed | Computer Vision |
| Seif | Water Requirement Prediction |
| Ahmed Youssef | Irrigation Optimization |
| Ziad Desoky | Dashboard & Economic Analysis |

## Development Pipeline

```text
Data Collection & Preparation
            ↓
Computer Vision
            ↓
Water Requirement Prediction
            ↓
Irrigation Optimization
            ↓
Dashboard & Economic Analysis
```

## Phase 1 — Data Collection & Preparation

**Owner:** Ahmed Hamdy

- Collect agricultural, weather, soil, irrigation, and related datasets.
- Explore relevant Roboflow agriculture datasets.
- Clean and preprocess the data.
- Standardize units and feature formats.
- Investigate missing values and outliers.
- Define the target variable for water requirement prediction.
- Create the initial integrated dataset.

## Phase 2 — Computer Vision

**Owner:** Saeed

- Select an appropriate agricultural computer vision dataset.
- Prepare images and annotations.
- Select and train a suitable computer vision model.
- Evaluate model performance.
- Extract useful field/crop information for the irrigation system.
- Export structured CV features for the ML pipeline.

## Phase 3 — Water Requirement Prediction

**Owner:** Seif

- Combine the prepared agricultural data with computer vision outputs.
- Perform feature engineering.
- Establish baseline machine learning models.
- Train and compare multiple models.
- Evaluate using MAE, RMSE, and R².
- Tune the selected model.
- Analyze feature importance/explainability.
- Build the final water requirement prediction pipeline.

## Phase 4 — Irrigation Optimization

**Owner:** Ahmed Youssef

- Define irrigation constraints.
- Use predicted water requirements as optimization inputs.
- Allocate available water between fields.
- Optimize irrigation quantity and timing.
- Consider water availability and field requirements.
- Calculate water and cost savings where possible.

## Phase 5 — Dashboard & Economic Analysis

**Owner:** Ziad Desoky

- Build the Streamlit dashboard.
- Display field-level irrigation recommendations.
- Display water usage and savings.
- Display economic indicators.
- Explain why irrigation recommendations were made.
- Integrate all project components.

## Final Pipeline

```text
Raw Data
   ↓
Data Preparation
   ↓
Computer Vision
   ↓
Water Requirement Prediction
   ↓
Irrigation Optimization
   ↓
Economic Analysis
   ↓
Streamlit Dashboard
```

## Current Status

Project structure created.

Detailed dataset selection, model selection, and implementation will be finalized during development.