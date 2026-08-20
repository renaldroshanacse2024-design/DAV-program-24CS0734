"""
Experiment 2B: Exploring Pandas DataFrame Operations for Data Manipulation and Analysis
AIM: To explore and perform various DataFrame operations using Pandas, including loading datasets, data
     inspection, handling missing values, transformations, filtering, grouping, sorting, and saving results.
"""

import pandas as pd
import numpy as np
import os

def main():
    print("=== EXPERIMENT 2B: PANDAS DATAFRAME OPERATIONS ===")
    
    # Load dataset into a DataFrame
    # Locate data.csv in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, 'data.csv')
    
    df = pd.read_csv(data_path)
    
    # Display first and last few rows
    print("First 5 rows:\n", df.head())
    print("\nLast 5 rows:\n", df.tail())
    
    # Check data types and general info
    print("\nDataFrame Info:")
    df.info()
    
    # Summary statistics
    print("\nSummary statistics:\n", df.describe())
    
    # Handle missing values
    # Fill only numeric columns with their mean to prevent pandas 3.0+ errors
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    
    # Create a new column based on an existing column
    df['new_column'] = df['existing_column'] * 2
    
    # Create a Series and perform operations
    series = df['existing_column']
    print("\nSeries addition (existing_column + 10):\n", (series + 10).head())
    
    # Filter rows based on conditions
    filtered_df = df[(df['existing_column'] > 50) & (df['another_column'] < 100)]
    print("\nFiltered DataFrame (existing_column > 50 and another_column < 100) - shape:", filtered_df.shape)
    print(filtered_df.head())
    
    # Grouping and aggregation
    grouped = df.groupby('category_column')['numeric_column'].mean()
    print("\nGrouped mean (mean of numeric_column by category_column):\n", grouped)
    
    # Sorting
    df_sorted = df.sort_values(by='numeric_column', ascending=False)
    print("\nSorted DataFrame (by numeric_column descending):\n", df_sorted.head())
    
    # Boolean masking
    masked_df = df[df['numeric_column'] > df['numeric_column'].median()]
    print("\nMasked DataFrame (numeric_column > median) - shape:", masked_df.shape)
    
    # Remove duplicates and drop missing values
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    
    # Create a new DataFrame with selected columns
    subset_df = df[['column1', 'column2']]
    
    # Save the new DataFrame to a CSV file
    output_path = os.path.join(script_dir, 'filtered_data.csv')
    subset_df.to_csv(output_path, index=False)
    print(f"\nSaved filtered subset to: {output_path}")
    
    # Compute summary statistics
    print("\nTotal sum of numeric_column:", df['numeric_column'].sum())
    print("Mean of numeric_column:", df['numeric_column'].mean())
    print("Standard Deviation of numeric_column:", df['numeric_column'].std())

if __name__ == "__main__":
    main()
