# 🔐 Network Security – Phishing Website Detection

## 📌 Project Overview
This project focuses on detecting **phishing websites** using machine learning techniques.  
Phishing websites are fraudulent sites designed to steal sensitive user information such as login credentials and financial data.

The goal of this project is to build a **robust, leakage-free, end-to-end machine learning pipeline** for phishing detection following industry best practices.

---

## 🎯 Problem Statement
To classify websites as:
- **Legitimate (1)**
- **Phishing (-1)**

based on URL structure, domain information, HTML/JavaScript behavior, and traffic-related features.

This is a **binary classification problem**.

---

## 📂 Dataset Information
- Dataset: **Phishing Websites Dataset (UCI Repository)**
- Total records (raw): ~11,000  
- Records after deduplication: ~5,800  
- Features: 30 rule-based features  
- Target column: `Result`

### Feature Encoding
All features are **ternary encoded**:
- `1` → Legitimate signal  
- `0` → Suspicious  
- `-1` → Phishing signal  

---

## 🧪 Exploratory Data Analysis (EDA)
The following EDA checks were performed:
- Missing value analysis
- Duplicate record removal (to prevent data leakage)
- Feature value range validation
- Class imbalance analysis
- Data leakage prevention checks

EDA was primarily focused on **data quality and validation**, while model performance was assessed during the evaluation stage.

---

## 📊 Model Evaluation

Model performance was evaluated using the following metrics:

- **F1-score**
- **Precision**
- **Recall**
- **Confusion Matrix**
- **ROC–AUC Curve**
- **Precision–Recall Curve**

ROC–AUC was used to measure overall class separability, while the Precision–Recall curve was used to assess phishing detection quality, where false negatives are critical.


## ⚙️ Machine Learning Pipeline
The project follows a modular pipeline architecture:

1. **Data Ingestion**
   - Data extraction from MongoDB
   - Duplicate removal
   - Stratified train-test split

2. **Data Validation**
   - Schema validation
   - Feature range checks
   - Leakage prevention checks

3. **Data Transformation**
   - Imputation for robustness
   - Feature preparation using pipelines

4. **Model Training**
   - Supervised classification models
   - Pipeline-based training

---



## 🧠 Key ML Concepts Used
- Stratified train-test split
- Data leakage prevention
- Pipeline-based preprocessing
- Model evaluation using classification metrics
- Threshold-independent evaluation (ROC–AUC, PR curve)

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- MongoDB
- Docker
- Fastapi

---

## 🚀 How to Run the Project

```bash
git clone https://github.com/Narenyadav0929/NetworkSecurity.git
cd NetworkSecurity
pip install -r requirements.txt
python main.py
