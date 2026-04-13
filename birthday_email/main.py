import pandas
import random
import smtplib
import datetime

now = datetime.datetime.now()
day = now.day
month = now.month

email = "SENDERS_EMAIL"
password = "APP_PASS"
receiver_address = "RECEIVERS_EMAIL"

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

connection = smtplib.SMTP("SENDERS_MAIL_SMTP_ADDRESS", 587)
connection.starttls()
connection.login(user=email, password=password)

data = pandas.read_csv("birthdays.csv")
for rows in data.itertuples():
    if rows.month == month and rows.day == day:

        with open(f"./letter_templates/{random.choice(letters)}") as df:
            content = df.read()
            final = content.replace("[NAME]", rows.name)

        connection.sendmail(from_addr=email, to_addrs=receiver_address, msg=f"Subject: Happy Birthday {rows.name}\n\n {final}")

connection.close()




