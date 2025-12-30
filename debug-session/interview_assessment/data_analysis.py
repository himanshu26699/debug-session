"""
Data Analysis and ML Model Training Script
This script loads student performance data, preprocesses it, and trains a simple model.
"""

#from pandas import pd
import pandas as pd
#import numpy as np
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def load_data(filepath):
    """Load the dataset from CSV file"""
    print("Loading data...")
    data = pd.read_csv(filepath)
    print(f"Data loaded successfully! Shape: {data.shape}")
    return data

def preprocess_data(data):
    """Preprocess the data by handling missing values"""
    print("\nPreprocessing data...")

    if data.isnull().sum().sum() > 0:
        print("Handling missing values...")
        data = data.fillna(data.mean())

    return data

def train_model(X_train, X_test, y_train, y_test):
    """Train a linear regression model"""
    print("\nTraining model...")

    model = LinearRegression()
    
    # corrected the order of the two lines
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    

    # Calculate error
    mse = mean_squared_error(y_test, predictions)
    print(f"Model trained! Mean Squared Error: {mse:.2f}")

    return model

def main():
    """Main function to run the analysis pipeline"""
    print("="*50)
    print("Student Performance Analysis")
    print("="*50)

    # Load data
    data = load_data("student_data.csv")

    # Preprocess
    data = preprocess_data(data)

    X = data[['study_hours', 'attendance', 'previous_score']]
    y = data['final_score'] # correction score was wrong column name 

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = train_model(X_train, X_test, y_train, y_test)

    print("\n" + "="*50)
    print("Analysis completed successfully!")
    print("="*50)

if __name__ == "__main__":
    main()
