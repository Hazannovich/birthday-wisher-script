import datetime as dt
import os
import smtplib
import random
import re
import pandas
# Put your Email here
my_email = "israel.h.bar@gmail.com"
# Use local environment variable or change this to your password
my_password = str(os.environ['EMAIL_PASSWORD'])
date = dt.datetime.now()
this_month = date.month
this_day = date.day
birthdays_data = pandas.read_csv("birthdays.csv")
birthdays = birthdays_data.to_dict(orient='records')
for key in birthdays:
    if key['month'] == this_month and key['day'] == this_day:
        letter = f"./letter_templates/letter_{random.randint(1,4)}.txt"
        with open(letter, 'r') as letter_template:
            my_msg = re.sub(r"\[NAME\]", key['name'], letter_template.read())
            receiver_email = key['email']
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(from_addr=my_email, to_addrs=receiver_email,
                                    msg=f"Subject:Happy Birthday!\n\n{my_msg}")
