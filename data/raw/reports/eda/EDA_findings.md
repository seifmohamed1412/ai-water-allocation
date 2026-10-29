# Exploratory Data Analysis — Irrigation Dataset

## Dataset quality

The processed dataset contains 58,700 training rows, 8,490 validation rows, and 16,520 test rows. Each split contains 39 columns, including 38 model input features and the `IR_mm` target.

The EDA checks found no missing values or exact duplicate rows in any of the three splits. The target has a training mean of approximately 6.971 mm/day and a median of 7.297 mm/day.

## Differences between crops

Average calculated irrigation requirements vary by crop. Rice has the highest training average at 9.993 mm/day, followed by maize at 7.710 mm/day and cotton at 7.619 mm/day. Wheat has the lowest average at 2.506 mm/day.

These differences are consistent with the dataset representing different crops and growing conditions. However, the target is calculated rather than measured from actual irrigation records.

## Feature relationships

The strongest positive Pearson correlations with `IR_mm` include `ET0_mm_roll7` (0.808), `ET0_mm_roll3` (0.800), and `ET0_mm_lag1` (0.798). The strongest negative correlation is `doy_cos` (-0.755), followed by `month_cos` (-0.662).

These relationships indicate that evapotranspiration-related and seasonal features are strongly associated with the target in the training data. Correlation does not imply causation.

## Limitations

The findings must be interpreted in light of the formula-derived target, unavailable soil-property data, approximate weather locations, and assumptions in the crop coefficients and effective-rainfall calculation. The chronological split also needs verification against the original dates or dataset-generation script.
