# Price monitoring 

## Description
Price monitoring - script to price monitoring. You can add a link to your favorite product and 
follow the price changes using the script. (:

## Functions
1. Scheduler - you can set the recurrence of the check to a specific time
2. Mail alert - after changing the price, a message is sent to your email
3. File config - you can set all configs in this file(smtp_server, smtp_port, login, password, 
to, url, path_to_chromedriver)
4. Logging - changing and not changing the price is saved to a file

## Example
```
##### Script to price monitoring started! #####
1. 2023-06-23 00:12:55 => Price changed from 0₽ to 690₽ => Блок питания для монитора LG 19V 1.7A (32W) 6.5x4.4мм
2. 2023-06-23 00:13:06 => Price changed from 0₽ to 6790₽ => 2 Тб Внутренний SSD диск Azerty Bory R500 2TB
3. 2023-06-23 00:13:17 => Price changed from 0₽ to 12320₽ => Видеокарта Radeon RX 580 8Gb GDDR5 (RX580 8 Гб) игровая
Sent msg to email: somebody@example.com
4. 2023-06-23 00:13:29 => Cost didn't changed, current price: 690₽ => Блок питания для монитора LG 19V 1.7A (32W) 6.5x4.4мм
5. 2023-06-23 00:13:40 => Cost didn't changed, current price: 6790₽ => 2 Тб Внутренний SSD диск Azerty Bory R500 2TB
6. 2023-06-23 00:13:51 => Cost didn't changed, current price: 12320₽ => Видеокарта Radeon RX 580 8Gb GDDR5 (RX580 8 Гб) игровая
```
## Feature list
- [x] Adding multiple links
- [x] Send one email in case of price change
- [ ] Adding links from different marketplaces

## Scheduler
1. Run a function every second
    ```
    schedule.every().seconds.do(get_price.get_price_from_site)
    ```
    
2. Run a function every 12 hours
    ```
    schedule.every().hours(12).do(get_price_from_site)
    ```
    
3. Run a function every day at 10:00
    ```
    schedule.every().day.at('10:00').do(get_price_from_site)
    ```
4. Run a function every minutes
    ```
    schedule.every.minutes.do(get_price_from_site)
    ```
