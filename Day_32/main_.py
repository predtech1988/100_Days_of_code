import datetime as dt
from random import randint, choice
import smtplib

user_name = "masters.way.info@gmail.com"
user_password = "A1D319E1EDEC09B351FD470DC8BE4EF06E83"

def send_mail():
    quotes = []
    with open("Day_32/quotes.txt", encoding="utf-8-sig") as f:
        quotes = [item for item in f.readlines()]
    quote = choice(quotes)
    message_text = quote.split("–")[0]
    sender = quote.split("–")[1]

    message = f"Subject: Greetings from {sender} \n\n Hello my friend, here is your random message ^_^: {message_text}".encode('utf-8')

    with smtplib.SMTP("smtp.elasticemail.com", port= 2525) as connection:
        connection.starttls()
        connection.login(user=user_name, password=user_password)
        connection.sendmail(from_addr= user_name,
        to_addrs="predtech1988@gmail.com",
        msg=message)


now = dt.datetime.now()
if now.weekday() == 3:
    print("CHETVERG")
    send_mail()


