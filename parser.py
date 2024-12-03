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

for element in departures:
    # Extract departure information
    departure_info = (element
                      .find('h4', class_=re.compile(r"^departure css-")))
    
    departure_city = (departure_info
                      .find('span', class_='iata-day')
                      .text
                      .strip()
                      .split(' • ')[0])
    departure_date = (departure_info
                      .find('span', class_='iata-day')
                      .text
                      .strip()
                      .split(' • '))
    # If no date is provided, use "-"
    if len(departure_date) == 1: 
        departure_date = "-"
    else:
        departure_date = departure_date[1]
    departure_time = (departure_info
                      .text
                      .split()[0])

    # Append to list
    depart_city.append(departure_city)
    dt.append(departure_date)
    depart_time.append(departure_time)

    #-----------------------------------------------------------------------

    # Extract arrival information
    arrival_info = (element
                    .find('h4', class_=re.compile('arrival css-')))
    arrival_time = (arrival_info
                    .text
                    .strip()
                    .split(' ')[0])
    arrival_city = (arrival_info
                    .find('span', class_='iata-day')
                    .text
                    .strip()
                    .split(' • ')[0])

    # Append to list
    city_arrival.append(arrival_city)
    time_arrival.append(arrival_time)

    #-----------------------------------------------------------------------

    # Extract stops and flight number
    leg_info = (element
                .find('span', class_='css-tkxfs6')
                .text
                .strip())

    flight_number = re.search('Voo [0-9]*', leg_info).group()
    stops = re.search('[0-9] conex|Direto', leg_info).group()

    # Extract flight length
    flight_length = (element
                     .find('button', class_=re.compile('duration css-'))
                     .find('strong')
                     .text
                     .strip()
                     .split())
    
    # Transform days into hours
    if 'd' in flight_length[0]:
        day_length = int(flight_length[0].split('d')[0])*24
        hr_length = int(flight_length[1].split('h')[0]) + day_length
        min_length = int(flight_length[2].split('m')[0])
    else:
        # Convert to integer
        hr_length = int(flight_length[0].split('h')[0])
        min_length = int(flight_length[1].split('m')[0])
    
    # Convert to hours
    hours_length = hr_length + (min_length/60)

    # Append to list
    flight_numbers.append(flight_number)
    n_stops.append(stops)
    flight_lengths.append(hours_length)

    #-----------------------------------------------------------------------

# Find prices
price_elements = soup.find_all('h4', class_='current css-2db79l')

# Iterate and collect ticket prices
for p in price_elements:
    price=(
        p
        .text
        .strip()
        .replace('R$', '')
        .replace('.', '')
        .split(',')[0]
        .strip()
    )
    
    # Append to list
    ticket_prices.append(price)
    
#-----------------------------------------------------------------------

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
    'ticket_prices': ticket_prices[:len(dt)]
    })

# print(dtf_flights)
dtf_flights.write_csv('.data/flights.csv')