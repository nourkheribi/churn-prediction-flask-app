from flask import Flask, render_template, request
import joblib 
import numpy as np

model = joblib.load('knn_churn.pkl')

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form inputs
    credit_score = int(request.form['creditscore'])
    geography = request.form['geography'].lower()
    gender = request.form['gender'].lower()
    age = int(request.form['age'])
    tenure = int(request.form['tenure'])
    balance = float(request.form['balance'])
    num_of_products = int(request.form['numofproducts'])
    has_card = 1 if request.form['Card'] == 'yes' else 0
    is_active_member = 1 if request.form['Active member'] == 'yes' else 0
    estimated_salary = float(request.form['estimatedsalary'])

    # Correct Encoding
    geography_mapping = {'france': 0, 'germany': 1, 'spain': 2}
    geography_encoded = geography_mapping.get(geography, 0)  # Default France=0

    gender_encoded = 1 if gender == 'male' else 0  # Male = 1, Female = 0

    # Build input vector (now matching 10 features)
    input_vector = np.array([[credit_score, geography_encoded, gender_encoded, age, tenure, balance, num_of_products, has_card, is_active_member, estimated_salary]])

    # Predict
    prediction = model.predict(input_vector)[0]

    # Interpretation
    result = "This customer is likely to churn." if prediction == 1 else "This customer is likely to stay."

    return render_template('result.html', prediction=result)


if __name__ == '__main__':
    app.run(debug=True)