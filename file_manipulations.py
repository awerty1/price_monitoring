from datetime import datetime

# Global variable
price_file = "price.txt"
prices = {}
changed_items = []
currency_symbol = "₽"

# '''Create a price.txt file to save the price'''
#
#
# def create_file_to_price():
#     with open(price_file, "w") as f:
#         f.write("0")


# '''Saving price to file price.txt'''
#
#
# def save_price_to_file(price):
#     with open(price_file, "w") as f:
#         f.write(price)


# '''Read price from file price.txt'''
#
#
# def read_price_from_file():
#     with open(price_file, "r") as f:
#         saved_price = f.read()
#     return saved_price

'''Save changed price to changed_items'''


def save_changed_price_to_changed_items(item_name, current_price, old_price):
    changed_items.append(f'{item_name}: '
                         f'{old_price}{currency_symbol} -> '
                         f'{current_price}{currency_symbol}')
    #print(changed_items)


'''Read all items from changed_items'''


def read_price_from_changed_items():
    return list(changed_items)


'''Saving price to dictionary'''


def save_price_to_prices(item_name, price):
    prices[price] = item_name
    #print(prices)


'''Read price from prices'''


def read_price_from_prices(item_name):
    # If there is no price in the dictionary to select, the function will return 0
    return prices.get(item_name, 0)


'''Function to save price changes to a file price_change.txt'''


def save_price_changes_to_file(counter, msg, item_name):
    now = datetime.now()
    # Date format 2023-05-20 18:19:31
    new_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    price_changes_file = 'price_change.txt'
    with open(price_changes_file, mode='a', encoding='utf-8', newline='') as f:
        f.write(f"{counter}. {new_datetime}: {msg} : {item_name}\n")


'''Function to read links line by line(generator)'''


def read_links(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()
