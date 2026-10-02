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
