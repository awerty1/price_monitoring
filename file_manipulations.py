from datetime import datetime


# Global variable
price_file = "price.txt"

'''Create a price.txt file to save the price'''


def create_file_to_price():
    with open(price_file, "w") as f:
        f.write("0")


'''Saving price to file price.txt'''


def save_price_to_file(price):
    with open(price_file, "w") as f:
        f.write(price)


'''Read price from file price.txt'''


def read_price_from_file():
    with open(price_file, "r") as f:
        saved_price = f.read()
    return saved_price


'''Function to save price changes to a file price_change.txt'''


def save_price_changes_to_file(counter, msg, item_name):
    now = datetime.now()
    # Date format 2023-05-20 18:19:31
    new_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    price_changes_file = 'price_change.txt'
    with open(price_changes_file, mode='a', encoding='utf-8', newline='') as f:
        f.write(f"{counter}. {new_datetime}: {msg} : {item_name}\n")
