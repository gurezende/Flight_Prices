'''Application: 
This app is intended to retrieve fligh tickets prices from the following flight companies.
+ American Airlines
+ Delta Airlines
+ Azul Airlines
'''

# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Opening Driver to use the pointer in browser
driver = webdriver.Chrome()
driver.get("https://www.voeazul.com.br/br/pt/home")
#driver.get("file:///C:/Users/gurez/OneDrive/%C3%81rea%20de%20Trabalho/azul.html")

time.sleep(2)
cookie_ok_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
cookie_ok_button.click()

# Complete Origin Search Box
origin = driver.find_element(By.CSS_SELECTOR, '#Origem1')
origin.send_keys("ZFF")#("Flórida - Todos os Aeroportos")
time.sleep(2)
origin.send_keys(Keys.RETURN)

# Complete Destination Search Box
destin = driver.find_element(By.CSS_SELECTOR, "#Destino1")
destin.send_keys("VCP")#("São Paulo - Campinas")
time.sleep(1)
destin.send_keys(Keys.RETURN)

# # Click on the Dates Search Button
driver.find_element(By.CSS_SELECTOR, "#datepicker_temp1").send_keys(Keys.RETURN)

time.sleep(1)

# Complete DATES
start_date = driver.find_element(By.CSS_SELECTOR, "#startDate")
start_date.send_keys("30/10/2024") #dd/mm/yyyy

end_date = driver.find_element(By.ID, "endDate")
end_date.send_keys("12/11/2024") #dd/mm/yyyy

# Click Button "Fechar"
driver.find_element(By.CSS_SELECTOR, 'button[tabindex="0"]').click()

# Click Button "Confirmar"
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '[data-testid="search-box-hotel-date-picker-primary-button"]').click()

time.sleep(25)

# Get page HTML
html_doc = driver.page_source
soup = BeautifulSoup(html_doc, 'html.parser')

# Get text only
page = soup.get_text()
print(page)

# Close Chrome driver
driver.quit()

# Save file

file = open('/data/flights.html', 'w')
file.write(soup)
file.close()


