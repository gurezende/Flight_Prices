'''This script is to load the flights data to a SQLite Database.'''

# Imports
import sqlite3
import polars as pl
from polars import col, concat_str
import numpy as np

def load_to_sql(flight_date:str, file_path = '.data/flights.csv'):
    '''
    Load table to SQL database
    - Inputs:
    * file path: str = path to the csv table with flight fares
    * flight_date: str = search date for the flight
    '''
 
    # Connect to the database
    conn = sqlite3.connect('flightsdb.db')
    cursor = conn.cursor()

    # Data
    df = pl.read_csv(file_path)

    # Format date
    yr = flight_date[-4:] #get year => last 4 digits of the flight date
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
                ticket_prices FLOAT,
                days_before_flight INT)
                ''')



    # Insert data into the table
    cursor.executemany('''
                    INSERT INTO flights (dt, depart_city, depart_time, city_arrival, time_arrival, flight_number, n_stops, flight_lengths, ticket_prices, days_before_flight) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', 
                    data)

    # # Commit changes and close connection
    conn.commit()
    conn.close()

    print(f"\n >> {df.shape[0]} Rows Loaded succesfully <<")

    return "Loaded"
