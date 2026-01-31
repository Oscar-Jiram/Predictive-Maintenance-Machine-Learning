#  Predictive Maintenance using Machine Learning  
## AI4I 2020 Dataset

---

## Project Overview

This project applies **machine learning to predictive maintenance**, aiming to **predict machine failures before they occur** using sensor data.

The objective is to build a **robust, interpretable, and cost-aware classification model** suitable for industrial decision-making, where missing a failure is significantly more expensive than triggering a false alarm.

---

##  Problem Statement

Machine failures are **rare but costly events**, resulting in a **highly imbalanced classification problem**.

**Target variable**
- `Machine failure`
  - `1` → Failure  
  - `0` → No failure  

The goal is to **maximize failure detection (recall)** while keeping operational costs under control.

---

##  Dataset

- **Name:** AI4I 2020 Predictive Maintenance Dataset  
- **Source:** Kaggle  
- **Link:**  
  https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification

### Main Features
- Air temperature  
- Process temperature  
- Rotational speed  
- Torque  
- Tool wear  
- Product type (`L`, `M`, `H`)

<small> The dataset is **not included** in this repository. </small>

---

##  Methodology

###  Data Preparation
- Removed non-informative identifiers (`Product ID`)
- One-hot encoded categorical variable (`Type`)
- Stratified train/test split
- Explicit handling of class imbalance

---

###  Models
- **Baseline:** Logistic Regression (`class_weight="balanced"`)
- **Final model:** XGBoost Classifier (tuned)

---

##  Model Performance

### Confusion Matrix (Final Model)

<img width="709" height="530" alt="image" src="https://github.com/user-attachments/assets/9c53ead4-d6da-413d-a207-b52536dc64bc" />

### Confusion Matrix Summary

| Metric | Value |
|------|------|
| True Positives (TP) | 66 |
| True Negatives (TN) | 1932 |
| False Positives (FP) | 0 |
| False Negatives (FN) | 2 |

---

### Key Metrics

| Metric | Value |
|------|------|
| Recall (Failure) | **97.1%** |
| Precision (Failure) | **100%** |
| F1-score | **0.985** |
| ROC-AUC | **0.98** |
| PR-AUC (Average Precision) | **0.97** |

---

##  ROC & Precision–Recall Curves

<img width="554" height="536" alt="image" src="https://github.com/user-attachments/assets/662bad7a-1c01-4f96-a8e0-973d850e16ca" />


<img width="549" height="532" alt="image" src="https://github.com/user-attachments/assets/c42df4c9-5575-46a7-9e8f-e8aefa40c2bf" />


These curves confirm the model’s strong discriminative power and robustness in a highly imbalanced setting.

---

##  Threshold Optimization

Instead of using the default probability threshold (0.5), multiple thresholds were evaluated.

<img width="663" height="478" alt="image" src="https://github.com/user-attachments/assets/6bdddd49-3355-47d7-adfc-8c644222e2a7" />

### Threshold Performance Summary

| Threshold | Precision | Recall | F1-score |
|---------|-----------|--------|----------|
| 0.10 | 0.60 | 0.97 | 0.74 |
| 0.15 | 0.93 | 0.97 | 0.95 |
| **0.20** | **1.00** | **0.97** | **0.985** |
| 0.50 | 1.00 | 0.97 | 0.985 |

---

##  Cost-Sensitive Analysis

To align the model with real-world maintenance decisions, a **cost-based evaluation** was performed.

### Cost Assumptions
- **False Positive (FP):** 300 units  
- **False Negative (FN):** 80,000 units  

### Cost Results

| Threshold | FP | FN | Total Cost |
|---------|----|----|------------|
| 0.20 | 0 | 2 | **160,000** |
| 0.35 | 0 | 2 | 160,000 |
| 0.50 | 0 | 2 | 160,000 |
| 0.70 | 0 | 2 | 160,000 |

Across a wide range of thresholds, the operational cost remains constant, indicating a **robust and stable model**.

---

##  Final Threshold Decision

The final threshold was set to **0.20**, as it is the **lowest threshold that eliminates false positives** while maintaining maximum recall.

This ensures **early failure detection** without increasing operational costs or triggering unnecessary maintenance actions.

---

##  Model Explainability (SHAP)


<img width="512" height="410" alt="image" src="https://github.com/user-attachments/assets/4d946213-3862-45e3-83f2-2af8c798bc26" />


### Key Insights
- **Tool wear** is the strongest driver of failures
- **Torque and rotational speed** show non-linear interactions
- Failure-type indicators (PWF, HDF, OSF, TWF) dominate risk signals
- Product type has a secondary but consistent effect

These insights align with expected physical behavior and support actionable maintenance planning.

---

##  Key Takeaways

- Predictive maintenance is a **risk management problem**, not an accuracy problem
- Threshold selection is critical in imbalanced industrial datasets
- Cost-sensitive evaluation bridges ML performance and business impact
- Explainability is essential for real-world adoption

---

##  How to Run

```bash
git clone https://github.com/Oscar-Jiram/Predictive-Maintenance-Machine-Learning.git
cd Predictive-Maintenance-Machine-Learning
pip install -r requirements.txt
jupyter notebook ML_AI4I2020.ipynb
```
## Future Improvements

Time-aware cross-validation

Cost-optimized training

Deployment as an API

Real-time monitoring dashboard

## Author

Oscar Castro

Industrial Automation & Data Analytics

Focus on Predictive Maintenance and Applied Machine Learning

<small> The trained model artifact is intentionally excluded; results are fully reproducible via the notebook. </small>

