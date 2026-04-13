
# Green Route Travel Recommendation System

Machine Learning based eco-friendly route recommendation system for Indian cities.

## Features
- 1500+ India travel routes dataset
- ML model training (Linear Regression, Random Forest, Gradient Boosting)
- Model comparison and evaluation (RMSE, MAE, R2)
- Jupyter Notebook for ML pipeline
- Streamlit Web Application
- Route optimization using Dijkstra algorithm

## Project Structure

data/
routes_dataset.csv

models/
emission_model.pkl

notebooks/
GreenRoute_ML.ipynb

app/
streamlit_app.py

## Installation

pip install -r requirements.txt

## Run Notebook

jupyter notebook notebooks/GreenRoute_ML.ipynb

## Run Web App

streamlit run app/streamlit_app.py
