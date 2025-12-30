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

## My corrections:
-I changed my Python interpreter to 3.12.6 that was compatible with the packages mentioned in requirements.txt
-requirements.txt
Old packages 
#pandas==2.1.0
#numpy==1.24.3

# Packages that worked with my system
    numpy>=1.26.4
    pandas>=2.2.0
    scikit-learn>=1.4.0

## code corrections
    #from pandas import pd : wrong import statement
    import pandas as pd # corrected
    #from numpy import np : wrong import statement
    import numpy as np # corrected

    sklearn package was missing so addded it in requirements.txt
    from sklearn.model_selection import train_test_split   # This import statement was also missing so added it
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error

# corrected the order of the two lines
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

# correction: score was wrong column name 
    y = data['final_score']  

