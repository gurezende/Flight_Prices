# Flight Prices Project 🛪
*Gathering airline ticket fares in a SQL DB.*

![](img/flight_fares-wd.jpg)


For the full code visit the repository [Flight Prices in GitHub](https://github.com/gurezende/Flight_Prices).

## Problem and Description

This project was created to fulfill the problem of getting flight ticket prices on a weekly basis for a future study about how the prices behave thoughout an year.

So, the scripts will:

1. Navigate to the airline company website and get flight ticket fares for the given date.
2.  Scrape the results
    * This was accomplished with `Selenium`.    
3. Parse departure and arrival city, time and date, flight length, number of stops and ticket price.
    * Done with `BeautifulSoup`.
4. Store the structured data in a SQL DB
    * Stored in `SQLite 3`.
5. Send a message via WhatsApp with the flight with the lowest price and the average price of the flights for that date.
    * Done with `pywhatkit`.

## Python Version

This project was created with **Python 3.12.1**.

## Modules

* uv >= 0.5.1
* bs4 >= 0.0.2
* mkdocs >= 1.6.1
* mkdocstrings-python >= 1.12.2
* numpy >= 2.1.3
* polars >= 1.16.0
* pywhatkit >= 5.4
* requests >= 2.32.3
* selenium >= 4.27.1
