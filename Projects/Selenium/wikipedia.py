from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_driver_path = r"C:\Users\User\Desktop\Devellopement\chromedriver.exe"

service = Service(r'C:\Users\User\Desktop\Devellopement\chromedriver.exe')

driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.maximize_window()
# Wikipedia = driver.find_element(By.LINK_TEXT, "Wikipedia")
# Wikipedia.click()

search = driver.find_element(By.NAME, 'search')
search.send_keys("PYTHON")
search.send_keys(Keys.ENTER)
input('>')