'''This script gets the database, reads it, takes the minimum flight fare 
for a given date and takes the average and median for the date to send via whatsapp to the user. '''


# imports
import polars as pl
import sqlite3
import pywhatkit as pw
import secure

def send_message(flight_date, origin_cd):
    '''Get the minimum and average ticket price for a flight date and send via Whatsapp Web
    INPUTS:
    * flight_date: str = date to search for flights
    * origin_cd = codes of the cities to be considered. e.g. origin_cds = "('MIA', 'FLL', 'MCO')"
    '''
    
    # Connect to the SQLite database
    
    conn = sqlite3.connect("flightsdb.db")

    # SQL query
    sql = f'''
        -- Main query
        SELECT 
            f.dt, 
            f.depart_city, 
            f.city_arrival, 
            f.n_stops, 
            f.flight_lengths, 
            MIN(f.ticket_prices) AS MIN_PRICE, 
            s.AVG_PRICE
        FROM flights f
        LEFT JOIN (
            SELECT dt, AVG(ticket_prices) AS AVG_PRICE
            FROM flights
            WHERE depart_city IN {origin_cd}
            GROUP BY dt
        ) s
        ON f.dt = s.dt
        WHERE f.depart_city IN {origin_cd} 
        AND f.dt = "{flight_date}"
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