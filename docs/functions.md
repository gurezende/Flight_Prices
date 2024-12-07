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

# Output Example

The expected outputs are as follows.

* **[.csv]** file with the flight prices will be the output of the `load_sql` script. 
    * The table will be loaded to a relational database.

| dt| depart_city| depart_time| city_arrival| time_arrival| flight_numbers| n_stops| flight_lengths| ticket_prices| days_before_flight |
|---|---|---|---|---|---|---|---|---|---|
| 28/12| FLL| 18:30| VCP| "04:45"| Voo 8705| Direto| 8.25| 12510| 22 |
| 28/12| MCO| 19:00| VCP| "05:35"| Voo 8707| Direto| 8.58| 4463| 22 |
| 28/12| FLL| 22:30| VCP| "08:45"| Voo 9305| Direto| 8.25| 2203| 22 |
| 28/12| FLL| 15:30| VCP| "07:20"| Voo 8723| 1 conex| 13.8| 3845| 22 |
| 28/12| FLL| 20:30| VCP| "09:15"| Voo 8733| 1 conex| 10.75| 2768| 22 |
| 28/12| FLL| 20:30| VCP| "11:40"| Voo 8733| 1 conex| 13.2| 0| 22 |
| 28/12| FLL| 20:30| VCP| "18:00"| Voo 8733| 1 conex| 19.5| 2768| 22 |
| 28/12| FLL| 20:30| VCP| "19:00"| Voo 8733| 1 conex| 20.5| 2768| 22 |
| VCP| 10:15| MCO| "17:00"| Voo 8706| Direto| 8.75| 0| 22 |
| VCP| 11:05| FLL| "17:30"| Voo 8702| Direto| 8.4| 13711| 22 | 

* After processed, the data table that follows is transformed into a dictionary and sent as text message via WhatsApp.
    * The script performing this task is `whatsapp.py`.

| dt | depart_city| city_arrival| n_stops | flight_lengths | MIN_PRICE | AVG_PRICE |
| ---|------------|-------------|---------|----------------|-----------|-----------|
| 28/12/2024|FLL | VCP | Direto | 8.25 | 2203.0 | 4475.0| 

## Functions

This is the main function code in the script `flight_prices.py`.

::: scripts.flight_prices.get_flight_prices