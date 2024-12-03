# Imports 
from bs4 import BeautifulSoup
import polars as pl


# Open file
f = open('.data/flights.html', 'r').read()

# Convert html to a BeatufulSoup object
soup = BeautifulSoup(f, 'html.parser')

# Find departures
departures = soup.find_all("div", class_="flight-card__info left-container css-vjjku5")

for element in departures:
    # Extract departure information
    departure_info = soup.find('h4', class_='departure css-bnagdk')
    departure_city, departure_date = departure_info.find('span', class_='iata-day').text.split(' • ')
    
    # Extract arrival information
    arrival_info = soup.find('h4', class_='arrival css-1whjg6b')
    arrival_time = arrival_info.text.strip().split(' ')[0]
    arrival_city = arrival_info.find('span', class_='iata-day').text.strip().split(' • ')[0]

    print(arrival_city, arrival_time, sep="- ")
