import random
import smtplib
import datetime as dt

MY_EMAIL = "falakshair.apptest@gmail.com"
MY_PASSWORD = "falak1234"

now = dt.datetime.now()
day = now.weekday()
if day == 1:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="falakshair.563@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
