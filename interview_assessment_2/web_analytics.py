"""
Web Analytics and Conversion Prediction Script
This script analyzes website traffic data and predicts conversion likelihood.
"""

import pandas as pd
import numpy as np
from sklearn import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def load_traffic_data(filepath):
    """Load website traffic data from CSV file"""
    print("Loading traffic data...")
    data = pd.read_csv(filepath)
    print(f"Data loaded successfully! Shape: {data.shape}")
    return data

def calculate_metrics(data):
    """Calculate additional metrics from raw data"""
    print("\nCalculating engagement metrics...")

    # Calculate bounce rate (percentage)
    data['bounce_rate'] = (data['bounced_sessions'] / data['total_sessions'] * 100

    # Calculate conversion rate
    data['conversion_rate'] = (data['conversions'] / data['total_sessions']) * 100

    return data

def prepare_features(data):
    """Prepare features for machine learning"""
    print("\nPreparing features...")

    # Select features for the model
    features = ['page_views', 'time_on_site', 'bounce_rate', 'traffic_source_encoded']
    X = data[features]

    # Target variable - whether user converted
    y = data['converted']

    return X, y

def build_model(X_train, X_test, y_train, y_test):
    """Build and evaluate a decision tree classifier"""
    print("\nBuilding classification model...")

    # Create model
    model = DecisionTreeClassifier(random_state=42, max_depth=5)

    # Train model
    model.fit(X_train, y_train)

    # Make predictions on training data (intentional bug)
    predictions = model.predict(X_train)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model trained! Accuracy: {accuracy:.2%}")

    return model

def visualize_results(model, feature_names):
    """Visualize feature importance"""
    print("\nGenerating feature importance chart...")

    importances = model.feature_importances_

    # Create bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(feature_names, importances)
    plt.title('Feature Importance for Conversion Prediction')
    plt.xlabel('Features')
    plt.ylabel('Importance')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('feature_importance.png')

    print("Chart saved as 'feature_importance.png'")

def main():
    """Main function to orchestrate the analysis"""
    print("="*60)
    print("Website Traffic Analysis & Conversion Prediction")
    print("="*60)

    # Load data
    data = load_traffic_data("website_traffic.csv")

    # Calculate derived metrics
    data = calculate_metrics(data)

    # Prepare features
    X, y = prepare_features(data)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    # Build and evaluate model
    model = build_model(X_train, X_test, y_train, y_test)

    # Visualize results
    visualize_results(model, X.columns.tolist())

    print("\n" + "="*60)
    print("Analysis completed successfully!")
    print("="*60)

if __name__ == "__main__":
    main()
