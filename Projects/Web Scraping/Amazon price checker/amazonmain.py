import requests
from bs4 import BeautifulSoup
import smtplib

mail = 'kkhpythonsender@gmail.com'
password = 'vbscgvckljwlrftz'
to = 'charbelsm2006@gmail.com'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 '
                  'Safari/537.36',
    "Accept-Language": 'en-US,en;q=0.9',


}
link = 'https://www.amazon.com/Skytech-Azure-Gaming-PC-Desktop/dp/B0BXCJVKHF/ref=sr_1_3?crid=3FMC098SUIWHA&keywords' \
       '=pc&qid=1687024619&sprefix=%2Caps%2C1160&sr=8-3&th=1'
response = requests.get(link, headers=headers)
data = response.text

soup = BeautifulSoup(data, 'html.parser')
price_whole = soup.find(name='span', class_="a-price-whole").getText()
price_decimal = soup.find(name='span', class_="a-price-fraction").getText()
price = price_whole + price_decimal
price = price.replace(',', '')
print(price)

productname = soup.find(name='span', id="productTitle").getText().encode('utf-8').strip()
print(productname)
if float(price) < 1000:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=mail, password=password)
        connection.sendmail(from_addr=mail, to_addrs='karimhawwa@gmail.com', msg=f"Subject: Pc dropped to 1k\n\nPrice "
                                                                                 f"of {productname} you were viewing "
                                                                                 f"dropped to {price}\n link={link}")
        print('mail sent')