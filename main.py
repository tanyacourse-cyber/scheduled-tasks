# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import pandas
import smtplib
import datetime
import random

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

def send_email(to_email, content):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject: Happy Birthday\n\n{content}.")

def get_letter(name1):
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as f:
        initial_letter = f.read()
        letter = initial_letter.replace("[NAME]", name1)
        return letter


data = pandas.read_csv("birthdays.csv")
all_birthdays = data.to_dict("records")

# print(all_birthdays)

today = datetime.datetime.now()
today_day = today.day
today_month = today.month
# print(now_month)
# print(now_day)

for n in all_birthdays:
    if n["day"] == today_day and n["month"] == today_month:
        name = n["name"]
        email = n["email"]
        send_email(email, get_letter(name))
