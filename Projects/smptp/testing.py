import smtplib

mail = 'kkhpythonsender@gmail.com'
password = 'ioaqdedixyuuflxk'
to = 'charbelsm2006@gmail.com'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=mail, password=password)
    for i in range(10):
        connection.sendmail(from_addr=mail, to_addrs=to, msg="Subject:Testing\n\n Hello this is the body of the mail test 123213123")