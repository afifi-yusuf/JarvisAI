from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://amazon.ae")
print(driver.title)

search = driver.find_element_by_id("twotabsearchtextbox")
search.send_keys("laptop")
search.send_keys(Keys.RETURN)

link = driver.find_element_by_link_text("Apple")
link.click()

product = driver.find_element_by_link_text("Apple MacBook MRQP2B/A Laptop Intel Core i5 1.3GHz Dual Core 12-Inch with Retina 8GB 512GB SSD Intel HD Graphics 615 MacOs Eng-Kb Gold")
product.click()

cart = driver.find_element_by_id("add-to-cart-button")
cart.click()

cart = driver.find_element_by_id("siNoCoverage")
cart.click()