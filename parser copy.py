# Imports 
from bs4 import BeautifulSoup
import polars as pl
import re

# Open file
f = open('.data/flights.html', 'r').read()

# Convert html to a BeatufulSoup object
soup = BeautifulSoup(f, 'html.parser')

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

for flight in departures[:4]:
    # print(flight)
    # print('===================================================================')
    # Extract departure information
    departure_info = (flight
                      .find('h4', class_=re.compile(r"^departure css-")))
    # departure_city, departure_date = (departure_info
    #                                   .find('span', class_='iata-day')
    #                                   .text
    #                                   .strip()
    #                                   .split(' • '))
    # departure_time = (departure_info
    #                   .text
    #                   .split()[0])

    print(departure_info)

#     #-----------------------------------------------------------------------

#     # Extract arrival information
#     arrival_info = (element
#                     .find('h4', class_='arrival css-1whjg6b'))
#     arrival_time = (arrival_info
#                     .text
#                     .strip()
#                     .split(' ')[0])
#     arrival_city = (arrival_info
#                     .find('span', class_='iata-day')
#                     .text
#                     .strip()
#                     .split(' • ')[0])

#     # Append to list
#     city_arrival.append(arrival_city)
#     time_arrival.append(arrival_time)

#     #-----------------------------------------------------------------------

#     # Extract stops and flight number
#     leg_info = (element
#                 .find('span', class_='css-tkxfs6')
#                 .text
#                 .strip())
#     flight_number, stops = leg_info[:8], leg_info[8:].strip()

#     # Extract flight length
#     flight_length = (element
#                      .find('button', class_='duration css-12pqtfr')
#                      .find('strong')
#                      .text
#                      .strip()
#                      .split())
#     # Convert to integer
#     hr_length = int(flight_length[0].split('h')[0])
#     min_length = int(flight_length[1].split('m')[0])
#     # Convert to hours
#     hours_length = hr_length + (min_length/60)

#     # Append to list
#     flight_numbers.append(flight_number)
#     n_stops.append(stops)
#     flight_lengths.append(hours_length)

#     #-----------------------------------------------------------------------

#     # Extract price
#     price = (element
#              .find('h4', class_='current css-2db79l')
#              .text
#              .strip()
#              .replace('R$', '')
#              .replace('.', '')
#              .split(',')[0]
#              .strip())

#     # Append to list
#     ticket_prices.append(price)
    
# #-----------------------------------------------------------------------

# # Build DataFrame
# dtf_flights = pl.DataFrame({
#     'dt': dt,
#     'depart_city': depart_city,
#     'depart_time': depart_time,
#     'city_arrival': city_arrival,
#     'time_arrival': time_arrival,
#     'flight_numbers': flight_numbers,
#     'n_stops': n_stops,
#     'flight_lengths': flight_lengths,
#     'ticket_prices': ticket_prices,
#     })

# dtf_flights.write_csv('.data/flights.csv')