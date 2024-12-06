'''This script loops 4 times the FlightPrices script to add the search results of fares 7, 30, 60, 90 days prior to the trip'''

from flight_prices import get_flight_prices

if __name__ == "__main__":
    # For how many days ahead is this flight search?
    for d in [10, 30, 60, 90]:
        get_flight_prices(d)


