# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Load datasets
train_df = pd.read_csv("C:/Users/sindh/Desktop/kill/train.csv")
test_df = pd.read_csv("C:/Users/sindh/Desktop/kill/test.csv")

# Define features and target variable
features = ["trip_duration", "distance_traveled", "num_of_passengers", "surge_applied"]
target = "total_fare"

# Drop missing values
train_df = train_df.dropna(subset=features + [target])

# Split dataset into features (X) and target (y)
X = train_df[features]
y = train_df[target]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the RandomForestRegressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate model
y_pred = model.predict(X_test_scaled)
accuracy = r2_score(y_test, y_pred)
print(f"✅ Model Accuracy (R² Score): {accuracy:.4f}")

# Function to predict fare (without using a pickle file)
def predict_fare():
    trip_duration = float(input("Enter trip duration (min): "))
    distance_traveled = float(input("Enter distance traveled (km): "))
    num_of_passengers = int(input("Enter number of passengers: "))
    surge_applied = float(input("Enter surge multiplier: "))

    # Prepare input data
    input_data = np.array([[trip_duration, distance_traveled, num_of_passengers, surge_applied]])
    
    # Scale the input data
    input_scaled = scaler.transform(input_data)
    
    # Predict fare
    predicted_fare = model.predict(input_scaled)[0]
    
    print(f"🚕 Predicted Fare: ${round(predicted_fare, 2)}")

# Run the prediction function
predict_fare()
