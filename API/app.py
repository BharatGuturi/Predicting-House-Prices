import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import inspect
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask_cors import CORS, cross_origin
from flask import Flask, jsonify
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
import os

#Database Setup

load_dotenv()
protocol = 'postgresql'
username = 'postgres'
password = '2090'
host = 'localhost'
port = 5432
database_name = 'housing_db'
rds_connection_string = f'{protocol}://{username}:{password}@{host}:{port}/{database_name}'
engine = create_engine(rds_connection_string)

housing_data = pd.read_sql_query('select * from public."Perth_housing_filtered"', con=engine)
y = housing_data['PRICE']
X = housing_data.drop(['PRICE'], axis = 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2)
scaler = MinMaxScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
data = [[5,3,3,530,264,2000,7800,3000,6060,-31.89944776661762,115.83194169786283,1200,50,12,2022]]
df = pd.DataFrame(data, columns=['BEDROOMS','BATHROOMS','GARAGE','LAND_AREA','FLOOR_AREA','BUILD_YEAR','CBD_DIST','NEAREST_STN_DIST','POSTCODE','LATITUDE','LONGITUDE','NEAREST_SCH_DIST','NEAREST_SCH_RANK','MONTH_SOLD','YEAR_SOLD'])
rf = RandomForestRegressor(random_state = 2).fit(X_train_scaled, y_train)
predictions = rf.predict(df)

# 2. Create an app
app = Flask(__name__)
cors = CORS(app) 

@app.route("/api/v1.0/prediction")
def prediction():
    return jsonify(predictions[0])

# 4. Define main behaviour
if __name__ == "__main__":
    app.run(debug=True)

