#  Predictive Maintenance using Machine Learning  
## AI4I 2020 Dataset

##  Project Overview

This project focuses on **predictive maintenance**, aiming to **predict machine failures before they occur** using supervised machine learning techniques.

The goal is to build, evaluate, and interpret models that can **learn failure patterns from sensor data**, helping reduce unplanned downtime and maintenance costs in industrial environments.

---

##  Problem Statement

Machine failures are **rare but costly events**, which creates a **highly imbalanced classification problem**.

**Target variable**
- `Machine failure`
  - `1` → Failure  
  - `0` → No failure  

The objective is to **maximize failure detection (recall)** while maintaining reasonable precision.

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

 The dataset is **not included** in this repository.  
Please download it directly from Kaggle.

---

##  Methodology

### 1. Data Preparation
- Removed non-informative identifiers (`Product ID`)
- Encoded categorical variable (`Type`)
- Train/test split with stratification
- Handled class imbalance

---

### 2. Baseline Model
**Logistic Regression**
- Feature scaling
- `class_weight="balanced"`
- Used as a performance benchmark

---

### 3. Tree-Based Model
**XGBoost Classifier**
- Handles non-linear relationships
- Captures feature interactions
- Hyperparameter tuning for improved recall

---

##  Evaluation Metrics

Due to class imbalance, the following metrics were used:

- **Recall (Failure class)** → primary metric
- Precision
- F1-score
- ROC-AUC
- Confusion Matrix

Accuracy was **not** used as the main metric.

---

##  Threshold Optimization

Instead of using the default `0.5` probability threshold:

- Multiple thresholds were evaluated
- Final threshold selected to **minimize false negatives**
- Business-oriented decision: missing a failure is more costly than a false alarm

---

##  Model Explainability (SHAP)

SHAP values were used to interpret model predictions.

### Key Insights
- **Tool wear** strongly increases failure probability
- **Torque and rotational speed** show non-linear interactions
- Certain product types present higher risk under specific conditions

These insights support **preventive maintenance decision-making**.

---

##  Results Summary

| Model | Recall (Failure) | Precision | F1-score |
|------|------------------|-----------|----------|
| Logistic Regression | Baseline | Baseline | Baseline |
| XGBoost (Tuned) | Improved | Improved | Improved |

*(Exact values are reported in the notebook)*

---

##  How to Run

```bash
git clone https://github.com/Oscar-Jiram/Predictive-Maintenance-Machine-Learning.git
cd Predictive-Maintenance-Machine-Learning
pip install -r requirements.txt

##  Key Takeaways

Predictive maintenance is a risk management problem, not an accuracy problem

Threshold tuning is critical in imbalanced industrial datasets

Interpretability is essential for real-world adoption

##  Future Improvements

Cross-validation with time-aware splits

Cost-sensitive learning

Model deployment (API)

Real-time monitoring dashboard

##  Author

Oscar Castro
Background in Industrial Automation & Data Analytics
Focus on manufacturing analytics, predictive maintenance, and applied ML
