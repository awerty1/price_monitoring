import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# my functions
import config
import config_example
import send_email
import messages
import file_manipulations

# Get url to site and path to chromedriver
# url = config.url
'''
path_to_chromedriver = config.path_to_chromedriver

# Specify the path to the Chromedriver
chromedriver_path = webdriver.chrome.service.Service(executable_path=path_to_chromedriver)
'''
# Variable for counter
counter = 1

'''Function to get the price from the site'''


def get_price_from_site():
    global counter
    file = 'links.txt'
    flag = False

    for link in file_manipulations.read_links(file):
        # processing the link

        # Settings for launching the browser in "headless" mode
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        # Launch the browser with the specified settings
        # driver = webdriver.Chrome(service_log_path='NUL', service=chromedriver_path, options=options)
        driver = webdriver.Chrome(options=options)

        driver.get(link)
        # driver.refresh()
        time.sleep(3)
        page = driver.page_source
        driver.quit()

        # get cost of item(product) N
        soup = BeautifulSoup(page, 'html.parser')
        container = soup.find_all('ins', attrs={
            'class': 'price-block__final-price'})

        # name of item(product)
        item_name = soup.h1.text

        # Check the price change
        # current_price = container[0].text.replace("₽", '').replace(' ', '').replace('\xa0', '')
        current_price = container[0].text.translate(str.maketrans('', '', ' \xa0₽'))
        # print(current_price)

        # Saving a price from a file
        # saved_price = file_manipulations.read_price_from_file()
        saved_price = file_manipulations.read_price_from_prices(item_name)
        # if saved_price != 0 and current_price != saved_price:
        if current_price != saved_price:
            msg = messages.changed_price_msg(counter, saved_price, current_price, item_name)
            file_manipulations.save_price_changes_to_file(counter, msg, item_name)
            file_manipulations.save_changed_price_to_changed_items(item_name, current_price, saved_price)
            # send_email.send_email_to(saved_price, current_price, item_name)
            file_manipulations.save_price_to_prices(current_price, item_name)
            flag = True
        else:
            msg = messages.price_did_not_changed(counter, current_price, item_name)
            file_manipulations.save_price_changes_to_file(counter, msg, item_name)

        counter += 1

    if flag:
        send_email.send_email_to(file_manipulations.read_price_from_changed_items())

        # Save the new price in the file
        # file_manipulations.save_price_to_file(current_price)
