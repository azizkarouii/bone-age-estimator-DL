# Notebook Outputs Extracted

This file collects the main textual outputs produced by the executed notebooks in this project. Large HTML tables, plots, and image grids are summarized instead of being copied verbatim.

## 1. `drafts/01_eda_preprocessing.ipynb`

Extracted output:

```text
Images trouvees: 12811
```

Notes:
- The notebook also produced a dataframe summary table.
- The cell rendered 4 preview hand radiograph images.
- A distribution plot was generated when the target column was numeric.

## 2. `drafts/02_baseline_cnn.ipynb`

Extracted outputs:

| Epoch | Train loss | Train MAE | Train MSE | Val loss | Val MAE | Val MSE |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1/10 | 35.2130 | 35.2130 | 2006.8650 | 34.6211 | 34.6211 | 1772.9615 |
| 2/10 | 33.9466 | 33.9466 | 1805.6951 | 34.0760 | 34.0760 | 1870.6748 |
| 3/10 | 33.5221 | 33.5221 | 1771.5029 | 34.5140 | 34.5140 | 1962.4393 |
| 4/10 | 33.5771 | 33.5771 | 1790.7678 | 33.9795 | 33.9795 | 1784.3894 |
| 5/10 | 33.5396 | 33.5396 | 1769.2639 | 33.9717 | 33.9717 | 1814.4049 |
| 6/10 | 33.7357 | 33.7357 | 1809.3593 | 35.8613 | 35.8613 | 1843.7880 |
| 7/10 | 33.6617 | 33.6617 | 1782.8402 | 34.2644 | 34.2644 | 1908.6339 |
| 8/10 | 33.3590 | 33.3590 | 1772.0029 | 33.9454 | 33.9454 | 1802.9203 |
| 9/10 | 33.3486 | 33.3486 | 1764.7345 | 34.4458 | 34.4458 | 1946.8376 |
| 10/10 | 33.4762 | 33.4762 | 1772.2738 | 34.0368 | 34.0368 | 1781.3271 |

| Final result | Value |
| --- | ---: |
| Validation MAE | 33.95 mois |

Notes:
- The notebook also rendered a learning-curve plot and a prediction scatter plot.
- EarlyStopping was configured with `patience=3`.

## 3. `drafts/03_regularization_tuning.ipynb`

Extracted outputs:

| Epoch | Train loss | Train MAE | Train MSE | Val loss | Val MAE | Val MSE |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1/15 | 92.4443 | 92.4151 | 10735.6582 | 47.1306 | 47.0965 | 3590.4858 |
| 2/15 | 36.8106 | 36.7690 | 2086.0984 | 641.5740 | 641.5248 | 414985.6562 |
| 3/15 | 32.5220 | 32.4673 | 1660.5759 | 3860.9275 | 3860.8672 | 14912093.0000 |
| 4/15 | 30.5825 | 30.5180 | 1481.6464 | 8312.4658 | 8312.3945 | 69108520.0000 |
| 5/15 | 28.7876 | 28.7181 | 1328.3572 | 217.7010 | 217.6306 | 49287.6797 |
| 6/15 | 28.7540 | 28.6828 | 1317.8856 | 700.4029 | 700.3311 | 494798.8750 |
| 7/15 | 28.6240 | 28.5511 | 1302.7584 | 178.0253 | 177.9517 | 40759.9453 |
| 8/15 | 27.7639 | 27.6899 | 1237.8038 | 801.3743 | 801.3001 | 647817.6250 |

Notes:
- This run showed unstable validation behavior after the first epochs.
- The notebook produced a model comparison plot.
- EarlyStopping was configured with `patience=7`.

## 4. `drafts/04_transfer_learning.ipynb`

Extracted outputs:

| Epoch | Train loss | Train MAE | Train MSE | Val loss | Val MAE | Val MSE |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1/5 | 38.7602 | 38.7602 | 2496.2986 | 34.0292 | 34.0292 | 1843.2396 |
| 2/5 | 34.6707 | 34.6707 | 1879.4231 | 34.0819 | 34.0819 | 1874.1355 |
| 3/5 | 34.3291 | 34.3291 | 1850.0886 | 34.2975 | 34.2975 | 1915.1936 |
| 4/5 | 34.2890 | 34.2890 | 1845.9615 | 34.5157 | 34.5157 | 1771.5719 |
| 5/5 | 34.3678 | 34.3678 | 1864.7350 | 34.3138 | 34.3138 | 1919.1088 |

