import requests
import bs4


response = requests.get("https://news.ycombinator.com/news")
webpage = response.text
print(webpage)
soup = bs4.BeautifulSoup(webpage, "html.parser")

title = soup.find(name="a", rel="noreferrer").getText()
print(title)
link = soup.find(name="a", rel="noreferrer").get("href")
print(link)
upvote = soup.find(name="span", class_="score").getText()
print(upvote)
