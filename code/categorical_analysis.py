import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to visualize distribution of categorical data
def visualize_categorical_distribution(df, column):
    plt.figure(figsize=(8, 6))
    sns.countplot(x=column, data=df, order=df[column].value_counts().index)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

# Function to display value counts for categorical variables
def display_value_counts(df, column):
    print(f"Value Counts for {column}:")
    print(df[column].value_counts())

# Function to display summary statistics for categorical variables
def display_categorical_summary_statistics(df, column):
    print(f"Summary Statistics for {column}:")
    print(df[column].describe())

# Function to analyze missing values in categorical variables
def analyze_categorical_missing_values(df, column):
    missing_values_count = df[column].isnull().sum()
    missing_percentage = (missing_values_count / len(df)) * 100
    print(f"Missing Values in {column}: {missing_values_count} ({missing_percentage:.2f}%)")

# Function to detect and display duplicate values in categorical variables
def detect_categorical_duplicate_values(df, column, sample_size=5):
    total_rows = len(df)
    duplicate_rows = df[df.duplicated()]
    duplicate_count = len(duplicate_rows)
    if duplicate_count > 0:
        duplicate_percentage = (duplicate_count / total_rows) * 100
        print(f"Duplicate Rows in {column}: {duplicate_count} ({duplicate_percentage:.2f}%)")
        print(duplicate_rows.head(sample_size))
    else:
        print(f"No duplicate rows found in {column}.")

# Function for categorical analysis
def perform_categorical_analysis(df):
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    for column in categorical_columns:
        print(f"Analysis for {column}:")
        visualize_categorical_distribution(df, column)
        display_value_counts(df, column)
        display_categorical_summary_statistics(df, column)
        analyze_categorical_missing_values(df, column)
        detect_categorical_duplicate_values(df, column)