Notes:
- The notebook also produced a transfer-learning comparison plot.
- A second training phase was prepared for fine-tuning.
- EarlyStopping was configured with `patience=3`.

## 5. `notebooks/final_pipeline_bone_age.ipynb`

Extracted outputs:

| Epoch | Train loss | Train MAE | Train MSE | Val loss | Val MAE | Val MSE | LR |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1/10 | 41.1314 | 41.1314 | 2763.3159 | 37.0960 | 37.0960 | 1939.8793 | 0.0010 |
| 2/10 | 36.9053 | 36.9053 | 2115.6658 | 34.2346 | 34.2346 | 1762.8502 | 0.0010 |
| 3/10 | 36.3546 | 36.3546 | 2052.9116 | 34.4131 | 34.4131 | 1755.1744 | 0.0010 |
| 4/10 | 37.0210 | 37.0210 | 2100.4099 | 37.2416 | 37.2416 | 1935.5109 | 0.0010 |
| 5/10 | 36.0739 | 36.0739 | 2016.5314 | 37.7992 | 37.7992 | 1976.4933 | 0.0010 |
| 6/10 | 35.4677 | 35.4677 | 1966.2048 | 34.3504 | 34.3504 | 1739.3961 | 5.0000e-04 |
| 7/10 | 35.4351 | 35.4351 | 1957.5800 | 33.5703 | 33.5703 | 1780.7902 | 5.0000e-04 |
| 8/10 | 35.3243 | 35.3243 | 1937.8640 | 34.4104 | 34.4104 | 1737.3716 | 5.0000e-04 |
| 9/10 | 35.3401 | 35.3401 | 1949.6296 | 33.3852 | 33.3852 | 1742.7667 | 5.0000e-04 |
| 10/10 | 35.2647 | 35.2647 | 1940.1036 | 33.7222 | 33.7222 | 1701.5709 | 5.0000e-04 |

| Final result | Value |
| --- | ---: |
| Train images | 10088 |
| Validation images | 2523 |
| Exported model | `models/bone_age_model.keras` (EfficientNet / Transfer Learning) |
| Export status | Success |
| Best model overall | Transfer Learning |
| Final validation MAE | 14.3728 mois |
| Final validation MSE | 333.7416 |
| Final validation R2 | 0.8116 |

Notes:
- The notebook also produced learning curves, predicted-vs-actual plots, and Grad-CAM visualizations.
- The best model was exported to `.keras`.
- Final comparison on validation selected Transfer Learning over the regularized CNN.

Extracted printed outputs from evaluation and export steps:

```text
Resultats CNN Regularise: {'mae': 33.385223388671875, 'mse': 1742.7667236328125, 'r2': 0.016080379486083984}
Resultats Transfer Learning: {'mae': 14.372787475585938, 'mse': 333.74163818359375, 'r2': 0.8115783929824829}

Modele sauvegarde: c:\Users\LENOVO\Desktop\4eme cycle ing\S2\ML\DLProject\models\bone_age_model.keras
Modele selectionne: EfficientNet
```

Note: `EfficientNet` ci‑dessus fait référence au backbone `EfficientNetB0` utilisé dans l'approche de transfer learning (libellé `Transfer Learning` dans le tableau comparatif).

## 6. Visual Outputs Not Copied

The following outputs were generated but are not embedded here because they are graphical or too large:
- Image preview grid in the EDA notebook.
- Learning curve plots for the baseline, regularized, transfer-learning, and final notebooks.
- Predicted-vs-actual scatter plots.
- Grad-CAM heatmaps from the final pipeline.

## 7. Source Paths

- [drafts/01_eda_preprocessing.ipynb](drafts/01_eda_preprocessing.ipynb)
- [drafts/02_baseline_cnn.ipynb](drafts/02_baseline_cnn.ipynb)
- [drafts/03_regularization_tuning.ipynb](drafts/03_regularization_tuning.ipynb)
- [drafts/04_transfer_learning.ipynb](drafts/04_transfer_learning.ipynb)
- [notebooks/final_pipeline_bone_age.ipynb](notebooks/final_pipeline_bone_age.ipynb)
