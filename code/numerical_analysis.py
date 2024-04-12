import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis
from sklearn.preprocessing import StandardScaler

# Function to visualize distribution
def visualize_data_distribution(df, column):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], bins=20, kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

# Function to visualize pairwise relationships
def visualize_pairwise_relationships(df):
    sns.pairplot(df)
    plt.show()

# Function to visualize feature relationships
def visualize_feature_relationships(df, column_x, column_y):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=column_x, y=column_y, data=df)
    plt.title(f'Relationship between {column_x} and {column_y}')
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.show()

# Function to visualize correlation
def visualize_correlation(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.show()

# Function for numerical analysis
def perform_numerical_analysis(df):
    numerical_columns = df.select_dtypes(include=['int', 'float']).columns
    for column in numerical_columns:
        print(f"Analysis for {column}:")
        visualize_data_distribution(df, column)
        visualize_feature_relationships(df, column, df.columns[-1])  # Assuming last column is the target variable
        visualize_pairwise_relationships(df)
        visualize_correlation(df)
