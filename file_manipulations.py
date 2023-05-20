from datetime import datetime

'''Create a price.txt file to save the price'''


def create_file_to_price():
    with open("price.txt", "w") as f:
        f.write("0")


'''Saving price to file price.txt'''


def save_price_to_file(price):
    with open("price.txt", "w") as f:
        f.write(price)


'''Read price from file price.txt'''


def read_price_from_file():
    with open("price.txt", "r") as f:
        saved_price = f.read()
    return saved_price


''' Function to save price changes to a file price_change.txt '''


def save_price_changes_to_file(counter, msg):
    now = datetime.now()
    # Date format 2023-05-20 18:19:31
    new_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    with open('price_change.txt', mode='a', encoding='utf-8', newline='') as f:
        f.write(f"{counter}. {new_datetime}: {msg}\n")
