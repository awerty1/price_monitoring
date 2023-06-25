# Price monitoring 

## Description
Price monitoring - script to price monitoring. You can add a link to your favorite product and 
follow the price changes using the script. Uses multiple marketplaces. Will work if invalid references were passed (:

## Functions
1. Scheduler - you can set the recurrence of the check to a specific time
2. Mail alert - after changing the price, a message is sent to your email
3. File config - you can set all configs in this file(smtp_server, smtp_port, login, password, 
to, url, path_to_chromedriver)
4. Logging - changing and not changing the price is saved to a file

## Example
```
##### Script to price monitoring started! #####
Invalid site name: incorrectlink
Opening marketplace, link: https://sitename.com/catalog/details/blok-pitaniya-dlya-lg-hp-19v-474a-600005735977/
1. 2023-06-25 22:14:04 => Price changed from 0₽ to 1616₽ => Блок питания для LG / HP 19V 4.74A
Opening marketplace, link: https://www.sitename.com/product/blok-pitaniya-dlya-monitora-lg-19v-1-7a-32w-6-5x4-4mm-s-igloy-3
2. 2023-06-25 22:14:16 => Price changed from 0₽ to 447₽ => Блок питания для монитора LG 19V 1.7A (32W) 6.5x4.4мм с иглой
Opening marketplace, link: https://sitename.com/product--mistral-krupa-pshenichnaia-bulgur/1778155701
3. 2023-06-25 22:14:29 => Price changed from 0₽ to 69₽ => Мистраль крупа пшеничная Булгур, 500 г
Opening marketplace, link: https://www.sitename.com/catalog/534534/detail.aspx
4. 2023-06-25 22:14:40 => Price changed from 0₽ to 690₽ => Блок питания для монитора LG 19V 1.7A (32W) 6.5x4.4мм
Opening marketplace, link: https://www.sitename.com/catalog/12312/detail.aspx
5. 2023-06-25 22:14:51 => Price changed from 0₽ to 6790₽ => 2 Тб Внутренний SSD диск Azerty Bory R500 2TB
Opening marketplace, link: https://www.sitename.com/catalog/432425/detail.aspx
6. 2023-06-25 22:15:02 => Price changed from 0₽ to 11440₽ => Видеокарта Radeon RX 580 8Gb GDDR5 (RX580 8 Гб) игровая
Error processing link '': Invalid link format
Error processing link 'fds': Invalid link format
Error processing link '': Invalid link format
Error processing link '': Invalid link format
Sent msg to email: somebody@example.com
Opening marketplace, link: https://sitename.ru/catalog/details/blok-pitaniya-dlya-lg-hp-19v-474a-600005735977/
7. 2023-06-25 22:14:04 => Cost didn't changed, current price: 1616₽ => Блок питания для LG / HP 19V 4.74A
```
## Feature list
- [x] Adding multiple links
- [x] Send one email in case of price change
- [x] Adding links from different marketplaces

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
   
## Instructions for use
1. Add links to file links.txt
2. Set scheduler start time in "main.py"
3. Fill in your configs in a file "config_example.py"