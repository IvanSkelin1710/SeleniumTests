from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

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

strainSearch = browser.find_element_by_xpath('//*[@id="wrapper"]/aside-nav/aside/nav/ul/li[7]/a/span[2]')
strainSearch.click()

strainSearch = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/ui-view/div/div[1]/form/input')))
strainSearch.send_keys('anxiety')

strainSearch = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="1"]/div')))
strainSearch.click()

strainSearch = wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page"]/ui-view/ui-view/div/div[1]/div[2]/div[1]/div/div[2]/panel-content/div/div[4]'), 'AVG EFFICACY'))

try:
	symptomInfo = browser.find_element_by_xpath('//*[@id="page"]/ui-view/ui-view/div/div[1]/div[2]/div[1]/div/div[2]/panel-content/div')
	filterStrains = browser.find_element_by_xpath('//*[@id="page"]/ui-view/ui-view/div/div[1]/div[2]/div[2]')
	topStrains = browser.find_element_by_xpath('//*[@id="page"]/ui-view/ui-view/div/div[2]')
	print("Anxiety info widgets loaded")
except NoSuchElementException:
	print("Anxiety info widgets not loaded")
	
logout = browser.find_element_by_xpath('//*[@id="page-header"]/div[4]/ul')
ActionChains(browser).move_to_element(logout).perform()
logout = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-header"]/div[4]/ul/li/ul/li[3]')))
logout.click()

element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/footer/ul/li[3]/a')))

print("Test successful")
browser.close()

