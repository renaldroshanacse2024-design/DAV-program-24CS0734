"""
Experiment 2C: Reading Data from Text Files, Excel, and the Web
AIM: To read and process data from various sources, including text files, Excel spreadsheets, and web-based
     data, using Python's Pandas library.
"""

import pandas as pd
import os
import warnings

# Suppress pandas future warnings about fillna method deprecation
warnings.simplefilter(action='ignore', category=FutureWarning)

def main():
    print("=== EXPERIMENT 2C: READING DATA FROM MULTIPLE SOURCES ===")
    
    # Define file paths relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, 'Google_data (2b.c1).csv')
    excel_path = os.path.join(script_dir, 'data (2c2).xlsx')
    web_url = 'https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv'
    
    # 1. Read data
    print("\n--- Reading Data ---")
    try:
        text_df = pd.read_csv(csv_path)
        print(f"Loaded CSV from {csv_path}. Shape: {text_df.shape}")
    except Exception as e:
        print(f"Error loading CSV: {e}")
        text_df = None
        
    try:
        excel_df = pd.read_excel(excel_path, sheet_name='Sheet1')
        print(f"Loaded Excel from {excel_path}. Shape: {excel_df.shape}")
    except Exception as e:
        print(f"Error loading Excel: {e}")
        excel_df = None
        
    try:
        web_df = pd.read_csv(web_url)
        print(f"Loaded Web CSV from {web_url}. Shape: {web_df.shape}")
    except Exception as e:
        print(f"Error loading Web CSV: {e}")
        web_df = None
        
    # 2. Display Head of each
    print("\n--- Displaying Head of DataFrames ---")
    if text_df is not None:
        print("\nGoogle Data CSV Head:")
        print(text_df.head(2))
    if excel_df is not None:
        print("\nExcel Sheet Head:")
        print(excel_df.head(2))
    if web_df is not None:
        print("\nWeb Data CSV Head:")
        print(web_df.head(2))
        
    # 3. Handle missing values
    print("\n--- Handling Missing Values ---")
    if text_df is not None:
        # Use newer ffill() if available, otherwise fillna(method='ffill')
        if hasattr(text_df, 'ffill'):
            text_df.ffill(inplace=True)
        else:
            text_df.fillna(method='ffill', inplace=True)
        print("Filled missing values in Google data with forward fill.")
        
    if excel_df is not None:
        # Use newer bfill() if available, otherwise fillna(method='bfill')
        if hasattr(excel_df, 'bfill'):
            excel_df.bfill(inplace=True)
        else:
            excel_df.fillna(method='bfill', inplace=True)
        print("Filled missing values in Excel data with backward fill.")
        
    if web_df is not None:
        web_df.dropna(inplace=True)
        print("Dropped rows with missing values in Web data.")
        
    # 4. Save processed data
    print("\n--- Saving Processed Data ---")
    if text_df is not None:
        proc_csv_path = os.path.join(script_dir, 'processed_text.csv')
        text_df.to_csv(proc_csv_path, index=False)
        print(f"Saved processed CSV to: {proc_csv_path}")
        
    if excel_df is not None:
        proc_excel_path = os.path.join(script_dir, 'processed_excel.xlsx')
        excel_df.to_excel(proc_excel_path, index=False)
        print(f"Saved processed Excel to: {proc_excel_path}")

if __name__ == "__main__":
    main()
