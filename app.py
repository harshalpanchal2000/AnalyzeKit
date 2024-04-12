import streamlit as st
import pandas as pd
from code.categorical_analysis import perform_categorical_analysis
from code.numerical_analysis import perform_numerical_analysis
from code.basic_analysis import perform_basic_analysis
import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")

def main():
    # Logo image in the main section
    st.image("logo.png")

    # Description of the app
    st.write(
        "AnalyseKit is a tool designed to help users quickly and easily understand their dataset through automated exploratory data analysis (EDA). "
        "Upload your CSV file and choose from different analysis options to gain insights into your data."
    )

    # Subheading
    st.subheader("Understand Your Data Quickly and Easily")

    # File uploader
    st.sidebar.title("Upload Dataset")
    uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Create tabs for different analyses
        analysis_option = st.sidebar.radio("Choose Analysis", ["Basic Analysis", "Categorical Analysis", "Numerical Analysis"])

        if analysis_option == "Basic Analysis":
            perform_basic_analysis(df)
        elif analysis_option == "Categorical Analysis":
            categorical_columns = df.select_dtypes(include=['object', 'category']).columns
            if len(categorical_columns) == 0:
                st.write("No categorical features found in the dataset.")
            else:
                perform_categorical_analysis(df)
        elif analysis_option == "Numerical Analysis":
            numerical_columns = df.select_dtypes(include=['int', 'float']).columns
            if len(numerical_columns) == 0:
                st.write("No numerical features found in the dataset.")
            else:
                perform_numerical_analysis(df)

    # Link to LinkedIn profile
    st.markdown(
        """
        <div style='position: fixed; bottom: 10px; right: 10px;'>
            <p>Built by <a href="https://www.linkedin.com/in/harshal-panchal/" target="_blank">Harshal Panchal</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
