# FWI (Fire Weather Index) Prediction Model

A Flask web application that predicts the Fire Weather Index using Ridge Regression.

## Features

- Web interface for FWI prediction
- Machine learning model using Ridge Regression
- Real-time predictions based on weather parameters

## Parameters

The model takes the following input parameters:
- Temperature
- RH (Relative Humidity)
- Ws (Wind Speed)
- Rain
- FFMC (Fine Fuel Moisture Code)
- DMC (Duff Moisture Code)
- ISI (Initial Spread Index)
- Classes
- Region

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Install required packages:
```bash
pip install flask numpy pandas scikit-learn
```

3. Run the application:
```bash
python application.py
```

4. Open your browser and go to:
```
http://localhost:5000
```

## Usage

1. Navigate to the prediction page
2. Enter the required weather parameters
3. Click "Predict" to get the FWI prediction

## Project Structure

```
├── application.py          # Main Flask application
├── ridge.pkl              # Trained Ridge model
├── scaler.pkl             # StandardScaler for data preprocessing
├── templates/
│   ├── index.html         # Home page
│   └── home.html          # Prediction form
└── README.md              # This file
```

## Technologies Used

- Python
- Flask
- Scikit-learn
- HTML/CSS
- Ridge Regression

## License

This project is open source and available under the [MIT License](LICENSE). 