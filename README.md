# Customer Churn Prediction Web Application

This project predicts customer churn using a machine learning model integrated into a web application built with Flask.
It allows users to input customer information and receive real-time predictions about whether the customer is likely to leave (churn) or stay.

## Project Structure

- `churn.ipynb` — Jupyter Notebook for data preprocessing, model training, and saving the trained model.
- `app.py` — Flask backend for handling requests and serving HTML pages.
- `templates/home.html` — Frontend form for inputting customer information.
- `templates/result.html` — (not provided yet) Displays the prediction result.
- `knn_churn.pkl` — Pre-trained machine learning model saved using `joblib`.

## How It Works

1. Users fill in customer information (credit score, geography, gender, age, etc.) through a web form.
2. The Flask app processes the input, prepares the feature vector, and sends it to the trained model.
3. The model predicts whether the customer will churn or not.
4. The result is displayed on a results page.
