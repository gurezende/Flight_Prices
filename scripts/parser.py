from bs4 import BeautifulSoup
import numpy as np
import re

class Parser:
    """
    A class to parse HTML files and extract flight information.
    """

    def open_file(self, file_path):
        """
        Opens the HTML file for parsing and converts to a BeautifulSoup object.

        Args:
            file_path (str): The file path to open.

        Returns:
            BeautifulSoup: The BeautifulSoup object.
        """
        html_content = open(file_path, 'r').read()
        # Convert html to a BeatufulSoup object
        return BeautifulSoup(html_content, 'html.parser')

    def departure_information(self, element):
        """
        Extracts departure information from a BeautifulSoup element.

        Args:
            element (BeautifulSoup): The BeautifulSoup element.

        Returns:
            tuple: A tuple containing departure city, date, and time.
        """
        departure_info = element.find('h4', class_=re.compile(r"^departure css-"))
        if not departure_info:
            return None, None, None

        iata_day_span = departure_info.find('span', class_='iata-day')
        if not iata_day_span:
            return None, None, None

        parts = iata_day_span.text.strip().split(' • ')
        departure_city = parts[0]

        if len(parts) > 1:
            departure_date = parts[1]
        else:
            departure_date = None

        departure_time = departure_info.text.split()[0]

        return departure_city, departure_date, departure_time

    def arrival_information(self, element):
        """
        Extracts arrival information from a BeautifulSoup element.

        Args:
            element (BeautifulSoup): The BeautifulSoup element.

        Returns:
            tuple: A tuple containing arrival city and time.
        """
        arrival_info = element.find('h4', class_=re.compile('arrival css-'))
        if not arrival_info:
            return None, None

        iata_day_span = arrival_info.find('span', class_='iata-day')
        if not iata_day_span:
            return None, None

        arrival_city = iata_day_span.text.strip().split(' • ')[0]
        arrival_time = arrival_info.text.strip().replace('\n', '').split(' ')[0]

        return arrival_city, arrival_time

    def flight_information(self, element):
        """
        Extracts flight number, quantity of connections, and duration of the flight from a BeautifulSoup element.

        Args:
            element (BeautifulSoup): The BeautifulSoup element.

        Returns:
            tuple: A tuple containing flight number, stops, and flight duration in hours.
        """
        leg_info_span = element.find('span', class_='css-tkxfs6')
        if not leg_info_span:
            return None, None, None

        leg_info = leg_info_span.text.strip()
        flight_number_match = re.search(r'Voo [0-9]*', leg_info)
        stops_match = re.search(r'[0-9] conex|Direto', leg_info)

        if not flight_number_match or not stops_match:
            return None, None, None

        flight_number = flight_number_match.group()
        stops = stops_match.group()

        duration_button = element.find('button', class_=re.compile('duration css-'))
        if not duration_button:
            return flight_number, stops, None

        duration_strong = duration_button.find('strong')
        if not duration_strong:
            return flight_number, stops, None

        flight_length = duration_strong.text.strip().split()

        if 'd' in flight_length[0]:
            day_length = int(flight_length[0].split('d')[0]) * 24
            if len(flight_length) < 2:
                flight_length.extend(['0h', '0m'])
            elif len(flight_length) < 3:
                flight_length.extend(['0m'])
            hr_length = int(flight_length[1].split('h')[0]) + day_length
            min_length = int(flight_length[2].split('m')[0])
        else:
            hr_length = int(flight_length[0].split('h')[0])
            if len(flight_length) < 2:
                flight_length.append('0m')
            min_length = int(flight_length[1].split('m')[0])

        hours_length = hr_length + (min_length / 60)

        return flight_number, stops, hours_length

    def prices_information(self, soup):
        """
        Extracts ticket prices of the flight from a BeautifulSoup element.

        Args:
            soup (BeautifulSoup): The BeautifulSoup object.

        Returns:
            list: A list of ticket prices.
        """
        parsed_prices = []
        price_elements = soup.find_all('div', class_=re.compile('flight-card__fare right-container'))

        for p in price_elements:
            price_text = p.text.strip().replace('R$', '').replace('.', '').replace('\n', '').replace('A partir de', '').replace('Voo esgotado', '0-').replace(' ', '').replace('0-0-', '0').split(',')[0].strip()
            try:
                price = float(price_text)
                parsed_prices.append(price)
            except ValueError:
                parsed_prices.append(None)

        return parsed_prices