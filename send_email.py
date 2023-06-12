import smtplib
import time
from email.mime.text import MIMEText

import config
import config_example

'''Function to send a message'''


def send_email_to(saved_price, current_price, item_name):
    try:
        smtp_server = config.smtp_server
        smtp_port = config.smtp_port

        smtp_username = config.login
        smtp_password = config.password

        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()
        smtp_connection.login(smtp_username, smtp_password)

        count_of_new_lines = "<br>"*6
        currency_symbol = "₽"
        msg = f'Цена на товар <b>{item_name}</b> ' \
              f'изменилась с {saved_price}{currency_symbol} на ' \
              f'{current_price}{currency_symbol}{count_of_new_lines}' \
              f'С уважением, ' \
              f'<br>Leonard Nimoy'

        # plain - for pure text without formatting
        # html - for text with html tags
        message = MIMEText(msg, 'html')
        message['Subject'] = f'Изменение цены'
        message['From'] = smtp_username
        message['To'] = config.recipient_email

        smtp_connection.send_message(message)
        print(f"Sent msg to email: {config.recipient_email}")
        time.sleep(2)
        smtp_connection.quit()
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"Error sending email: {e}")
