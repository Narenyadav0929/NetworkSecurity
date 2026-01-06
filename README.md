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
Key EDA steps performed:
- Missing value check (no missing values)
- Duplicate record removal (to prevent data leakage)
- Feature value range validation (`-1, 0, 1`)
- Class imbalance analysis (balanced after deduplication)
- Data leakage checks
- Visualization using:
  - Countplots
  - Boxplots
  - Pairplots (selected features)
  - Correlation heatmap (sanity check)

---

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
   - Imputation (future robustness)
   - Feature preparation using pipelines

4. **Model Training**
   - Classification models (Logistic Regression, Tree-based models)
   - Proper evaluation metrics

5. **Model Evaluation**
   - Confusion Matrix
   - ROC-AUC
   - Precision–Recall Curve

---

## 🧠 Key ML Concepts Used
- Stratified train-test split
- Data leakage prevention
- Pipeline-based preprocessing
- Feature importance analysis
- Rule-based feature interpretation

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Seaborn, Matplotlib
- MongoDB
- Docker

---

## 🚀 How to Run the Project

```bash
git clone https://github.com/Narenyadav0929/NetworkSecurity.git
cd NetworkSecurity
pip install -r requirements.txt
python main.py
