# 🌍 Air Quality Monitoring & Prediction System

This project is a **complete web-based air quality dashboard** that integrates **real-time data monitoring** and **next-day prediction** using a backend machine learning model. It fetches environmental sensor data from **ThingSpeak**, predicts the next day's values, and displays both current and predicted metrics on a beautifully styled, responsive web interface.

---

## 📦 Project Structure

```

air-quality-dashboard/
├── index.html                 # Frontend dashboard
├── backend\_predictor.py       # Python ML backend using scikit-learn

````

---

## 🚀 Features

### 🌐 Frontend (HTML/CSS/JS)
- Responsive dashboard for 7 air quality metrics
- Toggle between real-time data and predictions
- Animated welcome splash screen with spinner
- Uses ThingSpeak for IoT data integration
- Mobile-friendly UI with clean typography (Poppins)

### 🧠 Backend (Python + ML)
- Fetches last 100 readings from ThingSpeak
- Trains a linear regression model for each parameter
- Predicts next-day values using the latest available data
- Pushes predictions back to ThingSpeak for frontend display
- Simple GUI (Tkinter) with Start/Stop buttons

---

## 📡 ThingSpeak Configuration

The system uses **two ThingSpeak channels**:

| Purpose       | Channel ID | API Key             |
|---------------|-------------|---------------------|
| Real-Time     | `2832937`   | `VKI0C26TRO2SBZ4E`  |
| Prediction    | `2845953`   | `CJ8X1B5TQL18GG8E` *(write)*<br>`JGXQBVVG6FVYHWX4` *(read)* |

---

## 📈 Supported Parameters

| Field        | ThingSpeak Field |
|--------------|------------------|
| Dust Density | field1           |
| CO₂          | field2           |
| NH₃          | field3           |
| Smoke        | field4           |
| CO           | field5           |
| Temperature  | field6           |
| Humidity     | field7           |

---

## 💻 How to Run

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/your-username/air-quality-dashboard.git
cd air-quality-dashboard
````

### 🔹 2. Run the Backend Prediction Script

Make sure you have the required libraries:

```bash
pip install pandas numpy scikit-learn requests
```

Then run the backend:

```bash
python backend_predictor.py
```

A GUI window will appear:

* Click **Start** to begin prediction every 30 seconds.
* Click **Stop** to end the loop.

> Note: Predictions will be sent to your ThingSpeak prediction channel.

### 🔹 3. Open the Frontend

Just open `index.html` in any browser. It automatically fetches:

* Real-time data by default
* Predicted data when "Predict" is toggled

---

## 📸 Screenshots

> Add your screenshots here (welcome screen, dashboard, prediction mode)

---

## ✅ Future Enhancements

* Use advanced ML models (Random Forest, LSTM)
* Add graphs to visualize trends
* Display prediction accuracy (e.g., RMSE)
* Real-time alerts for critical levels

---

## 🧑‍💻 Author

**Kishore Selvarajan**
💡 IoT Developer | 🌐 Web Developer
🔗 [LinkedIn](https://www.linkedin.com/in/your-profile) | [GitHub](https://github.com/your-username)

---

## 📄 License

MIT License – use freely and modify!

---

```

Let me know if you want me to bundle this into a ZIP or help set up GitHub Pages deployment for the frontend.
```
