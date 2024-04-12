import pandas as pd
from categorical_analysis import perform_categorical_analysis
from numerical_analysis import perform_numerical_analysis
from basic_analysis import perform_basic_analysis

def automate_eda(data_path):
    # Load data into a pandas DataFrame
    df = pd.read_csv(data_path)
    
    # Perform basic analysis
    perform_basic_analysis(df)
    
    # Perform categorical analysis
    perform_categorical_analysis(df)
    
    # Perform numerical analysis
    perform_numerical_analysis(df)

if __name__ == "__main__":
    # Provide the path to your dataset
    data_path = "your_dataset.csv"
    
    # Call the main function to automate EDA
    automate_eda(data_path)

