import pandas as pd
df = pd.read_csv('D:\\devoix solution\\Task_02_AI_ML\\Dataset\\Churn_Modelling.csv')
print(df.shape)
print(df.info())
print(df.head())
print(df.isnull().sum())
print(df.duplicated().sum())


# Remove unnecessary columns
df = df.drop(columns=["RowNumber", "CustomerId", "Surname"])

print(df.head())
print(df.shape)

# Split the dataset into features and target variable
X = df.drop("Exited", axis=1)
y = df["Exited"]

print("Features:")
print(X.columns)
print("\nTarget:")
print(y.name)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

categorical_cols = ["Geography", "Gender"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
    ],
    remainder="passthrough"
)

X_encoded = preprocessor.fit_transform(X)

print("Original shape:", X.shape)
print("Encoded shape:", X_encoded.shape)


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X_encoded)

print("Scaled shape:", X_scaled.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training features:", X_train.shape)
print("Testing features:", X_test.shape)
print("Training target:", y_train.shape)
print("Testing target:", y_test.shape)


from sklearn.linear_model import LogisticRegression
import time

start_time = time.time()

log_model = LogisticRegression(random_state=42)
log_model.fit(X_train, y_train)

log_train_time = time.time() - start_time
print("Logistic Regression trained successfully")
print("Training time:", log_train_time, "seconds")


from sklearn.tree import DecisionTreeClassifier

start_time = time.time()

tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)

tree_train_time = time.time() - start_time

print("Decision Tree trained successfully")
print("Training time:", tree_train_time, "seconds")


from sklearn.ensemble import RandomForestClassifier

start_time = time.time()

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_train_time = time.time() - start_time

print("Random Forest trained successfully")
print("Training time:", rf_train_time, "seconds")

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

models = {
    "Logistic Regression": log_model,
    "Decision Tree": tree_model,
    "Random Forest": rf_model
}

results = []

for name, model in models.items():

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    })

    print("\n", name)
    print("Accuracy :", accuracy)
    print("Precision:", precision)
    print("Recall   :", recall)
    print("F1 Score :", f1)
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    comparison_df = pd.DataFrame(results)

comparison_df["Training Time"] = [
    log_train_time,
    tree_train_time,
    rf_train_time
]

print(comparison_df)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))

sns.barplot(
    data=comparison_df,
    x="Model",
    y="F1 Score"
)

plt.title("Model Comparison - F1 Score")
plt.ylabel("F1 Score")
plt.xlabel("Model")
plt.tight_layout()
plt.show()




from sklearn.metrics import ConfusionMatrixDisplay

for name, model in models.items():
    y_pred = model.predict(X_test)

    ConfusionMatrixDisplay.from_predictions(
        y_test,
        y_pred,
        cmap="Blues"
    )

    plt.title(f"{name} - Confusion Matrix")
    plt.tight_layout()
    plt.show()


    comparison_df.to_csv("model_comparison.csv", index=False)

print("\nFinal Model Comparison:")
print(comparison_df)

print("\nBest Model:")
best_model = comparison_df.loc[
    comparison_df["F1 Score"].idxmax(), "Model"
]

print(best_model)


from sklearn.model_selection import GridSearchCV

param_grid = {
    "n_estimators": [50, 100, 150],
    "max_depth": [None, 10, 20],
    "min_samples_split": [2, 5]
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=3,
    scoring="f1",
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

print("Best Parameters:")
print(grid_search.best_params_)

print("\nBest CV F1 Score:")
print(grid_search.best_score_)


best_rf = grid_search.best_estimator_

y_pred_tuned = best_rf.predict(X_test)

print("Tuned Random Forest Results")
print("Accuracy :", accuracy_score(y_test, y_pred_tuned))
print("Precision:", precision_score(y_test, y_pred_tuned))
print("Recall   :", recall_score(y_test, y_pred_tuned))
print("F1 Score :", f1_score(y_test, y_pred_tuned))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred_tuned))