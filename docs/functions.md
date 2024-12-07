# Scripts and Functions

## Scripts

* `webscraping.py`: Browses the website of the airline company and scrape the results.
* `parser_final.py`: parses the hmtl of the results to extract information.
    * *departure date, city, time*
    * *arrival city, time*
    * *flight length, number of stops*
* `load_sql.py`: Loads the resulting structured table to a SQLite3 database.
* `whatsapp.py`: Sends a message with the cheapest flight and average ticket fare for the selected date.
* `flight_prices.py`: Main script to organize and call the previous in order.
* `CompareFares.py`: Final script to enable choosing origin and destin cities and number of days from the current date to fetch results.

## Functions

This is the main function code in the script `flight_prices.py`.

::: scripts.flight_prices.get_flight_prices