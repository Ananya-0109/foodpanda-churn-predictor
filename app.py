import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("churn_model.pkl", "rb"))

st.set_page_config(page_title="Customer Churn Predictor", page_icon="🍔")

st.markdown(
    "<h1 style='white-space: nowrap;'>🍔 Food Delivery Customer Churn Prediction</h1>",
    unsafe_allow_html=True
)
st.write("---")

# ---------------- USER INPUT ---------------- #

st.subheader("Customer Information")

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox("Gender", ["Male", "Female"])

    city = st.selectbox(
        "City",
        ["Bangalore", "Delhi", "Mumbai", "Other"]
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=60,
        value=25,
        step=1
    )

    rating = st.selectbox(
        "Customer Rating",
        [1, 2, 3, 4, 5]
    )

with col2:

    payment_method = st.selectbox(
        "Payment Method",
        ["Credit Card", "Debit Card", "UPI", "Cash", "Other"]
    )

    order_frequency = st.number_input(
        "Order Frequency per Month",
        min_value=0,
        max_value=30,
        value=5,
        step=1
    )

    loyalty_points = st.number_input(
        "Loyalty Points",
        min_value=0,
        max_value=1000,
        value=100,
        step=10
    )

    days_since_last_order = st.number_input(
        "Days Since Last Order",
        min_value=0,
        max_value=60,
        value=7,
        step=1
    )

st.write("---")

# ---------------- PREDICTION ---------------- #

if st.button("🔍 Predict Churn"):

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

    # Ensure same feature order as training
    model_columns = model.feature_names_in_
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    # Predict probability
    probability = model.predict_proba(input_df)[0][1]

    # Prediction
    prediction = 1 if probability > 0.5 else 0

    # Risk category
    if probability < 0.3:
        risk = "Low Risk"
    elif probability < 0.6:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠ Customer is likely to churn")
    else:
        st.success("✅ Customer will stay")

    st.write(f"### Churn Probability: {probability*100:.2f}%")

    st.progress(float(probability))

    st.write(f"**Risk Level:** {risk}")


