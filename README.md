# Predicting House Prices in Perth

## Project Title - Predicting House Prices in Perth

It is everyones dream to buy a home. For someone who is thinking of buying a new house, this model aims to predict the house prices in the suburb of Perth. This data is analysed based on the available historical data of house prices in Perth.

## Sources of Data
https://www.kaggle.com/datasets/syuzai/perth-house-prices

## Architecture Diagram

<p align="center"><img src='https://github.com/BharatGuturi/Predicting-House-Prices/blob/main/Images/Architecture_diagram.png' width = 80% ></p> 


## Contents of the Folders
1.  PredicationWeb: Files related to Webapp
2.  PredictionsAPI: Files related to Flask API
3.  Resources: raw csvs and data cleaning pandas notebook
4.  Tables: scripts to create tables
5.  Images: Images related to readme files
6.  ETL: Extract, Transform and Load files
7.  ML Prediction: Prediction files
8.  Final_Presentation_Project_4: Presendation document
9.  Project_4_Report: Final report

## Execution of the code:
To run this project, following steps to be executed:
1. Clone the repo using following command:
    git clone https://github.com/BharatGuturi/Predicting-House-Prices.git 
2. Open local postgresSQL and create database with name 'housing_db'.
3. Execute the 'Perth_housing' and 'Perth_housing_filtered' files from the 'Tables' folders to create tables in housing_db 
4.  Create .env files with the content in cloned repo and PredictionAPI folder with followig details in it:
    db_UserName= <username>
    db_Password= <userpassword>
    <username> and <userpassword> are the user's usernames and passwords for postgressql connection
3.  Execute the 'ETL.ipynb' file to load the data into database
4.  Execute the 'ML_Prediction.ipynb' file
5.  Import required libraries using following commands in PredictionAPI folder
    pip install SQLAlchemy
    pip install Flask-Cors
    pip install Flask
    pip install python-dotenv
    pip install -U scikit-learn 
5.  Execute the 'app.py' file from 'PredictionAPI' folder
6.  Execute the 'HousingPrices.html' from 'PredictionWeb' folder or below URL for website deployed in Heroku
        Heroku deployed website: https://perth-house-prices.herokuapp.com/

## Deployment in Heroku
    Use the following link to access the web application in Heroku
    https://perth-house-prices.herokuapp.com/
    Note: Please note that steps 1 to 5 in the above section (Execution of the code) should be executed before executing the heroku web app.

## Team Members
Bharat Guturi

## Dataset Tables - Raw & Modified

#### all_perth_prices.csv - Raw
<p align="center"><img src='https://github.com/BharatGuturi/Predicting-House-Prices/blob/main/Images/Input_csv.png' width = 80% ></p> 

## Applications used:

Python - Libraries: Pandas, SQLAlchemy, numpy, sklearn, matplotlib, flask

Jupyter Notebook

Database - PGAdmin (PostgresSQL)

Javascript - Libraries: d3, plotly

UI - Bootstrap, html, css


## Process:

### Extract :

Import dependecies and the libraries

### Transform:

Transform tables to formal specification

##### Data Modelling - Tables :

Create the tables  

### Load:

Connect to postgres SQL database -> load data.

Formal specification to be created that defines the tables format can be imported into postgres SQL database.

### Imported tables:
 <p align="center"><img src='https://github.com/BharatGuturi/Predicting-House-Prices/blob/main/Images/Input_data.png' width = 80% ></p>  

### Data Analysis and Visualisations :

### Box Plot before filtering the data

<p align="center"><img src='https://github.com/BharatGuturi/Predicting-House-Prices/blob/main/Images/Boxplot_before_filtering_the_data.png' width = 80% ></p>

### Box Plot after filtering the data

<p align="center"><img src='https://github.com/BharatGuturi/Predicting-House-Prices/blob/main/Images/Box_plot_after_filtering_the_data.png' width = 80% ></p>

### Correlation Matrix

<p align="center"><img src='https://github.com/BharatGuturi/Predicting-House-Prices/blob/main/Images/correlation_matrix.png' width = 80% ></p>

### Visualisation of existing data after filtering

<p align="center"><img src='https://github.com/BharatGuturi/Predicting-House-Prices/blob/main/Images/existing_data_visualisation.png' width = 80% ></p>

### Accuracies of various models

<p align="center"><img src='https://github.com/BharatGuturi/Predicting-House-Prices/blob/main/Images/accuracies_of_various_models.png' width = 80% ></p>

### Web application

<p align="center"><img src='https://github.com/BharatGuturi/Predicting-House-Prices/blob/main/Images/web_application.png' width = 80% ></p>

### Web application output

<p align="center"><img src='https://github.com/BharatGuturi/Predicting-House-Prices/blob/main/Images/Predicted_and_Actual_price.png' width = 80% ></p>

### Responsive Visualisations and outputs

<p align="center"><img src='https://github.com/BharatGuturi/Predicting-House-Prices/blob/main/Images/Responsive_visualisation_1.png' width = 80% ></p>

<p align="center"><img src='https://github.com/BharatGuturi/Predicting-House-Prices/blob/main/Images/Responsive_visualisation_2.png' width = 80% ></p>

<p align="center"><img src='https://github.com/BharatGuturi/Predicting-House-Prices/blob/main/Images/Responsive_visualisation_3.png' width = 80% ></p>