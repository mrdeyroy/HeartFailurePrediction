from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict_devtown_proj', methods=["POST"]) # methods=["POST"] -> i will values from the user and return values to my html page
def predict():
    if request.method == "POST":
        try:
            # Get values from form input
            features = [float(request.form[key]) for key in request.form]
            
            # Convert to NumPy array and reshape
            input_data = np.array(features).reshape(1, -1)
            
            # Scale the input
            input_scaled = scaler.transform(input_data)
            
            # Predict
            prediction = model.predict(input_scaled)[0]
            result = "High risk of death" if prediction == 1 else "Low risk of death"
            
            return render_template("index.html", result=result)
        
        except Exception as e:
            return render_template("index.html", result="Error: Invalid input!")

if __name__ == "__main__":
    app.run(debug=True,port=5000)

