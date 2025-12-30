# Student Performance Analysis - Debugging Exercise

## Overview
This is a coding assessment to test your debugging skills. The repository contains a Python script that analyzes student performance data and trains a machine learning model. However, **the code has several bugs** that prevent it from running correctly.

## Your Task
1. **Clone/Download** this repository
2. **Set up** the Python environment
3. **Run** the script and identify errors
4. **Fix** the bugs one by one until the code runs successfully
5. **Document** what bugs you found (optional but recommended)

## Expected Time
This exercise should take approximately **15-30 minutes** to complete.

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
python data_analysis.py
```

## What the Code Should Do
When working correctly, the script should:
- Load student performance data from `student_data.csv`
- Preprocess the data (handle missing values)
- Split data into training and test sets
- Train a Linear Regression model
- Display the model's Mean Squared Error

## Files in This Repository
- `data_analysis.py` - Main Python script (contains bugs)
- `student_data.csv` - Sample student performance dataset
- `requirements.txt` - Python package dependencies
- `README.md` - This file

## Tips for Debugging
1. Read error messages carefully - they usually point to the problem
2. Check import statements
3. Verify syntax (colons, indentation)
4. Ensure packages are installed
5. Check the logic flow of the code

## Success Criteria
The script runs without errors and displays output similar to:
```
==================================================
Student Performance Analysis
==================================================
Loading data...
Data loaded successfully! Shape: (20, 4)

Preprocessing data...

Training model...
Model trained! Mean Squared Error: X.XX

==================================================
Analysis completed successfully!
==================================================
```

Good luck! 🚀
