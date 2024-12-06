'''Application: 
This app is intended to retrieve fligh tickets prices from the following flight companies.
+ Azul Airlines
'''

# Import functions
from webscraping import get_flights, get_date
from parser_final import *
from load_sql import load_to_sql
from whatsapp import send_message

# Imports 
import datetime
import time
import sqlite3
import re
import pywhatkit as pw
import polars as pl
from polars import col, concat_str
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

    
def get_flight_prices(d):
    
    # Date to search
    search_date = get_date(add_days=d)
    print(f'\n >> Searching flights on {search_date} <<') 

    # Get Flights page
    get_flights(depart='ZFF',
                arrivl='VCP',
                date_depart= search_date,
                days_range= 5)
    
    # Open HTML file
    soup = open_file('.data/flights.html')

    # Find departures
    departures = soup.find_all("div", class_="flight-card__info left-container css-vjjku5")

    # Creating lists to store the values from the text
    dt = [] #flight date
    depart_city = [] #city departure
    depart_time = [] #departure times
    city_arrival = [] #city arrival
    time_arrival = [] #arrival times
    flight_numbers = [] #flight numbers
    n_stops = [] # qty of stops
    flight_lengths = [] # length in hours
    ticket_prices = [] #ticket prices

    for element in departures:
        # Extract departure data
        departure_city, departure_date, departure_time = departure_information(element=element)
        # Append to list
        depart_city.append(departure_city)
        dt.append(departure_date)
        depart_time.append(departure_time)
                        
        # Extract arrival data
        arrival_city, arrival_time = arrival_information(element=element)
        # Append to list
        city_arrival.append(arrival_city)
        time_arrival.append(arrival_time)
        
        # Extract flight data
        flight_number, stops, hours_length = flight_information(element=element)
        # Append to list
        flight_numbers.append(flight_number)
        n_stops.append(stops)
        flight_lengths.append(hours_length)

        # Extract ticket Prices data
        ticket_prices = prices_information(soup)
        # IF ticket prices are not matching the other add 0.
        while len(ticket_prices) < len(dt): ticket_prices.append('0')

    # First match of the search is usually a "same-day flight".
    # Make the date equal to the second entry
    dt[0] = dt[1]
    
    # Build DataFrame
    dtf_flights = pl.DataFrame({
        'dt': dt,
        'depart_city': depart_city,
        'depart_time': depart_time,
        'city_arrival': city_arrival,
        'time_arrival': time_arrival,
        'flight_numbers': flight_numbers,
        'n_stops': n_stops,
        'flight_lengths': flight_lengths,
        'ticket_prices': ticket_prices,
        'days_before_flight': [str(d)] * len(dt)
        })
        
    print(dtf_flights)
    # Save data as a table
    dtf_flights.write_csv('.data/flights.csv')

    # # Load to SQL
    load_to_sql(flight_date= search_date)

    # # Send Whatsapp Message
    send_message(search_date)