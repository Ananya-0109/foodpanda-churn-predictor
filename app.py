import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("churn_model.pkl", "rb"))

st.set_page_config(page_title="Customer Churn Predictor", page_icon="🍔", layout="centered")

st.title("🍔 Food Delivery Customer Churn Prediction")
st.write("Enter customer details to predict whether a customer will churn.")

st.write("---")

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

# ⭐ STAR RATING SYSTEM

st.markdown("### ⭐ Customer Rating")

star_cols = st.columns(5)

if "rating" not in st.session_state:
    st.session_state.rating = 3

for i in range(5):
    with star_cols[i]:
        if st.button("⭐", key=i):
            st.session_state.rating = i + 1

rating = st.session_state.rating

stars_display = "⭐" * rating + "☆" * (5 - rating)
st.markdown(f"<h3 style='color:#ffb400'>{stars_display}</h3>", unsafe_allow_html=True)

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

    model_columns = model.feature_names_in_
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    probability = model.predict_proba(input_df)[0][1]

    prediction = 1 if probability > 0.5 else 0

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

    st.write(f"**Churn Probability:** {probability*100:.2f}%")
    st.progress(float(probability))
    st.write(f"**Risk Level:** {risk}")
