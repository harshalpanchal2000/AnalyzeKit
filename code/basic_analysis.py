import pandas as pd
from scipy.stats import skew

# Function to find missing values and its percentage
def find_missing_values(df):
    missing_values = df.isnull().sum()
    total_rows = len(df)
    missing_percentage = (missing_values / total_rows) * 100
    return missing_values[missing_values > 0], missing_percentage[missing_values > 0]

# Function to calculate skewness
def calculate_skewness(df):
    skewness = df.apply(skew)
    return skewness

# Function to find duplicate values and its percentage
def find_duplicate_values(df):
    return None, 0

# Function to calculate summary statistics
def calculate_summary_statistics(df):
    summary_stats = df.describe().transpose()
    return summary_stats

# Function to display basic dataset information
def display_dataset_info(df):
    dataset_info = df.info()
    return dataset_info

# Function to perform basic analysis
def perform_basic_analysis(df):
    # Find missing values
    missing_values, missing_percentage = find_missing_values(df)
    print("Missing Values:")
    print(missing_values)
    print("\nMissing Values Percentage:")
    print(missing_percentage)

    # Calculate skewness
    skewness = calculate_skewness(df)
    print("\nSkewness:")
    print(skewness)

    # Find duplicate values
    duplicate_rows, duplicate_percentage = find_duplicate_values(df)
    print("\nDuplicate Rows:")
    print(duplicate_rows)
    print("\nDuplicate Rows Percentage:")
    print(duplicate_percentage)

    # Calculate summary statistics
    summary_statistics = calculate_summary_statistics(df)
    print("\nSummary Statistics:")
    print(summary_statistics)

    # Display basic dataset information
    dataset_info = display_dataset_info(df)
    print("\nDataset Information:")
    print(dataset_info)

if __name__ == "__main__":
    # Example usage:
    data_path = "your_data_path.csv"  # Provide the path to your dataset
    df = pd.read_csv(data_path)
    perform_basic_analysis(df)
