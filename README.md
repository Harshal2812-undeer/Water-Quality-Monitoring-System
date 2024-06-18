# Water-Quality-Monitoring-System

# Water Quality Monitoring System

This project is a Flask-based web application that allows users to predict the quality of water samples based on three important parameters: pH, turbidity, and temperature. The application also includes user authentication functionality, allowing users to register and log in to access the water quality prediction feature.

## Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy
- bcrypt
- NumPy
- Pandas
- scikit-learn
- pickle

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-repo/water-quality-monitoring-system.git
   ```

2. Navigate to the project directory:

   ```
   cd water-quality-monitoring-system
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Run the Flask application:

   ```
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000` to access the application.

## Features

- User registration and authentication
- Water quality prediction based on pH, turbidity, and temperature
- Random Forest Classifier model for accurate predictions

## Important Parameters

The following parameters are crucial in determining water quality:

1. **pH**: pH is a measure of the acidity or basicity of a solution. It is an essential parameter for water quality as it affects various chemical and biological processes. A pH value outside the acceptable range can harm aquatic life and cause corrosion or scaling in water distribution systems.

2. **Turbidity**: Turbidity is a measure of the cloudiness or haziness of water caused by suspended particles. High turbidity can be an indicator of pollution or the presence of contaminants. It can also interfere with disinfection processes and provide a suitable environment for microbial growth.

3. **Temperature**: Water temperature plays a vital role in various chemical and biological processes. It affects the solubility of gases, the rate of chemical reactions, and the metabolism of aquatic organisms. Extreme temperatures can stress or kill aquatic life and promote the growth of harmful microorganisms.

By considering these three parameters, the Water Quality Monitoring System can provide an accurate assessment of water purity, allowing users to take appropriate actions to ensure safe and clean water for various purposes.
