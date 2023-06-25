import time
import smtplib
from email.mime.text import MIMEText

from colorama import Fore

import config
import config_example

'''Function to send a message'''


def send_email_to(item_name_saved_price_current_price):
    try:
        smtp_server = config.smtp_server
        smtp_port = config.smtp_port

        smtp_username = config.login
        smtp_password = config.password

        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()
        smtp_connection.login(smtp_username, smtp_password)

        count_of_new_lines = "<br>"*6
        new1_line = "<br>"

        '''
        msg = f'Цена на товар <b>{item_name}</b> ' \
              f'изменилась с {saved_price}{currency_symbol} на ' \
              f'{current_price}{currency_symbol}{count_of_new_lines}' \
              f'С уважением, ' \
              f'<br>Leonard Nimoy'
        '''
        msg = f'<b>Изменились цены на следующие товары:</b>{new1_line}'
        for counter, item in enumerate(item_name_saved_price_current_price, start=1):
            msg += f'{counter}. {item}{new1_line}'
        msg += f'{count_of_new_lines}С уважением, ' \
               f'{new1_line}Leonard Nimoy'

        # plain - for pure text without formatting
        # html - for text with html tags
        message = MIMEText(msg, 'html')
        message['Subject'] = f'Изменение цены'
        message['From'] = smtp_username
        message['To'] = config.recipient_email

        smtp_connection.send_message(message)
        print(f"{Fore.LIGHTGREEN_EX}"
              f"Sent msg to email:"
              f"{Fore.RESET} "
              f"{Fore.LIGHTWHITE_EX}{config.recipient_email}{Fore.RESET}")
        time.sleep(2)
        smtp_connection.quit()
    except smtplib.SMTPException as exception:
        print(f"SMTP error occurred: {exception}")
    except Exception as exception:
        print(f"Error sending email: {exception}")
