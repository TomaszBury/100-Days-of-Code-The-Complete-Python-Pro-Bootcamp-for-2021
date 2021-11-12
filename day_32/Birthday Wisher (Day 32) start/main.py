import smtplib
import datetime as dt
import random

MY_EMAIL = "erica.schultz54@ethereal.email"
PASSWORD = "AMUEYVnjQHdmDEFUu3"
WHEN_TO_SEND = 4


now = dt.datetime.now()
weekday = now.weekday()
if weekday == WHEN_TO_SEND:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()

    quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.ethereal.email", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="tomasz.bury@fake_at_fake.uk",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )



