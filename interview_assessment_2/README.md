# Web Analytics Debugging Exercise

## Overview
This is a coding assessment to test your debugging skills. The repository contains a Python script that analyzes website traffic data and predicts user conversion using machine learning. However, **the code has several bugs** that prevent it from running correctly.

## Your Task
1. **Set up** the Python environment
2. **Run** the script and identify errors
3. **Fix** the bugs one by one until the code runs successfully
4. **Verify** the output looks correct

## Expected Time
This exercise should take approximately **20-30 minutes** to complete.

## Setup Instructions

### Step 1: Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Script
```bash
python web_analytics.py
```

## What the Code Should Do
When working correctly, the script should:
- Load website traffic data from `website_traffic.csv`
- Calculate engagement metrics (bounce rate, conversion rate)
- Prepare features for machine learning
- Train a Decision Tree classifier to predict conversions
- Evaluate model accuracy on test data
- Generate a feature importance visualization chart

## Files in This Repository
- `web_analytics.py` - Main Python script (contains bugs)
- `website_traffic.csv` - Website traffic dataset with user behavior metrics
- `requirements.txt` - Python package dependencies
- `README.md` - This file

## Dataset Description
The CSV file contains the following columns:
- `page_views` - Number of pages viewed in session
- `time_on_site` - Time spent on site (seconds)
- `bounced_sessions` - Number of sessions that bounced
- `total_sessions` - Total number of sessions
- `conversions` - Number of conversions
- `converted` - Binary target (1 = converted, 0 = did not convert)
- `traffic_source` - Source of traffic (organic, paid, social, direct)

## Tips for Debugging
1. **Read error messages carefully** - they usually indicate the exact problem
2. Check import statements and package installations
3. Verify Python syntax (parentheses, colons, indentation)
4. Ensure column names match the actual CSV data
5. Check the logic flow - does the code make sense?
6. Consider the machine learning workflow - what order should operations happen?

## Success Criteria
The script runs without errors and displays output similar to:
```
============================================================
Website Traffic Analysis & Conversion Prediction
============================================================
Loading traffic data...
Data loaded successfully! Shape: (25, 7)

Calculating engagement metrics...

Preparing features...

Building classification model...
Model trained! Accuracy: XX.XX%

Generating feature importance chart...
Chart saved as 'feature_importance.png'

============================================================
Analysis completed successfully!
============================================================
```

## Notes
- You may need to explore the CSV file to understand the data structure
- Some bugs are syntax errors, others are logic errors
- All packages needed should be installable via pip
- The model accuracy should be reasonable (not 0% or 100%)

Good luck debugging!
