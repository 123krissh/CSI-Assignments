import streamlit as st
import pandas as pd
from utils import load_model, create_input_df
import matplotlib.pyplot as plt
import seaborn as sns

# Load model
model = load_model("model/trained_model.pkl")
data = pd.read_csv("model/House Price Prediction Dataset.csv")

st.set_page_config(page_title="House Price Predictor", layout="centered")
st.title("🏡 House Price Prediction App")

st.sidebar.header("Enter House Details")

# Input widgets
area = st.sidebar.number_input("Area (sqft)", min_value=100, max_value=10000, step=10)
bedrooms = st.sidebar.selectbox("Bedrooms", [1, 2, 3, 4, 5])
bathrooms = st.sidebar.selectbox("Bathrooms", [1, 2, 3])
floors = st.sidebar.selectbox("Floors", [1, 2, 3])
garage = st.sidebar.radio("Garage", ["Yes", "No"])
year_built = st.sidebar.slider("Year Built", 1950, 2025, 2020)
location = st.sidebar.selectbox("Location", ["Urban", "Downtown", "Rural", "Suburban"])
condition = st.sidebar.selectbox("Condition", ["Excellent", "Good", "Fair", "Poor"])

# Predict
input_df = create_input_df(area, bedrooms, bathrooms, floors, garage, year_built, location, condition)

if st.sidebar.button("Predict Price 💸"):
    price = model.predict(input_df)[0]
    st.success(f"🏷️ **Estimated House Price: ₹ {price:,.2f}**")

    # Show input summary
    st.subheader("🔍 Your Input Summary")
    st.table(input_df)

    # Visualize similar homes
    st.subheader("📊 Similar Homes Comparison")
    similar = data[
        (data['Bedrooms'] == bedrooms) &
        (data['Bathrooms'] == bathrooms) &
        (data['Location'] == location)
    ]
    
    if not similar.empty:
        fig, ax = plt.subplots()
        sns.histplot(similar['Price'], kde=True, ax=ax)
        plt.axvline(price, color='red', linestyle='--', label="Predicted Price")
        ax.set_title("Price Distribution of Similar Homes")
        ax.set_xlabel("Price")
        plt.legend()
        st.pyplot(fig)
    else:
        st.info("No similar homes found in dataset for comparison.")
        