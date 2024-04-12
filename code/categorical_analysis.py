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

# Function for categorical analysis
def perform_categorical_analysis(df):
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    for column in categorical_columns:
        print(f"Analysis for {column}:")
        visualize_categorical_distribution(df, column)
