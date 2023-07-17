import requests
import datetime
import smtplib
mail = 'kkhpythonsender@gmail.com'
password = 'vbscgvckljwlrftz'
to = 'karimhawwa@gmail.com'
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_stocks = 'PA4D0XG558PFVY4S'

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': API_KEY_stocks


}
connection = requests.get(url='https://www.alphavantage.co/query', params=parameters)
connection.raise_for_status()
data = connection.json()
year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day

if day - 1 < 10:
    day = f'0{day}'
if month < 10:
    month = f'0{month}'
day1_open = data['Time Series (Daily)'][f"{year}-{month}-{int(day)-1}"]['1. open']
day1_close = data['Time Series (Daily)'][f"{year}-{month}-{int(day)-1}"]['4. close']

difference = round(100 * (float(day1_close) - float(day1_open) ) / float(day1_open), 2)
print(difference)
if difference < 0:
    difference = f'🔻{-difference}'.encode('utf-8')
else:
    difference = f'🔺{difference}'.encode('utf-8')


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
API_KEY_news = '21a03921f5f448de98e5dfa1cb511dc9'

parameters = {
    'q': 'Tesla',
    'from': f"{year}-{month}-{int(day)-1}",
    'sortBy': 'popularity',
    'apiKey': API_KEY_news

}
connection_news = requests.get(url='https://newsapi.org/v2/everything', params=parameters)
connection_news.raise_for_status()
news_data = connection_news.json()
article1 = news_data['articles'][:3][0]['description'].encode('utf-8')
article2 = news_data['articles'][:3][1]['description'].encode('utf-8')
article3 = news_data['articles'][:3][2]['description'].encode('utf-8')


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=mail, password=password)
    connection.sendmail(from_addr=mail, to_addrs=to, msg=f"Subject:{STOCK}:{difference}\n\narticle1:{article1}\narticle2:{article2}\narticle3:{article3}")

