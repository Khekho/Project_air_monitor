import pandas as pd
import numpy as np
import requests
import threading
import tkinter as tk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# ThingSpeak API Details
READ_CHANNEL_ID = "2832937"
READ_API_KEY = "VKI0C26TRO2SBZ4E"
WRITE_CHANNEL_ID = "2845953"
WRITE_API_KEY = "CJ8X1B5TQL18GG8E"

FIELD_MAPPING = {
    "dust_density": "field1",
    "co2": "field2",
    "nh3": "field3",
    "smoke": "field4",
    "co": "field5",
    "temperature": "field6",
    "humidity": "field7"
}

running = False  # Flag to control the loop

def fetch_and_predict():
    global running
    while running:
        url = f"https://api.thingspeak.com/channels/{READ_CHANNEL_ID}/feeds.csv?api_key={READ_API_KEY}&results=100"
        df = pd.read_csv(url)

        # Extract relevant fields
        data = df[list(FIELD_MAPPING.values())].dropna().astype(float)

        # Create a model for each field to predict
        predictions = {}
        for field_name, field_column in FIELD_MAPPING.items():
            X = data.drop(columns=[field_column])  # Input: All other fields
            Y = data[field_column]  # Output: Field to predict

            # Split Data
            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

            # Train Model
            model = LinearRegression()
            model.fit(X_train, Y_train)

            # Predict tomorrow's value for the field
            tomorrow_input = np.array([X.iloc[-1]])  # Using latest data as reference
            predicted_value = model.predict(tomorrow_input)

            predictions[field_name] = round(predicted_value[0], 2)  # Round for readability

        # Print the predicted values for all fields
        for field, value in predictions.items():
            print(f"Predicted {field} for Tomorrow: {value:.2f}")

        # Send Predictions to ThingSpeak
        write_url = f"https://api.thingspeak.com/update?api_key={WRITE_API_KEY}"
        payload = {
            "field1": predictions.get("dust_density", ""),
            "field2": predictions.get("co2", ""),
            "field3": predictions.get("nh3", ""),
            "field4": predictions.get("smoke", ""),
            "field5": predictions.get("co", ""),
            "field6": predictions.get("temperature", ""),
            "field7": predictions.get("humidity", ""),
                    }
        response = requests.get(write_url, params=payload)

        if response.status_code == 200 and response.text != "0":
            print("Predictions successfully saved to ThingSpeak!")
        else:
            print("Failed to update ThingSpeak:", response.text)
        
        threading.Event().wait(30)  # Wait for 5 seconds

def start():
    global running
    if not running:
        running = True
        threading.Thread(target=fetch_and_predict, daemon=True).start()

def stop():
    global running
    running = False

# GUI Setup
root = tk.Tk()
root.title("ThingSpeak Prediction")

tk.Button(root, text="Start", command=start).pack(pady=10)
tk.Button(root, text="Stop", command=stop).pack(pady=10)

tk.Label(root, text="Click Start to begin prediction every 30 sec").pack(pady=10)

root.mainloop()
