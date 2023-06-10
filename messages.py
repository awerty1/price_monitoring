from datetime import datetime


# global variable
right_arrow = "=>"

'''Function for getting time'''


def get_datetime():
    now = datetime.now()
    # Date format 2023-05-20 18:19:31
    new_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    return new_datetime


'''Message when the script starts'''


def start_msg():
    starting_msg = f" Script to price monitoring started! "
    hash_symbols = '#'*5
    print(f"{hash_symbols}{starting_msg}{hash_symbols}")


'''Function for changed price message'''


def changed_price_msg(counter, saved_price, current_price):
    new_datetime = get_datetime()
    msg = f"Price changed from {saved_price}₽ to {current_price}₽"
    print(f"{counter}. {new_datetime} {right_arrow} {msg}")
    return msg


'''Function for message when price did not changed '''


def price_did_not_changed(counter, current_price):
    new_datetime = get_datetime()
    msg = f"Cost did not changed: {current_price}₽"
    print(f"{counter}. {new_datetime} {right_arrow} {msg}")
    return msg
