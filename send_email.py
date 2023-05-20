import smtplib
import time
from email.mime.text import MIMEText
import config


def send_email_to(saved_price, current_price):
    try:
        smtp_server = config.smtp_server
        smtp_port = config.smtp_port

        smtp_username = config.login
        smtp_password = config.password

        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()
        smtp_connection.login(smtp_username, smtp_password)

        msg = f'Цена изменилась с {saved_price}₽ на {current_price}₽\n\n\n\n\n\n' \
              f'С уважением, ' \
              f'Leonard Nimoy'

        message = MIMEText(msg, 'plain')
        message['Subject'] = f'Изменение цены'
        message['From'] = smtp_username
        message['To'] = config.to

        smtp_connection.send_message(message)
        print(f"Sent to email: {config.to}")
        time.sleep(2)
        smtp_connection.quit()
    except Exception as e:
        print(f"Error sending email: {e}")
