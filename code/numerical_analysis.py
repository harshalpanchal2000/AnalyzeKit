import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis
from sklearn.preprocessing import StandardScaler

# Function to display dataset information
def display_dataset_info(df):
    print("Dataset Info:")
    print(df.info())

# Function to display dataset description
def display_dataset_description(df):
    print("Dataset Description:")
    print(df.describe())

# Function to display basic summary statistics
def display_basic_summary_statistics(df, column):
    print(f"Basic Summary Statistics for {column}:")
    print(f"Mean: {df[column].mean()}")
    print(f"Median: {df[column].median()}")
    print(f"Mode: {df[column].mode().values}")
    print(f"Standard Deviation: {df[column].std()}")
    print(f"Variance: {df[column].var()}")
    print(f"Minimum: {df[column].min()}")
    print(f"Maximum: {df[column].max()}")
    print(f"25th Percentile: {df[column].quantile(0.25)}")
    print(f"75th Percentile: {df[column].quantile(0.75)}")
    print(f"Interquartile Range (IQR): {df[column].quantile(0.75) - df[column].quantile(0.25)}")
    print(f"Skewness: {skew(df[column])}")
    print(f"Kurtosis: {kurtosis(df[column])}")

# Function to analyze missing values
def analyze_missing_values(df, column):
    missing_values_count = df[column].isnull().sum()
    missing_percentage = (missing_values_count / len(df)) * 100
    print(f"Missing Values in {column}: {missing_values_count} ({missing_percentage:.2f}%)")

# Function to detect and display duplicate values
def detect_duplicate_values(df, sample_size=5):
    total_rows = len(df)
    duplicate_rows = df[df.duplicated()]
    duplicate_count = len(duplicate_rows)
    if duplicate_count > 0:
        duplicate_percentage = (duplicate_count / total_rows) * 100
        print(f"Duplicate Rows: {duplicate_count} ({duplicate_percentage:.2f}%)")
        print(duplicate_rows.head(sample_size))
    else:
        print("No duplicate rows found.")

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

# Function to detect outliers
def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers

# Function for numerical analysis
def perform_numerical_analysis(df):
    numerical_columns = df.select_dtypes(include=['int', 'float']).columns
    for column in numerical_columns:
        print(f"Analysis for {column}:")
        visualize_data_distribution(df, column)
        visualize_feature_relationships(df, column, df.columns[-1])  # Assuming last column is the target variable
        display_basic_summary_statistics(df, column)
        analyze_missing_values(df, column)
        detect_outliers(df, column)
    visualize_pairwise_relationships(df)
    visualize_correlation(df)
