import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

df = pd.read_csv("D:\CSI Assignments\AssignmentWeek7\model\House Price Prediction Dataset.csv")
df = df.drop(columns=["Id"])

X = df.drop("Price", axis=1)
y = df["Price"]

categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
], remainder="passthrough")

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor(n_estimators=100, random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline.fit(X_train, y_train)

joblib.dump(pipeline, "trained_model.pkl")
print("Model saved as trained_model.pkl")