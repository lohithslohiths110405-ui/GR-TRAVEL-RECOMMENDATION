

# 🌱 Green Route – Carbon Efficient Travel Recommender

A smart travel recommendation system that suggests the most **eco-friendly transportation mode** between two cities based on **carbon emissions**.

This project helps users make sustainable travel decisions by comparing emissions across different transport options like bike, car, bus, train, and flight.

---

## 🚀 Features

* 🌍 Select **source and destination cities**
* 📏 Calculates **distance between locations**
* 🚗 Compares multiple transportation modes:

  * Bike
  * Car
  * Bus
  * Train
  * Flight
* 🌱 Recommends the **lowest carbon emission option**
* 📊 Visualizes emissions using charts (Streamlit UI)
* 🌐 Includes both:

  * **Streamlit App (interactive UI)**
  * **Flask Web App (HTML-based UI)**

---

## 🧠 How It Works

1. The system reads route data from a dataset (`routes_dataset.csv`)
2. It calculates emissions using predefined **emission factors**
3. Formula used:

```text
Emission (kg CO₂) = Distance (km) × Emission Factor
```

4. The transport mode with the **lowest emission** is recommended

---

## 🤖 Model Details

The Green Route system uses a **hybrid approach** combining **rule-based logic** and an optional **machine learning model**.

---

### 🔹 1. Rule-Based System (Core Logic)

The primary recommendation is generated using a deterministic formula:

```text
Emission (kg CO₂) = Distance (km) × Emission Factor
```

* Each transport mode has a predefined emission factor
* Emissions are calculated for all modes
* The mode with the **minimum emission** is selected

#### ✅ Advantages

* Simple and interpretable
* Fast execution
* No training required
* Works even with limited data

---

### 🔹 2. Machine Learning Model (Optional)

A trained model (`emission_model.pkl`) is included to enhance predictions using data-driven insights.

---

### 🔹 3. Input Features

The ML model can use:

* Distance between cities
* Transport mode (encoded)
* Route-related attributes
* (Future) Traffic and environmental conditions

---

### 🔹 4. Output

The model can:

* Predict **carbon emission values**, OR
* Recommend the **best transport mode**

---

### 🔹 5. Algorithms Used

Depending on implementation (from notebooks):

* Linear Regression → emission prediction
* Decision Tree / Random Forest → improved accuracy
* Classification models → transport recommendation

---

### 🔹 6. Model Training Process

1. **Data Collection**

   * Dataset: `routes_dataset.csv`

2. **Data Preprocessing**

   * Handling missing values
   * Encoding categorical variables
   * Feature scaling (if required)

3. **Train-Test Split**

   * Splitting dataset into training and testing sets

4. **Model Training**

   * Training using historical travel and emission data

5. **Evaluation Metrics**

   * Mean Absolute Error (MAE)
   * Mean Squared Error (MSE)
   * Accuracy (for classification)

---

### 🔹 7. Model Workflow

```text
Input (Source, Destination)
        ↓
Fetch Distance from Dataset
        ↓
Calculate Emissions (Rule-Based)
        ↓
(Optional) ML Model Prediction
        ↓
Compare Results
        ↓
Recommend Best Transport Mode
```

---

### 🔹 8. Limitations

* Depends on dataset quality
* Limited generalization with small datasets
* Requires retraining for updated data

---

### 🔹 9. Future Improvements

* 📡 Real-time API integration (Google Maps, traffic)
* 🌦️ Weather-aware recommendations
* 🧠 Advanced ML / Deep Learning models
* 🌍 Geo-spatial analysis
* 💰 Multi-factor optimization (cost + time + emissions)



## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/green-route.git
cd green-route
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### 🔹 Streamlit App

```bash
streamlit run streamlit_app.py
```

---

### 🔹 Flask App

```bash
cd app
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## 📊 Dataset

* File: `routes_dataset.csv`
* Contains:

  * Source city (`from`)
  * Destination city (`to`)
  * Distance (`distance_km`)

---

## 🌱 Emission Factors

| Transport Mode | Emission Factor (kg CO₂/km) |
| -------------- | --------------------------- |
| Bike           | 0.02                        |
| Car            | 0.12                        |
| Bus            | 0.05                        |
| Train          | 0.03                        |
| Flight         | 0.25                        |

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Flask
* Pandas
* NumPy
* Scikit-learn
* HTML, CSS, JavaScript





---

## 👨‍💻 Author

**Lohith.S**


**Anu.A**


