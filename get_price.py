import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from colorama import Fore

import config
import config_example
import send_email
import messages
import file_manipulations
from choose_site import choose_site

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
        # get name of site
        try:
            name_of_site = file_manipulations.get_name_of_site(link)
        except ValueError as error:
            print(f"{Fore.RED}"
                  f"Error processing link '"
                  f"{Fore.RESET}"
                  f"{Fore.BLUE}{link}{Fore.RESET}"
                  f"{Fore.RED}': {error}{Fore.RESET}")
            continue  # go to the next iteration of the loop

        # processing the link
        options = Options()
        # remove the --headless option
        if name_of_site == "yandex":
            options.set_capability('goog:chromeOptions', {'args': []})
        # Settings for launching the browser in "headless" mode
        else:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                                 " (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")
        # Launch the browser with the specified settings
        # driver = webdriver.Chrome(service_log_path='NUL', service=chromedriver_path, options=options)
        driver = webdriver.Chrome(options=options)

        try:
            driver.get(link)
        except WebDriverException as exception:
            print(f"{Fore.RED}"
                  f"Page loading ERROR: {exception}"
                  f"{Fore.RESET}")
        # driver.refresh()
        time.sleep(3)
        page = driver.page_source
        driver.quit()

        # choose site
        item_name, current_price = choose_site(name_of_site, page)

        # if didn't find correct site_name
        if item_name is None and current_price is None:
            continue

        # Saving a price from a dictionary
        saved_price = file_manipulations.read_price_from_old_prices(item_name)
        # if saved_price != 0 and current_price != saved_price:
        if current_price != saved_price:
            msg = messages.changed_price_msg(counter, saved_price, current_price, item_name)
            file_manipulations.save_price_changes_to_file(counter, msg, item_name)
            # Save the new price in the file
            file_manipulations.save_changed_price_to_changed_items(item_name, current_price, saved_price, link)
            file_manipulations.save_curprice_n_itname_to_prices(current_price, item_name)
            flag = True
        else:
            msg = messages.price_did_not_changed(counter, current_price, item_name)
            file_manipulations.save_price_changes_to_file(counter, msg, item_name)

        counter += 1

    if flag:
        send_email.send_email_to(file_manipulations.read_price_from_changed_items())

