'''This script gets the database, reads it, takes the minimum flight fare 
for a given date and takes the average and median for the date to send via whatsapp to the user. '''


# imports
import polars as pl
import sqlite3
import pywhatkit as pw
import secure

def send_message(flight_date):
    '''Get the minimum and average ticket price for a flight date and send via Whatsapp Web'''
    
    # Connect to the SQLite database
    
    conn = sqlite3.connect("flightsdb.db")

    # SQL query
    sql = f'''
    -- Main query
    SELECT f.dt, depart_city, city_arrival, n_stops, flight_lengths, min(ticket_prices) as MIN_PRICE,
        s.AVG_PRICE 
    FROM flights f
    LEFT JOIN 

    -- Subquery Average
        (SELECT dt, AVG(ticket_prices) as AVG_PRICE
        FROM flights
        GROUP BY dt) s

    ON f.dt = s.dt
    WHERE f.dt = "{flight_date}"
    '''

    # Query db
    df = pl.read_database(
        query=sql,
        connection=conn
    )  

    # Close the connection
    conn.close()

    # View data
    print(df)

    # Phone to send the message
    phone = secure.phone
    # msg = str(df.to_dict(as_series=False))
    msg = str(df.to_dict(as_series=False))
     
    # Send Python Message via Web WhatsApp
    pw.sendwhatmsg_instantly(phone_no=phone,
                    message=msg,
                    wait_time=8,
                    tab_close= True)

    print("\nMessage sent\n")

    return "Msg Sent"