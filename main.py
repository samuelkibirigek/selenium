from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:/Users/Sam/Desktop/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com/s?k=macbook+air&crid=2YWRWXF10W9F&sprefix=macbook+air%2Caps%2C952&ref=nb_sb_noss_1")
price = driver.find_element(By.CSS_SELECTOR, "span .a-price-fraction")
print(price.text)
driver.quit()



