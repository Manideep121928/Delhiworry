# 🚚 Delivery ETA Intelligence Dashboard
Delivery ETA Intelligence Dashboard – Machine Learning and Network Analytics for Logistics Optimization.
## Project Overview

Delivery ETA Intelligence Dashboard is a Machine Learning and Network Analytics project designed to predict shipment delivery times, identify logistics bottlenecks, and analyze transportation network performance.

The project combines predictive modeling, business intelligence, graph analytics, and interactive dashboarding to provide actionable insights into logistics operations.


## Problem Statement

Logistics companies often struggle with inaccurate delivery time estimation and limited visibility into network bottlenecks. Delayed shipments can lead to customer dissatisfaction, increased operational costs, and inefficient resource allocation.

This project aims to:

* Predict delivery ETA using Machine Learning
* Identify critical hubs in the logistics network
* Detect bottleneck corridors causing delays
* Provide data-driven insights through an interactive dashboard


## Dataset

The dataset contains shipment movement information including:

* Source Hub
* Destination Hub
* Route Type
* Travel Distance
* Travel Time
* Segment Information
* OSRM Estimated Time
* Shipment Status Information

### Logistics Network Statistics

| Metric                  | Value |
| ----------------------- | ----- |
| Total Hubs (Nodes)      | 1657  |
| Total Corridors (Edges) | 2783  |


## Feature Engineering

Several domain-specific features were created to improve ETA prediction performance.

## Key Features

* Historical Delay Ratio
* Corridor Delay Statistics
* Hub Shipment Volume
* Average Trip Speed
* Segment Distance
* Segment OSRM Time
* Route Characteristics

Feature engineering significantly improved predictive capability.

## Machine Learning Models

Multiple regression models were evaluated for ETA prediction.

## Models Tested

1. Linear Regression
2. Random Forest Regressor
3. XGBoost Regressor

## Final Selected Model

**XGBoost Regressor**

## Performance Metrics

| Metric   | Value  |
| -------- | ------ |
| MAE      | 10.60  |
| RMSE     | 24.13  |
| R² Score | 0.7184 |

The final trained model is stored in:

```text
models/final_eta_model.pkl
```


## Network Analytics

The logistics network was modeled as a graph using NetworkX.

### Analytics Performed

* Degree Centrality Analysis
* Betweenness Centrality Analysis
* Bottleneck Corridor Detection
* Delay Hotspot Identification
* Network Summary Generation

These analyses help identify critical hubs and network vulnerabilities.


## Dashboard

An interactive Streamlit dashboard was developed to visualize project insights and model performance.

### Dashboard Sections

### 📈 Overview

* Total Hubs
* Total Corridors
* Best Model
* R² Score

### 🏢 Hub Analytics

* Top Source Hubs
* Top Destination Hubs

### ⚠️ Bottleneck Analytics

* Top Bottleneck Corridors
* Average Delay Analysis

### 🌐 Network Analytics

* Degree Centrality
* Betweenness Centrality

### 📊 Network Summary

* Network Statistics
* Node and Edge Summary

### 🤖 Model Performance

* Model Comparison
* XGBoost Performance Metrics

## Results

## Best ETA Prediction Model

**XGBoost Regressor**

| Metric   | Value  |
| -------- | ------ |
| MAE      | 10.60  |
| RMSE     | 24.13  |
| R² Score | 0.7184 |

## Key Network Insights

* Analyzed 1,657 logistics hubs
* Evaluated 2,783 transportation corridors
* Identified critical hubs using graph centrality measures
* Detected bottleneck corridors and delay hotspots
* Generated network intelligence reports for operational decision-making

## Project Structure

```text
delivery-eta-intelligence/
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── final_eta_model.pkl
│   └── label_encoders.pkl
│
├── notebooks/
│   ├── 01_eda_and_quality_checks.ipynb
│   ├── 02_eda_feature_engineering.ipynb
│   ├── 03_model_building.ipynb
│   ├── 04_model_selection_and_finetuning.ipynb
│   ├── 05_network_analytics_and_dashboard_prep.ipynb
│   └── 06_network_graph_analytics.ipynb
│
├── reports/
│
├── README.md
└── requirements.txt
```
## How to Run

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Launch Dashboard

```bash
streamlit run dashboard/app.py
```

The dashboard will be available at:
http://localhost:8501



## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* NetworkX
* Streamlit
* Matplotlib
* Plotly
* Joblib


## Future Improvements

* Real-time ETA prediction
* Route optimization recommendations
* Automated bottleneck alerts
* Interactive network graph visualization
* Cloud deployment

## Team

This project was developed collaboratively by:

- Manideep
- Sravya
- Khushi

as part of a logistics analytics and machine learning project focused on ETA prediction and network bottleneck detection.
