"""
Experiment 2D: Exploring Descriptive Analytics Using the Iris Dataset
AIM: To explore descriptive analytics using the Iris dataset with Python's Pandas and Seaborn libraries.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def main():
    print("=== EXPERIMENT 2D: DESCRIPTIVE ANALYTICS ON IRIS DATASET ===")
    
    # Define file paths relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, 'iris_dataset(2d).csv')
    
    # Load dataset
    df = pd.read_csv(data_path)
    
    # Display basic information and summary statistics
    print("\n--- Basic Information ---")
    print(df.info())
    
    print("\n--- Summary Statistics ---")
    print(df.describe())
    
    # Perform univariate analysis - species count
    print("\n--- Species Count ---")
    print(df['species'].value_counts())
    
    # 1. Visualize data distributions using histograms
    print("\nGenerating feature distribution histogram...")
    plt.figure(figsize=(10, 8))
    df.hist(figsize=(10, 8), edgecolor='black')
    plt.suptitle('Feature Distributions', y=0.98, fontsize=16)
    plt.tight_layout()
    hist_path = os.path.join(script_dir, 'feature_distributions.png')
    plt.savefig(hist_path)
    plt.close('all')
    print(f"Saved histogram plot to: {hist_path}")
    
    # 2. Boxplot for Sepal Length
    print("Generating sepal length boxplot...")
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x='species', y='sepal length (cm)', palette='Set2')
    plt.title('Sepal Length Comparison Across Species', fontsize=14)
    boxplot_path = os.path.join(script_dir, 'sepal_length_comparison.png')
    plt.savefig(boxplot_path)
    plt.close()
    print(f"Saved boxplot to: {boxplot_path}")
    
    # 3. Pairplot to analyze feature relationships
    print("Generating pairplot...")
    g = sns.pairplot(df, hue='species', palette='husl')
    g.fig.suptitle('Pairwise Feature Relationships by Species', y=1.02, fontsize=16)
    pairplot_path = os.path.join(script_dir, 'pairplot.png')
    plt.savefig(pairplot_path, bbox_inches='tight')
    plt.close()
    print(f"Saved pairplot to: {pairplot_path}")
    
    print("\nDescriptive analytics visualization completed successfully.")

if __name__ == "__main__":
    main()
