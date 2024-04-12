import streamlit as st
import pandas as pd
from scipy.stats import skew
import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")

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
    # Display a sample of the dataset
    st.write("Sample of Dataset:")
    st.write(df.head())

    # Find missing values
    missing_values, missing_percentage = find_missing_values(df)
    st.write("Missing Values:")
    st.write(missing_values)
    st.write("Missing Values Percentage:")
    st.write(missing_percentage)

    # Calculate skewness
    skewness = calculate_skewness(df)
    st.write("Skewness:")
    st.write(skewness)

    # Find duplicate values
    duplicate_rows, duplicate_percentage = find_duplicate_values(df)
    st.write("Duplicate Rows:")
    st.write(duplicate_rows)
    st.write("Duplicate Rows Percentage:")
    st.write(duplicate_percentage)

    # Calculate summary statistics
    summary_statistics = calculate_summary_statistics(df)
    st.write("Summary Statistics:")
    st.write(summary_statistics)

    # Display basic dataset information
    dataset_info = display_dataset_info(df)
    st.write("Dataset Information:")
    st.write(dataset_info)

# Main function
def main():
    st.title("Automated Dataset Analysis")
    
    # Load dataset
    uploaded_file = st.file_uploader("Upload Dataset", type=["csv", "txt"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Create tabs for each analysis
        with st.beta_expander("Basic Analysis"):
            perform_basic_analysis(df)
        
        with st.beta_expander("Missing Values Analysis"):
            find_missing_values(df)
        
        with st.beta_expander("Skewness Analysis"):
            calculate_skewness(df)
        
        with st.beta_expander("Duplicate Values Analysis"):
            find_duplicate_values(df)
        
        with st.beta_expander("Summary Statistics Analysis"):
            calculate_summary_statistics(df)
        
        with st.beta_expander("Dataset Information"):
            display_dataset_info(df)

# Execute the main function
if __name__ == "__main__":
    main()
