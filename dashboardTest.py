from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

def checkWidgets():
	try:
		numberOfSesh = browser.find_element_by_xpath('//*[@id="page"]/ui-view/div/div/div[1]/total-sessions/div')
		numberOfProd = browser.find_element_by_xpath('//*[@id="page"]/ui-view/div/div/div[2]/total-strains/div')
		topSymptoms = browser.find_element_by_xpath('//*[@id="page"]/ui-view/div/div/div[1]/top-symptoms-treated/div')
		topStrains = browser.find_element_by_xpath('//*[@id="page"]/ui-view/div/div/div[2]/top-strains-used/div')
		news = browser.find_element_by_xpath('//*[@id="page"]/ui-view/div/div/div[1]/news/div')
		print("widgets have loaded")
	except NoSuchElementException:
		print("widgets have not loaded")

browser = webdriver.Chrome()
user = "petar@strainprint.ca"
pwd = "pppp"

browser.maximize_window()
browser.get("https://mystrainprint.com/login")

wait = WebDriverWait(browser, 15)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/ui-view/main/div/div[1]/div[2]/form/button')))

username = browser.find_element_by_xpath("/html/body/div/ui-view/main/div/div[1]/div[2]/form/div[1]/input")
username.send_keys(user)

password = browser.find_element_by_xpath("/html/body/div/ui-view/main/div/div[1]/div[2]/form/div[2]/input")
password.send_keys(pwd)

login = browser.find_element_by_xpath("/html/body/div/ui-view/main/div/div[1]/div[2]/form/button")
login.click()

try:
	element = wait.until(EC.visibility_of_element_located((By.XPATH , '//*[@id="page"]/ui-view/div/div/div[1]/news/div/div[2]/div/div/img')))
except NoSuchElementException:
	print("Test Fail")
	browser.close()

assert 'https://mystrainprint.com/' in browser.current_url

checkWidgets()

switch = browser.find_element_by_xpath('//*[@id="page-header"]/div[3]/toggle-switch/div/span[2]')
switch.click()

element = wait.until(EC.visibility_of_element_located((By.ID, 'top-strains-used-bar-chart-label-2')))

checkWidgets()
	
logout = browser.find_element_by_xpath('//*[@id="page-header"]/div[4]/ul')
ActionChains(browser).move_to_element(logout).perform()
logout = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-header"]/div[4]/ul/li/ul/li[3]')))
logout.click()

element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/footer/ul/li[3]/a')))

print("Test successful")
browser.close()


