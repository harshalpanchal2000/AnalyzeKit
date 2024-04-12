import streamlit as st
import pandas as pd
from code.categorical_analysis import perform_categorical_analysis
from code.numerical_analysis import perform_numerical_analysis
from code.basic_analysis import perform_basic_analysis

def main():
    st.title("AnalyseKit: Automated Exploratory Data Analysis")

    # Subheading
    st.subheader("Understand Your Data Quickly and Easily")

    # File uploader
    st.sidebar.title("Upload Dataset")
    uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Display basic info
        st.subheader("Basic Analysis")
        perform_basic_analysis(df)

        # Display categorical analysis
        st.subheader("Categorical Analysis")
        perform_categorical_analysis(df)

        # Display numerical analysis
        st.subheader("Numerical Analysis")
        perform_numerical_analysis(df)

if __name__ == "__main__":
    main()
