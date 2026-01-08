# 🔐 Network Security – Phishing Website Detection

An end-to-end machine learning project focused on detecting phishing websites using structured URL and website behavior features.  
The project is designed with strong emphasis on data leakage prevention, modular ML pipelines, and automated deployment following industry best practices.

---

## 📌 Project Overview

Phishing websites are fraudulent sites created to steal sensitive user information such as login credentials and financial data.  
This project aims to classify websites as legitimate or phishing using machine learning techniques and a production-ready pipeline.

The solution covers the complete ML lifecycle:
- Data ingestion and validation
- Exploratory data analysis (EDA)
- Feature engineering and model training
- Model evaluation using classification metrics
- Dockerized deployment with CI/CD automation

---

## 🎯 Problem Statement

Classify websites into two categories:

- Legitimate (1)
- Phishing (-1)

based on:
- URL structure
- Domain-based features
- HTML & JavaScript behavior
- Traffic-related signals

This is a binary classification problem where minimizing false negatives (missed phishing sites) is critical.

---

## 📂 Dataset Information

- Dataset: Phishing Websites Dataset (UCI Repository)
- Raw records: ~11,000
- Records after deduplication: ~5,800
- Features: 30 rule-based features
- Target column: Result

### Feature Encoding

All features are ternary encoded:
- 1 → Legitimate signal
- 0 → Suspicious
- -1 → Phishing signal

---

## 🧪 Exploratory Data Analysis (EDA)

EDA was focused on data quality and validation rather than visualization.

Key checks performed:
- Missing value analysis
- Duplicate record removal to prevent data leakage
- Feature value range validation
- Class imbalance analysis
- Data leakage prevention checks

Model performance evaluation was performed separately during the model evaluation stage.

---

## 📊 Model Evaluation

Model performance was evaluated using the following metrics:
- F1-score
- Precision
- Recall
- Confusion Matrix
- ROC–AUC Curve
- Precision–Recall Curve

ROC–AUC was used to measure overall class separability, while the Precision–Recall curve was used to assess phishing detection quality where false negatives are critical.

---

## ⚙️ Machine Learning Pipeline

The project follows a modular pipeline-based architecture:

### Data Ingestion
- Data extraction from MongoDB
- Duplicate removal
- Stratified train-test split

### Data Validation
- Schema validation
- Feature range checks
- Leakage prevention checks

### Data Transformation
- Imputation for robustness
- Pipeline-based feature preparation

### Model Training
- Supervised classification models
- Pipeline-based training to prevent leakage

---

## 🧠 Key ML & MLOps Concepts Used

- Stratified train-test split
- Data leakage prevention
- Pipeline-based preprocessing
- Classification model evaluation
- Threshold-independent metrics (ROC–AUC, Precision–Recall)
- Modular and reusable ML components

---

## 🔄 CI/CD Workflow (GitHub Actions)

This project includes a complete CI/CD pipeline using GitHub Actions, Docker, and AWS.

### Workflow Highlights
- Triggered automatically on every push to the main branch
- Docker image is built and pushed to Amazon ECR
- Deployment handled via a self-hosted runner
- Existing containers are safely stopped and replaced
- Application runs on port 8080 with restart policies enabled

### Benefits
- Fully automated deployment
- No manual intervention
- Production-ready ML workflow
- Demonstrates real-world MLOps practices

---

## 🛠️ Tech Stack

### Programming & ML
- Python
- Pandas, NumPy
- Scikit-learn

### Backend & Deployment
- FastAPI
- Docker
- MongoDB

### Cloud & DevOps
- AWS ECR
- AWS EC2 (Self-hosted runner)
- GitHub Actions (CI/CD)

---

## 🚀 How to Run the Project Locally

```bash
git clone https://github.com/Narenyadav0929/NetworkSecurity.git
cd NetworkSecurity
pip install -r requirements.txt
python main.py


👤 Author

Narender Singh Yadav
Aspiring Data Analyst | Machine Learning Enthusiast
GitHub: https://github.com/Narenyadav0929