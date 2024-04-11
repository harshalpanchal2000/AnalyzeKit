from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'seaborn',
        'scipy',
    ],
    author='Harshal Panchal',
    author_email='contact@itsmeharshal.com',
    description='AnalyzeKit is a comprehensive Python library designed to streamline and enhance the process of Exploratory Data Analysis (EDA). 
                 Built with efficiency and versatility in mind, AnalyzeKit offers a suite of powerful tools and functionalities 
                 to empower data scientists, analysts, and researchers in gaining deep insights into their datasets.',
    url='https://github.com/harshalpanchal2000/automateanalysis',
)
