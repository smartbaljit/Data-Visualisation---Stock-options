################################################
#                  Imports
################################################

# import necessary libraries
from sqlalchemy import func
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import (
    Flask,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy

################################################
#                 Configuration
################################################

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/data.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

################################################
#                    Routes
################################################

# Create a route that renders index.html template
@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/tickers")
def tickers():
    """Return a list of tickers names."""

    # STEP 1 -> Grab all data from a table
    calls_df = pd.read_sql_query("SELECT * FROM allcalls", db.session.bind)

    unique_tickers = list(calls_df['Ticker'].unique()) # be sure to use list() to convert from
    # nd array to python array

    # STEP 2 -> Use Pandas to find the unique ticker values

    # Use Pandas to perform the sql query
    # stmt = db.session.query(calls_data).statement
    # df = pd.read_sql_query(stmt, db.session.bind) 
   
    # Return a list of the column names (sample names)
    return jsonify(unique_tickers)


# Query the database and return the jsonified results
@app.route("/calls")
def calls_data():
    calls_df = pd.read_sql_query("SELECT * FROM allcalls", db.session.bind)

    print(calls_df)

    return jsonify(calls_df.to_dict(orient="records"))


@app.route("/calls/<ticker>")
def calls_data_by_ticker(ticker):
    calls_df = pd.read_sql_query(f"SELECT * FROM allcalls WHERE allcalls.Ticker = '{ticker}'", db.session.bind)

    print(calls_df)

    return jsonify(calls_df.to_dict(orient="records"))

@app.route("/puts")
def put_data():
    puts_df = pd.read_sql_query("SELECT * FROM allputs", db.session.bind)

    print(puts_df)

    return jsonify(puts_df.to_dict(orient="records"))

@app.route("/puts/<ticker>")
def puts_data_by_ticker(ticker):
    puts_df = pd.read_sql_query(f"SELECT * FROM allputs WHERE allputs.Ticker = '{ticker}'", db.session.bind)

    print(puts_df)

    return jsonify(puts_df.to_dict(orient="records"))

    # return

################################################
#                   Run App
################################################

if __name__ == "__main__":
    app.run(debug=True)
