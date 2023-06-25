from datetime import datetime

from colorama import Fore
import tldextract


# global variable
price_file = "price.txt"
prices = {}
changed_items = []
currency_symbol = "₽"


'''Save changed price to changed_items'''


def save_changed_price_to_changed_items(item_name, current_price, old_price, link):
    changed_items.append(f'{item_name}: '
                         f'{old_price}{currency_symbol} -> '
                         f'{current_price}{currency_symbol} <br>'
                         f'{link}')


'''Read all items from changed_items'''


def read_price_from_changed_items():
    return list(changed_items)


'''Saving price to dictionary'''


def save_curprice_n_itname_to_prices(item_name, price):
    prices[price] = item_name


'''Read price from prices'''


def read_price_from_old_prices(item_name):
    # if there is no price in the dictionary to select, the function will return 0
    return prices.get(item_name, 0)


'''Get all items frm prices'''


def get_all_items_frm_prices():
    return len(prices)


'''Function to save price changes to a file price_change.txt'''


def save_price_changes_to_file(counter, msg, item_name):
    now = datetime.now()
    # date format 2023-05-20 18:19:31
    new_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    price_changes_file = 'price_change.txt'
    with open(price_changes_file, mode='a', encoding='utf-8', newline='') as f:
        f.write(f"{counter}. {new_datetime}: {msg} : {item_name}\n")


'''Function to read links line by line(generator)'''


def read_links(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()


'''Function to get site name from link'''


def get_name_of_site(link):
    if not link.startswith('http'):
        raise ValueError(f"Invalid link format")

    # getting domain frm link
    name_of_site = tldextract.extract(link).domain
    print(f"Opening {Fore.LIGHTWHITE_EX}{name_of_site}{Fore.RESET}, link: {link}")
    return name_of_site
