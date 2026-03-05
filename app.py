import streamlit as st
import pickle
import pandas as pd

# Load trained model

model = pickle.load(open("churn_model.pkl", "rb"))

# Page title

st.title("🍔 Food Delivery Customer Churn Prediction")
st.caption("Enter customer details to estimate churn probability.")

st.divider()

# -----------------------

# CUSTOMER INFORMATION

# -----------------------

st.subheader("Customer Information")

col1, col2 = st.columns(2)

with col1:
gender = st.selectbox("Gender", ["Male", "Female"])
city = st.selectbox("City", ["Bangalore", "Delhi", "Mumbai", "Other"])

with col2:
age = st.number_input("Age", min_value=18, max_value=60, step=1)
payment_method = st.selectbox(
"Payment Method",
["Credit Card", "Debit Card", "UPI", "Cash", "Other"]
)

st.divider()

# -----------------------

# CUSTOMER ACTIVITY

# -----------------------

st.subheader("Customer Activity")

col3, col4 = st.columns(2)

with col3:
order_frequency = st.number_input(
"Order Frequency per Month",
min_value=0,
max_value=30,
step=1
)

```
loyalty_points = st.number_input(
    "Loyalty Points",
    min_value=0,
    max_value=1000,
    step=10
)
```

with col4:
days_since_last_order = st.number_input(
"Days Since Last Order",
min_value=0,
max_value=60,
step=1
)

rating = st.radio("Customer Rating", [1, 2, 3, 4, 5])

st.divider()

# -----------------------

# PREDICTION BUTTON

# -----------------------

predict_button = st.button("🔍 Predict Churn")

if predict_button:

```
input_dict = {
    "age": [age],
    "order_frequency": [order_frequency],
    "loyalty_points": [loyalty_points],
    "days_since_last_order": [days_since_last_order],
    "rating": [rating],
    "gender_Male": [1 if gender == "Male" else 0],
    "city_Bangalore": [1 if city == "Bangalore" else 0],
    "city_Delhi": [1 if city == "Delhi" else 0],
    "city_Mumbai": [1 if city == "Mumbai" else 0],
    "payment_method_Credit Card": [1 if payment_method == "Credit Card" else 0],
    "payment_method_Debit Card": [1 if payment_method == "Debit Card" else 0],
    "payment_method_UPI": [1 if payment_method == "UPI" else 0],
    "payment_method_Other": [1 if payment_method == "Other" else 0],
}

input_df = pd.DataFrame(input_dict)

# Ensure column order matches model training
model_columns = model.feature_names_in_
input_df = input_df.reindex(columns=model_columns, fill_value=0)

# Model prediction
prediction = model.predict(input_df)[0]
probability = model.predict_proba(input_df)[0][1]

# Risk classification
if probability < 0.3:
    risk = "Low Risk"
elif probability < 0.6:
    risk = "Medium Risk"
else:
    risk = "High Risk"

st.divider()
st.subheader("Prediction Result")

if prediction == 1:
    st.error(f"⚠ Customer is likely to churn (Probability: {probability*100:.2f}%)")
else:
    st.success(f"✅ Customer will stay (Probability of churn: {probability*100:.2f}%)")

st.write(f"**Risk Level:** {risk}")

# Visual probability bar
st.progress(float(probability))
```

