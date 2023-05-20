from datetime import datetime
'''
saving price to file price.txt
'''


def save_price_to_file(price):
    with open("price.txt", "w") as f:
        f.write(price)



#read price from price
def read_price_from_file():
    with open("price.txt", "r") as f:
        saved_price = f.read()
    return saved_price

# Создаем файл price.txt для сохранения цены
def create_file_to_price():
    with open("price.txt", "w") as f:
        f.write("0")


def save_price_changes_to_file(counter, msg):
    now = datetime.now()
    # формат даты
    new_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    with open('price_change.txt', mode='a', encoding='utf-8', newline='') as f:
        f.write(f"{counter}. {new_datetime}: {msg}\n")