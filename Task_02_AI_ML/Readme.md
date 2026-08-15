

# Task 02 – Build and Compare Machine Learning Models

## 📌 Project Overview

This project focuses on developing and comparing multiple machine learning classification models for a real-world **Customer Churn Prediction** problem.

The objective is to predict whether a bank customer is likely to leave the bank based on customer information such as credit score, age, geography, balance, number of products, activity status, and estimated salary.

Three machine learning algorithms were trained and compared:

* Logistic Regression
* Decision Tree
* Random Forest

Hyperparameter tuning was also performed using GridSearchCV as a bonus task.

---

## 🎯 Objectives

* Load and explore a real-world dataset.
* Handle missing values and duplicate records.
* Remove irrelevant features.
* Encode categorical variables.
* Scale numerical features.
* Split the dataset into training and testing sets.
* Train multiple machine learning classification models.
* Evaluate models using appropriate classification metrics.
* Compare model performance.
* Perform hyperparameter tuning using GridSearchCV.
* Select the best-performing model.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn

---

## 📊 Dataset

The project uses a Bank Customer Churn dataset containing:

* **10,000 records**
* **14 original columns**

The identifier columns `RowNumber`, `CustomerId`, and `Surname` were removed because they were not useful for predicting customer churn.

After feature selection, the dataset contained:

* **10 input features**
* **1 target variable**

### Target Variable

`Exited`

* `0` → Customer stayed
* `1` → Customer exited

### Main Features

* CreditScore
* Geography
* Gender
* Age
* Tenure
* Balance
* NumOfProducts
* HasCrCard
* IsActiveMember
* EstimatedSalary

---

## 🔧 Data Preprocessing

The following preprocessing steps were performed:

1. Removed irrelevant identifier columns.
2. Checked for missing values.
3. Checked for duplicate records.
4. Encoded categorical features using One-Hot Encoding.
5. Scaled the processed features using StandardScaler.
6. Split the dataset into training and testing sets.

### Dataset Split

* Training records: **8,000**
* Testing records: **2,000**

After encoding:

* Feature shape: **10,000 × 13**

---

## 🤖 Machine Learning Models

### 1. Logistic Regression

Used as the baseline classification model because it is fast, simple, and suitable for binary classification.

### 2. Decision Tree

A tree-based classifier capable of learning nonlinear relationships between customer features and churn.

### 3. Random Forest

An ensemble learning algorithm that combines multiple decision trees to improve predictive performance and robustness.

---

## 📈 Model Evaluation

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

### Results

| Model               |   Accuracy |  Precision |     Recall |   F1 Score |
| ------------------- | ---------: | ---------: | ---------: | ---------: |
| Logistic Regression |     80.80% |     58.91% |     18.67% |     28.36% |
| Decision Tree       |     79.40% |     49.41% | **51.84%** |     50.60% |
| **Random Forest**   | **86.15%** | **76.42%** |     46.19% | **57.58%** |

Random Forest achieved the best overall performance based on Accuracy, Precision, and F1 Score.

---

## ⚙️ Hyperparameter Tuning

GridSearchCV was used to tune the Random Forest model.

### Best Parameters

```text
n_estimators = 100
max_depth = None
min_samples_split = 5
```

### Best Cross-Validation F1 Score

**58.37%**

### Tuned Random Forest Test Results

| Metric    | Result |
| --------- | -----: |
| Accuracy  | 86.20% |
| Precision | 76.95% |
| Recall    | 45.95% |
| F1 Score  | 57.54% |

The tuned model achieved slightly higher Accuracy and Precision, while its F1 Score remained almost unchanged compared with the original Random Forest.

---

## 🏆 Final Model

**Random Forest** was selected as the best overall model.

It achieved:

* **86.15% Accuracy**
* **76.42% Precision**
* **46.19% Recall**
* **57.58% F1 Score**

Although the Decision Tree achieved a higher Recall, Random Forest provided the best overall balance of evaluation metrics.

---

## 📁 Project Structure

```text
Task_02_AI_ML/
│
├── dataset/
├── Images/
├── Report/
├── main.py
├── model_comparison.csv
└── README.md
```

---

## 📌 Conclusion

This project demonstrates a complete machine learning workflow, including data preprocessing, feature encoding, scaling, train-test splitting, model development, evaluation, comparison, and hyperparameter tuning.

Among the tested models, Random Forest provided the strongest overall performance for predicting customer churn.

The project also demonstrates the importance of comparing multiple machine learning algorithms instead of relying on a single model.

---

## 👨‍💻 Project

**Task:** Task 02 – Build and Compare Machine Learning Models
**Problem:** Customer Churn Prediction
**Models:** Logistic Regression, Decision Tree, Random Forest
