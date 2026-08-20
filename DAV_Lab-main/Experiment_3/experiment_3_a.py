"""
Experiment 3A: Univariate Analysis: Statistical Analysis Using Diabetes Datasets
AIM: To analyze the Diabetes dataset from UCI and the Pima Indians Diabetes dataset using univariate
     statistical methods, including Frequency, Mean, Median, Mode, Variance, Standard Deviation,
     Skewness, and Kurtosis.
"""

import pandas as pd
import numpy as np
import os
from scipy.stats import skew, kurtosis

def main():
    print("=== EXPERIMENT 3A: UNIVARIATE STATISTICAL ANALYSIS ===")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    uci_path = os.path.join(script_dir, 'uci_diabetes.csv')
    pima_path = os.path.join(script_dir, 'pima_diabetes.csv')
    
    # Load datasets
    uci_diabetes = pd.read_csv(uci_path)
    pima_diabetes = pd.read_csv(pima_path)
    
    print("\nUCI Diabetes Dataset Sample:")
    print(uci_diabetes.head(2))
    print("\nPima Indians Diabetes Dataset Sample:")
    print(pima_diabetes.head(2))
    
    # Define Relevant Numerical Columns
    numerical_columns = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI",
                         "DiabetesPedigreeFunction", "Age"]
    
    # Univariate Analysis Function
    def univariate_analysis(df, columns):
        stats = {}
        for col in columns:
            stats[col] = {
                "Mean": np.mean(df[col]),
                "Median": np.median(df[col]),
                "Mode": df[col].mode()[0],
                "Variance": np.var(df[col], ddof=1),
                "Standard Deviation": np.std(df[col], ddof=1),
                "Skewness": skew(df[col]),
                "Kurtosis": kurtosis(df[col])
            }
        return pd.DataFrame(stats).T

    # Perform Univariate Analysis
    uci_stats = univariate_analysis(uci_diabetes, numerical_columns)
    pima_stats = univariate_analysis(pima_diabetes, numerical_columns)
    
    # Display Results
    print("\nUCI Diabetes Dataset Statistics:")
    print(uci_stats)
    print("\nPima Indians Diabetes Dataset Statistics:")
    print(pima_stats)

if __name__ == "__main__":
    main()
