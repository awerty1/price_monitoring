import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import schedule
import send_email
# my functions
import config
import config_example
import messages
import file_manipulations


url = config.url
path_to_chromedriver = config.path_to_chromedriver

# Указываем путь к драйверу Chrome
chromedriver_path = webdriver.chrome.service.Service(executable_path=path_to_chromedriver)


# chromedriver_path =

def get_price_from_site():
    global counter
    # Сохранение цены из файла
    saved_price = file_manipulations.read_price_from_file()

    # Настройки для запуска браузера в "безголовом" режиме
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    # Запускаем браузер с указанными настройками
    driver = webdriver.Chrome(service_log_path='NUL', service=chromedriver_path, options=options)

    driver.get(url)
    # driver.refresh()
    time.sleep(3)
    page = driver.page_source
    driver.quit()

    soup = BeautifulSoup(page, 'html.parser')
    container = soup.find_all('ins', attrs={
        'class': 'price-block__final-price'})
    # print(container[0].text.replace(' ', ''))

    # проверяем изменение цены
    current_price = container[0].text.replace("₽", '').replace(' ', '')
    if current_price != saved_price:
        msg = messages.changed_price_msg(counter, saved_price, current_price)
        file_manipulations.save_price_changes_to_file(counter, msg)
        send_email.send_email_to(saved_price, current_price)
    else:
        msg = messages.price_did_not_changed(counter, current_price)
        file_manipulations.save_price_changes_to_file(counter, msg)

    counter += 1

    # сохраняем новую цену в файл
    file_manipulations.save_price_to_file(current_price)


if __name__ == '__main__':
    counter = 1
    messages.start_msg()
    file_manipulations.create_file_to_price()
    # запуск функции каждую секунду
    schedule.every().seconds.do(get_price_from_site)
    # every 12 hours
    #schedule.every().hours(12).do(get_price_from_site)
    # every day at 10:00
    #schedule.every().day.at('10:00').do(get_price_from_site)
    # every minutes
    #schedule.every.minutes.do(get_price_from_site)

    while True:
        schedule.run_pending()
        time.sleep(1)

