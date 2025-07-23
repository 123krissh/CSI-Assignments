
import joblib
import numpy as np
import pandas as pd

# Load model
def load_model(path="AssignmentWeek7/model/trained_model.pkl"):
    return joblib.load(path)

# Convert user input to DataFrame for prediction
def create_input_df(area, bedrooms, bathrooms, floors, garage, year_built, location, condition):
    return pd.DataFrame([{
        "Area": area,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Floors": floors,
        "Garage": garage,
        "YearBuilt": year_built,
        "Location": location,
        "Condition": condition
    }])
