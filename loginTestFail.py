from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
user = "petar"
pwd = "pppp"

browser.maximize_window()
browser.get("https://mystrainprint.com/login")

wait = WebDriverWait(browser, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/ui-view/main/div/div[1]/div[2]/form/button')))

username = browser.find_element_by_xpath("/html/body/div/ui-view/main/div/div[1]/div[2]/form/div[1]/input")
username.send_keys(user)

password = browser.find_element_by_xpath("/html/body/div/ui-view/main/div/div[1]/div[2]/form/div[2]/input")
password.send_keys(pwd)

login = browser.find_element_by_xpath("/html/body/div/ui-view/main/div/div[1]/div[2]/form/button")
login.click()

try:
	element = wait.until(EC.visibility_of_element_located((By.XPATH , '/html/body/div/ui-view/main/div/div[1]/div[2]/form/div[2]/p[2]')))
except NoSuchElementException:
	print("Test Fail")
	browser.close()

assert 'https://mystrainprint.com/login' in browser.current_url

print("Test successful")
browser.close()
