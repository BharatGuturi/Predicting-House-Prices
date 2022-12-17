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
1.  Create .env files with the content:
    db_UserName= <username>
    db_Password= <userpassword>
    <username> and <userpassword> are the user's usernames and passwords for postgressql
2.  Execute the 'Perth_housing' and 'Perth_housing_filtered' files from the 'Tables' folders to create tables  
3.  Execute the 'ETL.ipynb' file
4.  Execute the 'ML_Prediction.ipynb' file
5.  Execute the 'app.py' file from 'PredictionsAPI' folder
6.  Execute the 'HousingPrices.html' from 'PredictionWeb' folder

## Deployment in Heroku
    Use the following link to access the web application in Heroku
    https://perth-house-prices.herokuapp.com/
    Note: Please note that steps 1 to 5 in the above section (Execution of the code) should be executed before executing the heroku web app.

## Team Members
Bharat Guturi

## Dataset Tables - Raw & Modified

#### all_perth_prices.csv - Raw


## Applications used:

Python - Libraries: Pandas, SQLAlchemy

Jupyter Notebook

Database - PGAdmin (PostgresSQL)

Javascript - Libraries: d3, plotly

UI - Bootstrap, html, css

Installation of Flask Cors is required - Use pip install -U flask-cors 

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


### Data Analysis and Visualisations :

### Box Plot before filtering the data


### Box Plot after filtering the data


### Box Plot after filtering the data


### Correlation Matrix


### Visualisation of existing data after filtering


### Accuracies of various models


### Web application


### Web application output


### Responsive Visualisations and outputs


