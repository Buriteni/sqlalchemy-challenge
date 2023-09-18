# Import the dependencies.
from flask import Flask, jsonify
# import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
import numpy as np

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
from sqlalchemy.orm import Session
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def  welcome():
#    """""List all available api routes."""""
   return (
      f"/api/v1.0/precipitation<br/>"
      f"/api/v1.0/stations<br/>"
      f"/api/v1.0/tobs<br/>"
      f"/api/v1.0/start<br/>"
      f"/api/v1.0/start/end<br/>"
      f"42"
   )

@app.route("/api/v1.0/precipitation")
def precipitation():
   session = Session(engine)
#    """""Precipitation last 13 months."""""
   latest_date = dt.date(2017, 8, 23)
   one_year_ago = latest_date - dt.timedelta(days=365)
   prcp_query = session.query(measurement.date, measurement.prcp).\
   filter(measurement.date >= one_year_ago).all()
   session.close()
#    """""Convert the query result to a dictionary using date as the key and prcp as the value"""""
   prcp_dict = {}
   for row in prcp_query:
       prcp_dict[row.date] = row.prcp
    # """""Return JSON"""""
   return jsonify(prcp_dict)


@app.route("/api/v1.0/stations")
def stations():
   session = Session(engine)

#    """""Return Stations"""""
   Station = Base.classes.station
   results = session.query(Station.station).all()
   session.close()

#    """""Convert the query result to a dictionary using date as the key and prcp as the value"""""
   stations = list(np.ravel(results))

    # """""Return JSON"""""
   return jsonify(stations = stations)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/api/v1.0/tob")
def stations():
   session = Session(engine)

#    """""Query the dates and temperature observations of the most-active station for the previous year of data."""""
   Station = Base.classes.station
   last_date = session.query(measurement.date).order_by(measurement.date.desc()).first()[0]
last_year = dt.datetime.strptime(last_date, "%Y-%m-%d") - dt.timedelta(days=365)
temp_query = session.query(measurement.date, measurement.tobs).\
    filter(measurement.station == most_active_station).\
    filter(measurement.date >= last_year)

#    """""Convert the query result to a dictionary using date as the key and prcp as the value"""""
temp_df = pd.read_sql(temp_query.statement, temp_query.session.bind)
temp_df.set_index("date", inplace=True)

    # """""Return JSON"""""
return jsonify(stations = stations)

if __name__ == "__main__":
    app.run(debug=True)




   


