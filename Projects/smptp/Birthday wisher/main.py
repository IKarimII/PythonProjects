import random

import pandas
import smtplib
import datetime as dt

mail = 'kkhpythonsender@gmail.com'
password = 'vbscgvckljwlrftz'
to = 'charbelsm2006@gmail.com'

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

with open(file='birthdays.csv', mode='r')as birthday_list:
    df_bday = pandas.read_csv(birthday_list)
    month = df_bday['month'].tolist()
    day = df_bday['day'].tolist()

current_time = dt.datetime.now()
current_month = int(current_time.month)
current_day = int(current_time.day)

birth_moth = df_bday[df_bday['month'] == current_month]
current_days = birth_moth[birth_moth['day'] == current_day]
user_name = current_days['name'].astype('string')
names = user_name


if current_month in month and current_day in day:
    letter = random.randint(1, 3)
    with open(file=f"letter_templates/letter_{letter}.txt", mode='r') as letter_temp:
        letter_template = letter_temp.read()
    customized_letter = letter_template.replace('[NAME]', f'{names}')
    print(customized_letter)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=mail, password=password)
        connection.sendmail(from_addr=mail, to_addrs=to,msg=f"Subject:Happy Birthday\n\n{customized_letter}")





