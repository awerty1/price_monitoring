from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# my functions
import config
import config_example
import send_email
import messages
import file_manipulations

# Get url to site and path to chromedriver
url = config.url
path_to_chromedriver = config.path_to_chromedriver

# Specify the path to the Chromedriver
chromedriver_path = webdriver.chrome.service.Service(executable_path=path_to_chromedriver)

# Variable for counter
counter = 1

'''Function to get the price from the site'''


def get_price_from_site():
    global counter

    # Saving a price from a file
    saved_price = file_manipulations.read_price_from_file()

    # Settings for launching the browser in "headless" mode
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    # Launch the browser with the specified settings
    driver = webdriver.Chrome(service_log_path='NUL', service=chromedriver_path, options=options)

    driver.get(url)
    # driver.refresh()
    time.sleep(3)
    page = driver.page_source
    driver.quit()

    soup = BeautifulSoup(page, 'html.parser')
    container = soup.find_all('ins', attrs={
        'class': 'price-block__final-price'})

    # Check the price change
    #current_price = container[0].text.replace("₽", '').replace(' ', '').replace('\xa0', '')
    current_price = container[0].text.translate(str.maketrans('', '', ' \xa0₽'))
    if current_price != saved_price:
        msg = messages.changed_price_msg(counter, saved_price, current_price)
        file_manipulations.save_price_changes_to_file(counter, msg)
        send_email.send_email_to(saved_price, current_price)
    else:
        msg = messages.price_did_not_changed(counter, current_price)
        file_manipulations.save_price_changes_to_file(counter, msg)

    counter += 1

    # Save the new price in the file
    file_manipulations.save_price_to_file(current_price)
