from datetime import datetime

from colorama import Fore


# global variable
right_arrow = "=>"
currency_symbol = "₽"

'''Function for getting time'''


def get_datetime():
    now = datetime.now()
    # date format 2023-05-20 18:19:31
    new_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    return new_datetime


'''Message when the script starts'''


def start_msg():
    starting_msg = f" Script to price monitoring started! "
    hash_symbols = '#'*40
    print(f"{Fore.LIGHTWHITE_EX}{hash_symbols}{starting_msg}{hash_symbols}{Fore.RESET}")


'''Function for changed price message'''


def changed_price_msg(counter, saved_price, current_price, item_name):
    new_datetime = get_datetime()
    msg = f"{Fore.LIGHTGREEN_EX}" \
          f"Price changed from {saved_price}{currency_symbol} to {current_price}{currency_symbol}" \
          f"{Fore.RESET}"
    print(f"{counter}. {new_datetime} {right_arrow} {msg} {right_arrow} {item_name}")
    return msg


'''Function for message when price did not changed '''


def price_did_not_changed(counter, current_price, item_name):
    new_datetime = get_datetime()
    msg = f"{Fore.RED}" \
          f"Cost didn't changed, current price: {current_price}{currency_symbol}" \
          f"{Fore.RESET}"
    print(f"{counter}. {new_datetime} {right_arrow} {msg} {right_arrow} {item_name}")
    return msg


'''
A message that the price of the selected products has not changed
'''


def price_of_selected_items_did_not_changed(count_of_items):
    print(f"{Fore.LIGHTRED_EX}"
          f"The price on {Fore.RESET}"
          f"{Fore.BLUE}{count_of_items}{Fore.RESET} "
          f"{Fore.LIGHTRED_EX}items hasn't changed.{Fore.RESET}")
