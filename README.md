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
1. 2023-06-10 23:58:22 => Price changed from 0₽ to 600₽
Sent msg to email: somebody@example.com
2. 2023-06-10 23:58:22 => Cost did not changed: 600₽
3. 2023-06-11 00:06:38 => Cost did not changed: 600₽
4. 2023-06-11 00:06:46 => Cost did not changed: 600₽
5. 2023-06-11 00:06:54 => Cost did not changed: 600₽
```
## Feature list
- [ ] Adding multiple links
- [ ] Adding links from different marketplaces
- [ ] Send one email in case of price change
