from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\Users\User\Desktop\Devellopement\chromedriver.exe"

service = Service(r'C:\Users\User\Desktop\Devellopement\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com")

# driver.close() #Closes on tab
# driver.quit() #closes crome

driver.find_element(By.ID, "id")
driver.find_element(By.NAME, "name")
driver.find_element(By.XPATH, "xpath")
driver.find_element(By.LINK_TEXT, "link text")
driver.find_element(By.PARTIAL_LINK_TEXT, "partial link text")
driver.find_element(By.TAG_NAME, "tag name")
driver.find_element(By.CLASS_NAME, "class name")
driver.find_element(By.CSS_SELECTOR, "css selector")