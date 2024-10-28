# Fraud Detection for E-commerce and Banking

This project leverages machine learning to detect fraudulent transactions in e-commerce and banking, aiding in proactive security and risk management. The goal is to provide a robust fraud detection pipeline with explainability, deployment, and dashboard visualization for actionable insights.

---

## Project Overview

### Key Features
- **Data Analysis & Preprocessing**: Handling missing values, data cleaning, and feature engineering for fraud detection.
- **Model Building & Training**: Comparison of multiple models, including deep learning architectures (CNN, RNN, LSTM).
- **Explainability**: Interpretation using SHAP and LIME for feature influence insights.
- **Deployment**: API service for real-time fraud predictions via Flask, Dockerized for scalability.
- **Dashboard**: Interactive visualization of fraud insights using Dash.

---

## Project Directory Structure

The repository is organized as follows:

- **`.github/workflows/`**: Contains GitHub Actions for CI/CD and automated testing.
- **`.vscode/`**: Development configuration for Visual Studio Code.
- **`fraud-detection-api/`**: REST API implementation for serving fraud detection models.
- **`fraud-dashboard/`**: Dash application for real-time fraud data visualization.
- **`notebooks/`**: Jupyter notebooks for data exploration, feature engineering, and model prototyping.
- **`scripts/`**: Scripts for data preprocessing, visualization, and model building.
- **`tests/`**: Unit tests for model integrity and data processing functions.

---

## Installation

Follow these steps to set up and run the project locally:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/epythonlab/fraud-detection.git
   cd fraud-detection
   ```

2. **Set Up a Virtual Environment**

   **For Linux/MacOS:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   **For Windows:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

---

## Project Tasks and Workflow

### Task 1 - Data Analysis and Preprocessing
- **Handling Missing Values**: Imputation or removal of missing data.
- **Data Cleaning**: Removing duplicates and correcting data types.
- **Exploratory Data Analysis (EDA)**:
  - Univariate and bivariate analysis.
- **Geolocation Analysis**: 
  - Convert IP addresses to integers.
  - Merge `Fraud_Data.csv` with `IpAddress_to_Country.csv`.
- **Feature Engineering**:
  - Transaction frequency and velocity.
  - Time-based features (hour of day, day of week).
- **Normalization and Scaling**
- **Encoding Categorical Features**

### Task 2 - Model Building and Training
- **Data Preparation**: Feature and target separation, and train-test split.
- **Model Selection**:
  - Classical models: Logistic Regression, Decision Tree, Random Forest.
  - Advanced models: Gradient Boosting, MLP, CNN, RNN, LSTM.
- **Model Training and Evaluation**:
  - Train on both `creditcard` and `Fraud_Data` datasets.
- **MLOps**: 
  - Use MLflow for versioning, experiment tracking, and model comparison.

### Task 3 - Model Explainability
- **SHAP (SHapley Additive exPlanations)**:
  - Explain feature importance using SHAP summary, force, and dependence plots.
- **LIME (Local Interpretable Model-agnostic Explanations)**:
  - Generate feature importance plots for individual predictions.

### Task 4 - Model Deployment and API Development
- **Setting Up the Flask API**:
  - Serve models via Flask in `serve_model.py`.
- **Dockerization**:
  - Create a Docker container for the API with a `Dockerfile`.
  - Run the container with:
    ```bash
    docker build -t fraud-detection-model .
    docker run -p 5000:5000 fraud-detection-model
    ```
- **Logging**:
  - Use Flask-Logging to monitor requests and track predictions.

### Task 5 - Dashboard Development with Flask and Dash
- **Interactive Dashboard**:
  - Visualize fraud insights (transaction count, fraud cases, geographic data).
  - Use Dash to create charts (line, bar) and summary boxes for fraud trends.
  - Set up a Flask endpoint to serve fraud data for the Dash front end.
    ![image](https://github.com/user-attachments/assets/6e303f9a-90be-42b9-9734-78a0f9a0c2f7)
    ![image](https://github.com/user-attachments/assets/3eca58d5-d3ce-4654-88b9-3b6c759ef4dd)
    ![image](https://github.com/user-attachments/assets/d9b58a11-2e3e-4986-b904-0c1189546436)




---

## Contributing

We welcome contributions to enhance the project:

1. Fork the repository and create a new branch.
2. Make changes with clear, descriptive commit messages.
3. Submit a pull request with a detailed explanation.

---

