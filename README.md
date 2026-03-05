##🍔 Food Delivery Customer Churn Prediction

This project is a Machine Learning web application that predicts whether a customer of a food delivery platform is likely to churn (stop using the service) based on their behavior and engagement with the platform.

The model analyzes factors such as order frequency, loyalty points, customer ratings, and recency of orders to estimate the probability of churn.

The application is deployed using Streamlit, allowing users to interactively input customer data and receive real-time churn predictions.


WEB APP LINK- https://foodpanda-churn-predictor-khqrvxutpfpayu6ey25ua5.streamlit.app/#churn-probability-0-48

📊 Problem Statement

Customer churn is a major challenge for food delivery platforms. Identifying customers who are likely to stop using the service allows businesses to:

Take preventive actions

Improve customer retention

Design targeted marketing strategies

This project demonstrates how machine learning can be used to predict customer churn based on behavioral patterns.
SCREENSHOTS OF THE WEB APP
<img width="1136" height="901" alt="image" src="https://github.com/user-attachments/assets/3a78e921-70d1-4525-a39a-c0d15a1347d9" />
Confusion Matrix
<img width="519" height="413" alt="image" src="https://github.com/user-attachments/assets/c2150a53-508f-4407-8b11-3f4cf727cdfb" />

⚙️ Features

Interactive Streamlit web application

Real-time churn prediction

Displays churn probability

Risk classification:

Low Risk

Medium Risk

High Risk

User-friendly two-column input layout

Visual probability progress bar

🧠 Machine Learning Model

The churn prediction model is trained using customer behavioral features including:

Age

Order Frequency

Loyalty Points

Days Since Last Order

Customer Rating

Gender

City

Payment Method

These features help simulate real-world customer engagement patterns used in churn prediction systems.

🛠 Tech Stack

Python

Pandas

Scikit-Learn

Streamlit

Pickle

📁 Project Structure
Food-Delivery-Churn-Prediction
│
├── app.py                # Streamlit web application
├── churn_model.pkl       # Trained ML model
├── requirements.txt      # Python dependencies
├── dataset.csv           # Dataset used for training
└── README.md             # Project documentation
🚀 How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/yourusername/food-delivery-churn-prediction.git
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the Streamlit app
streamlit run app.py
💡 Example Use Case

A business analyst can input customer information such as:

Order frequency

Customer rating

Loyalty points

Last order activity

The system then predicts:

Probability of churn

Risk level of the customer

This helps businesses identify at-risk customers and improve retention strategies.
