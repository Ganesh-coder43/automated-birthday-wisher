##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
from smtplib import SMTP
import random
# 1. Update the birthdays.csv
place = "[NAME]"
wish = pd.read_csv("birthdays.csv")
data = wish.to_dict(orient='records')
MY_EMAIL = "saiganeshkodidela@gmail.com"
APP_PASSWORD = "wtvfcepxvwkddigo"
now = dt.datetime.now()
month_ = now.month
day_ = now.day

for i in data:
    
    if int(i["month"]) == month_ and int(i["day"]) == day_:

        TO_EMAIL = i["email"]
        num = random.randint(1,3)
        with open(f"letter_templates/letter_{num}.txt") as wish:
            content = wish.read()
        content = content.replace(place,i["name"])
        # print(content)
        message = f"From: {MY_EMAIL}\nTo: {TO_EMAIL}\nSubject: Happy Birthday\n\n{content}"
    
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=APP_PASSWORD)
            
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg = message
            )
# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




