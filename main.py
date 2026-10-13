import os
import csv
import datetime as dt
import pandas
import random
import smtplib

my_email = os.environ.get("my_email")
password = os.environ.get("password")

now=(dt.datetime.now().month,dt.datetime.now().day)
data=pandas.read_csv('birthdays.csv')
birthdays_dict = {(data_row["month"],data_row["day"]):data_row for (index, data_row) in data.iterrows()}
if now in birthdays_dict:
    birthday_person=birthdays_dict[now]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as f:
        contents=f.read()
        contents=contents.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday:\n\n{contents}")
#
