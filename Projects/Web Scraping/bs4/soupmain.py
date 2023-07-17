from bs4 import BeautifulSoup

with open('index.html') as html_file:
    content = html_file.read()

soup = BeautifulSoup(content, "html.parser")

anchors = (soup.find_all(name='a'))

for tag in anchors:
    # print(tag.getText())
    # print(tag.get('href'))
    pass

url = soup.select(selector=".money")
print(url)