import schedule

import get_price

'''
Function to set the interval

#variables:
* interval - for every N seconds, minutes, hours, days (int)
* unit - choice between seconds, minutes, hours, days (str)
* time - time string, example :03, 00:03, 00:00:03 (str)
'''


def schedule_job_interval(interval=0, unit='seconds', time=None):
    if time is None:
        if unit == 'seconds':
            schedule.every(interval).seconds.do(lambda: get_price.get_price_from_site())
        elif unit == 'minutes':
            schedule.every(interval).minutes.do(lambda: get_price.get_price_from_site())
        elif unit == 'hours':
            schedule.every(interval).hours.do(lambda: get_price.get_price_from_site())
        elif unit == 'days':
            schedule.every(interval).days.do(lambda: get_price.get_price_from_site())
        else:
            raise ValueError("Invalid time unit")
    elif interval == 0 and time is not None:
        if unit == 'hours':
            # for example :03 => every hour at 03 min
            schedule.every().hour.at(time).do(get_price.get_price_from_site)
        elif unit == 'days':
            # for example 10:03(:30) => every day at 10:03(:30)
            schedule.every().day.at(time).do(get_price.get_price_from_site)
    else:
        raise ValueError("It is not allowed to enter 3 parameters at the same time")

    # Run a function every second
    # schedule.every().seconds.do(get_price.get_price_from_site)
    # every 12 hours
    # schedule.every().hours(12).do(get_price_from_site)
    # every day at 10:00
    # schedule.every().day.at('10:00').do(get_price_from_site)
    # every minutes
    # schedule.every.minutes.do(get_price_from_site)
