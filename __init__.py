import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew

def detailed_eda_for_variable(df, variable):
    # Display basic information about the variable
    print(f"Variable: {variable}")
    print(f"Type: {df[variable].dtype}")
    print(f"Number of Unique Values: {df[variable].nunique()}")
    print(f"Missing Values: {df[variable].isnull().sum()}")
    print(f"Sample Values: {df[variable].sample(min(5, df.shape[0]))}")

    # If the variable is numerical
    if pd.api.types.is_numeric_dtype(df[variable]):
        # Display summary statistics
        print("\nSummary Statistics:")
        print(df[variable].describe())

        # Visualize distribution
        plt.figure(figsize=(8, 6))
        sns.histplot(df[variable], bins=20, kde=True)
        plt.title(f'Distribution of {variable}')
        plt.xlabel(variable)
        plt.ylabel('Frequency')
        plt.show()

        # Compute skewness
        skewness = skew(df[variable].dropna())
        print(f'Skewness: {skewness}')

        # Detect and visualize outliers using boxplot
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=df[variable])
        plt.title(f'Boxplot of {variable}')
        plt.xlabel(variable)
        plt.show()
    
    # If the variable is categorical
    elif pd.api.types.is_categorical_dtype(df[variable]):
        # Display count of unique values
        print("\nValue Counts:")
        print(df[variable].value_counts())

        # Visualize distribution
        plt.figure(figsize=(8, 6))
        sns.countplot(x=variable, data=df)
        plt.title(f'Count of {variable}')
        plt.xlabel(variable)
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.show()

def automate_detailed_eda(data_path):
    # Load data into a pandas DataFrame
    df = pd.read_csv(data_path)
    
    # Display basic information about the DataFrame
    print("DataFrame Info:")
    print(df.info())
    
    # Display summary statistics for numerical columns
    print("\nSummary Statistics:")
    print(df.describe())
    
    # Display number of missing values in each column
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # Detailed analysis for each variable
    for column in df.columns:
        detailed_eda_for_variable(df, column)

    # Identify and remove duplicate rows
    duplicate_rows = df[df.duplicated()]
    if not duplicate_rows.empty:
        print("\nDuplicate Rows:")
        print(duplicate_rows)
        df = df.drop_duplicates()
        print("Duplicate rows removed.")

    # Compute correlation matrix for numerical variables
    correlation_matrix = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()

