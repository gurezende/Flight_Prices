'''This script is to load the flights data to a SQLite Database.'''

# Imports
import sqlite3
import polars as pl
from polars import col, concat_str
import numpy as np
import datetime

def load_to_sql(file_path = '.data/flights.csv'):
 
    # Connect to the database
    conn = sqlite3.connect('flightsdb.db')
    cursor = conn.cursor()

    # Data
    df = pl.read_csv(file_path)

    # Format date
    yr = datetime.datetime.now().year
    df = (df
      .filter( col('dt') != "-")
      .with_columns(concat_str(col('dt'), pl.lit('/'), pl.lit(yr)).alias('dt') ) 
      )
          
    # Filter Data
    data = (df
            .filter( (col('depart_city') != "VCP") &
                     (col('ticket_prices') > 0) )
            .to_numpy()
            )
    
    # Create the table if it doesn't exist
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS flights (dt DATE,
                depart_city TEXT,
                depart_time TIME,
                city_arrival TEXT,
                time_arrival TIME,
                flight_number TEXT,
                n_stops TEXT,
                flight_lengths FLOAT,
                ticket_prices FLOAT)
                ''')



    # Insert data into the table
    cursor.executemany('''
                    INSERT INTO flights (dt, depart_city, depart_time, city_arrival, time_arrival, flight_number, n_stops, flight_lengths, ticket_prices) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', 
                    data)

    # # Commit changes and close connection
    conn.commit()
    conn.close()

    print(f"\n >> {df.shape[0]} Rows Loaded succesfully <<")

    return "Loaded"
