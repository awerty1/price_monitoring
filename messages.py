
'''Message when the script starts'''


def start_msg():
    start_msg = f" Script to price monitoring started! "
    print(f"#####{start_msg}#####")


'''Function for changed price message'''


def changed_price_msg(counter, saved_price, current_price):
    msg = f"Price changed from {saved_price}₽ to {current_price}₽"
    print(f"{counter}. {msg}")
    return msg


'''Function for message when price did not changed '''


def price_did_not_changed(counter, current_price):
    msg = f"Cost did not changed: {current_price}₽"
    print(f"{counter}. {msg}")
    return msg
