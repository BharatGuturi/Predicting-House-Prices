import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import inspect
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask_cors import CORS, cross_origin
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
import os


# Database Setup
load_dotenv()
protocol = 'postgresql'
username = os.environ.get('db_UserName')
password = os.environ.get('db_Password')
host = 'localhost'
port = 5432
database_name = 'housing_db'
rds_connection_string = f'{protocol}://{username}:{password}@{host}:{port}/{database_name}'
engine = create_engine(rds_connection_string)

#Fetching filtered data and executing regressor
housing_data = pd.read_sql_query(
    'select * from public."Perth_housing_filtered"', con=engine)
y = housing_data['PRICE']
X = housing_data.drop(['PRICE'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2)
scaler = MinMaxScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)


# Create an app
app = Flask(__name__)
cors = CORS(app)

#route to fetch the data from UI and return the predicted output
@app.route('/api/v1.0/housePred', methods=["POST"])
def housePred():
    rf = RandomForestRegressor(random_state=2).fit(X_train_scaled, y_train)
    data_form = [[request.json['br'], request.json['bath'], request.json['gar'], request.json['la'], request.json['fa'], 
                request.json['by'], request.json['cb'], request.json['sdist'], request.json['pc'],
                request.json['latitude'],request.json['longitude'], request.json['sdist'], request.json['sRank'], 
                6, request.json['by']]]
    houseData = pd.DataFrame(data_form, columns=['BEDROOMS', 'BATHROOMS', 'GARAGE', 'LAND_AREA', 'FLOOR_AREA', 'BUILD_YEAR', 'CBD_DIST',
                                     'NEAREST_STN_DIST', 'POSTCODE', 'LATITUDE', 'LONGITUDE', 'NEAREST_SCH_DIST', 'NEAREST_SCH_RANK', 
                                     'MONTH_SOLD', 'YEAR_SOLD'])
    predicted_house = rf.predict(data_form)
    return jsonify(predicted_house[0])


# Define main behaviour
if __name__ == "__main__":
    app.run()
