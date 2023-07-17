import random
import smtplib
import datetime as dt

mail = 'kkhpythonsender@gmail.com'
password = 'vbscgvckljwlrftz'
to = 'charbelsm2006@gmail.com'

number = 0

current_date = dt.datetime.now().day
print(current_date)


with open(file="quotes.txt", mode='r') as file:
    quotes = file.readlines()
number += 1
quote = random.choice(quotes)
time = str(current_date)
with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=mail, password=password)
    connection.sendmail(from_addr=mail, to_addrs=to, msg=f"Subject:Quote of the day : Day{time}\n\n {quote}")
    connection.sendmail(from_addr=mail, to_addrs='karimhawwa@gmail.com', msg=f"Subject:Quote of the day : Day{time}\n\n {quote}")
    connection.sendmail(from_addr=mail, to_addrs='charbelgebrayel16@gmail.com', msg=f"Subject:Quote of the day : Day{time}\n\n {quote}")