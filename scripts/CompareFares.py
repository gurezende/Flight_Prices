'''This script loops 4 times the flight_prices script to add the search
results of ticket fares for 10, 30, 60, 90 days ahead from the current date'''

from flight_prices import get_flight_prices

if __name__ == "__main__":
    # For how many days ahead is this flight search?
    for d in [10, 30, 60, 90]:
        get_flight_prices(d = d,
                          origin_cd= 'ZFF',
                          destin_cd = 'VCP'
                          )





