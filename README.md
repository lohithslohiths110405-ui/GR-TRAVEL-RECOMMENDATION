
🌱 Green Route – Carbon Efficient Travel Recommender

A smart travel recommendation system that suggests the most eco-friendly transportation mode between two cities based on carbon emissions.

This project helps users make sustainable travel decisions by comparing emissions across different transport options like bike, car, bus, train, and flight.

🚀 Features
🌍 Select source and destination cities
📏 Calculates distance between locations
🚗 Compares multiple transportation modes:
Bike
Car
Bus
Train
Flight
🌱 Recommends the lowest carbon emission option
📊 Visualizes emissions using charts (Streamlit UI)
🌐 Includes both:
Streamlit App (interactive UI)
Flask Web App (HTML-based UI)

🧠 How It Works
The system reads route data from a dataset (routes_dataset.csv)
It calculates emissions using predefined emission factors
Formula used:
Emission = Distance × Emission Factor
The transport mode with the lowest emission is recommended
📂 Project Structure
GR-TRAVEL-RECOMMENDATION/
│
├── app/
│   ├── app.py                 # Flask backend
│   ├── templates/
│   │   └── index.html        # Frontend UI
│   └── static/
│       ├── style.css
│       └── script.js
│
├── data/
│   └── routes_dataset.csv    # Travel routes dataset
│
├── models/
│   └── emission_model.pkl    # Trained ML model (optional use)
│
├── notebooks/
│   ├── EDA_and_Model_Training.ipynb
│   └── ML_Pipeline.ipynb
│
├── streamlit_app.py          # Streamlit UI
├── requirements.txt
└── README.md
⚙️ Installation
1. Clone the Repository
git clone https://github.com/your-username/green-route.git
cd green-route
2. Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux
3. Install Dependencies
pip install -r requirements.txt
▶️ Running the Project
🔹 Run Streamlit App
streamlit run streamlit_app.py
Opens in browser
Interactive charts and UI
🔹 Run Flask App
cd app
python app.py
Open browser:
http://127.0.0.1:5000/

or ## Run Flask App
cd app
python app.py

## Run Streamlit
streamlit run streamlit_app.py
📊 Dataset
File: routes_dataset.csv
Contains:
Source city (from)
Destination city (to)
Distance (distance_km)
🌱 Emission Factors Used
Transport Mode	Emission Factor (kg CO₂/km)
Bike	0.02
Car	0.12
Bus	0.05
Train	0.03
Flight	0.25
🛠️ Technologies Used
Python 🐍
Streamlit 📊
Flask 🌐
Pandas 📈
NumPy
Scikit-learn (for ML model)
HTML, CSS, JavaScript
📸 Screenshots (Optional)

Add screenshots here if needed

🔮 Future Enhancements
🌍 Real-time route integration (Google Maps API)
📱 Mobile-friendly UI
🤖 Advanced ML-based recommendations
🌦️ Weather-based travel suggestions
💰 Cost comparison along with emissions
🤝 Contributing

Contributions are welcome!

Fork the repository
Create a new branch
Make your changes
Submit a pull request
📜 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Lohith S
Anu A
