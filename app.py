# Import the dependencies.
from flask import Flask

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
   """""List all available api routes."""""
   return (
      f"/api/v1.0/precipitation"
      f"/api/v1.0/stations"
      f"/api/v1.0/tobs"
      f"/api/v1.0/<start>"
      f"/api/v1.0/<start>/<end>"
   )

@app.route("/api/v1.0/precipitation")
def precipitation():
   session = Session(engine)
   """""Precipitation last 13 months."""""
   last_date = session.query(measurement.date, measurement.prcp).\
   filter(measurement.date >= one_year_ago).all()
   """""Convert the query result to a dictionary using date as the key and prcp as the value"""""
prcp_dict = []
for row in prcp_query:
        prcp_dict[row.date] = row.prcp
"""""Return JSON"""""
return jsonify(prcp_dict)

   


