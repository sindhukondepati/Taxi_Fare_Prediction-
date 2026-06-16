from flask import Flask, request, render_template
import numpy as np
import joblib
import os

app = Flask(__name__, static_folder='static')

# Load trained model and scaler
model_path = "taxi_fare_model.pkl"
scaler_path = "scaler.pkl"

if os.path.exists(model_path) and os.path.exists(scaler_path):
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    print("✅ Model & Scaler loaded from files.")
else:
    print("❌ Model files not found. Run 'model.py' first!")
    exit()

# Define features
features = ["trip_duration", "distance_traveled", "num_of_passengers", "surge_applied"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        trip_duration = float(request.form['trip_duration'])
        distance_traveled = float(request.form['distance_traveled'])
        num_of_passengers = int(request.form['num_of_passengers'])
        surge_applied = float(request.form['surge_applied'])

        # Prepare input data
        input_data = np.array([[trip_duration, distance_traveled, num_of_passengers, surge_applied]])

        # Scale input data
        input_data_scaled = scaler.transform(input_data)

        # Predict fare
        predicted_fare = model.predict(input_data_scaled)[0]
        print(f"✅ Predicted Fare: {predicted_fare}")

        # Return result as text, no JSON
        return render_template('index.html', fare=round(predicted_fare, 2))

    except Exception as e:
        print("❌ Error in prediction:", str(e))
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
