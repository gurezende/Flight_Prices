from parser import Parser


parser = Parser()


# Open HTML file
soup = parser.open_file('.data/flights.html')
print(type(soup))