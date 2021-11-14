import smtplib
import datetime as dt
import random

MY_EMAIL = "erica.schultz54@ethereal.email"
PASSWORD = "AMUEYVnjQHdmDEFUu3"
WHEN_TO_SEND = "11/14/21"
##################### Extra Hard Starting Project ######################
now = dt.datetime.now()
print(now.strftime("%x"))
if now.strftime("%x") == WHEN_TO_SEND:
    print("great")

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




