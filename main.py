import time
import schedule
# my functions
import messages
import file_manipulations
import get_price


def main():
    # counter = 1
    messages.start_msg()
    file_manipulations.create_file_to_price()
    # запуск функции каждую секунду
    schedule.every().seconds.do(get_price.get_price_from_site)
    # every 12 hours
    # schedule.every().hours(12).do(get_price_from_site)
    # every day at 10:00
    # schedule.every().day.at('10:00').do(get_price_from_site)
    # every minutes
    # schedule.every.minutes.do(get_price_from_site)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
