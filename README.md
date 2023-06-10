# Price monitoring 

## Description
Price monitoring - script to price monitoring. (:

## Functions
1. Scheduler - you can set the recurrence of the check to a specific time
2. Mail alert - after changing the price, a message is sent to your email
3. File config - you can set all configs in this file(smtp_server, smtp_port, login, password, 
to, url, path_to_chromedriver)
4. Logging - changing and not changing the price is saved to a file

## Example
```
##### Script to price monitoring started! #####
1. Price changed from 0₽ to 600₽
Sent msg to email: somebody@example.com
2. Cost did not changed: 600₽
3. Cost did not changed: 600₽
4. Cost did not changed: 600₽
5. Cost did not changed: 600₽
```