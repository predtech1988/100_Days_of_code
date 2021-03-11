##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import csv
import smtplib
import datetime as dt
from random import choice

USER_NAME = "masters.way.info@gmail.com"
USER_PASSWORD = "A1D319E1EDEC09B351FD470DC8BE4EF06E83"
current_date = dt.datetime.now()
month = current_date.month
day = current_date.day


def send_mail(name, email):
    mail_template = choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])
    try:
        with open (f"Day_32/letter_templates/{mail_template}") as f:
            mail_body = f.read().replace("[NAME]", name)
            message = f"Subject: Happy Birthday {name}! \n\n {mail_body}"            
            with smtplib.SMTP("smtp.elasticemail.com", port= 2525) as connection:
                connection.starttls()
                connection.login(user=USER_NAME, password=USER_PASSWORD)
                connection.sendmail(from_addr= USER_NAME,
                    to_addrs=email,
                    msg=message)
    except FileNotFoundError:
        print("File with letter template not found")


def check_birthdays(file):
    rows = csv.reader(file)
    for row in rows:
        if month == int(row[3]) and day == int(row[4]):     
            print(f"Happy Day {row[0]}")
            send_mail(row[0], row[1])


try:
    with open ("Day_32/birthdays.csv", "r") as f:
        next(f)
        check_birthdays(f)
except FileNotFoundError:
    print("Sorry file not found")



