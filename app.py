import streamlit as st
import pandas as pd
from code.categorical_analysis import perform_categorical_analysis
from code.numerical_analysis import perform_numerical_analysis
from code.basic_analysis import perform_basic_analysis
import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")

# Define the path to the background image file
bg_image_path = "images/bg.png"  # Adjust the path as per your file structure

# Define the CSS style to set the background image
page_bg_img = f"""
<style>
[data-testid="stAppContainer"] {{
    background-image: url({bg_image_path});
    background-size: cover;
}}
</style>
"""

# Custom Theme
st.markdown(page_bg_img, unsafe_allow_html=True)



def main():
    # Logo image in the main section
    st.image("images/logo.png")
    
    # Additional image below the logo
    st.image("images/Description.png")

    # File uploader
    st.sidebar.title("Upload Dataset")
    uploaded_file = st.sidebar.file_uploader("", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Create tabs for different analyses
        analysis_option = st.sidebar.radio("Choose Analysis", ["Basic Analysis", "Categorical Analysis", "Numerical Analysis"])

        if analysis_option == "Basic Analysis":
            st.markdown("## Basic Analysis")
            perform_basic_analysis(df)
        elif analysis_option == "Categorical Analysis":
            st.markdown("## Categorical Analysis")
            perform_categorical_analysis(df)
        elif analysis_option == "Numerical Analysis":
            st.markdown("## Numerical Analysis")
            perform_numerical_analysis(df)

    # Link to LinkedIn profile with yellow-colored text
    st.markdown(
        """
        <div style='position: fixed; bottom: 10px; right: 10px;'>
            <p>Built by <a href="https://www.linkedin.com/in/harshal-panchal/" target="_blank" style="color: #fcdc5c;">Harshal Panchal</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
