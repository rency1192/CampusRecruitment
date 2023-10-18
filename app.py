from flask import Flask, render_template, request, jsonify
import joblib  # Add this import
import tensorflow as tf
# Create a Flask app
app = Flask(__name__)

# Load your trained model
model = joblib.load('model.pkl')  # Load your saved model

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route to handle form submission and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        ssc_p = float(request.form['ssc_p'])
        hsc_p = float(request.form['hsc_p'])
        degree_p = float(request.form['degree_p'])
        workex = float(request.form['workex'])
        mba_p = float(request.form['mba_p'])
        etest_p = float(request.form['etest_p'])
        gender = float(request.form['gender'])
        degree_t = float(request.form['degree_t'])
        specialisation = float(request.form['specialisation'])

        # Preprocess input data (if necessary)

        # Pass input data to your machine learning model for prediction
        user_input = [[ssc_p, hsc_p, degree_p, workex, mba_p, etest_p, gender, degree_t, specialisation]]
        user_pred = model.predict(user_input)

        # Determine the prediction result
        if user_pred == 1:
            result = "The Candidate will be Placed!"
        else:
            result = "The Candidate won't be Placed :("

        # Return the prediction result to the frontend
        return render_template('result.html', prediction=result)

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
