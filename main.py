from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
EMAIL = "andrefrar@yahoo.gr"
PASSWORD = "charlidamelio17"

TARGET = "alexandros_kopsialis"

driver = webdriver.Chrome(PATH)

driver.get("https://instagram.com")

time.sleep(3)

accept_cookies_btn = driver.find_element_by_class_name("bIiDR")
accept_cookies_btn.click()

time.sleep(2)

# enter the email and password and sign in to the account

email_input = driver.find_element_by_name("username")
email_input.send_keys(EMAIL)
password_input = driver.find_element_by_name("password")
password_input.send_keys(PASSWORD)

login_btn = driver.find_element_by_class_name("DhRcB")
login_btn.click()

time.sleep(3)

search_input = driver.find_element_by_class_name("XTCLo")
search_input.send_keys(TARGET)

time.sleep(3)

# locate the targets profile in the search results
target_reference = driver.find_element_by_class_name("-qQT3")
target_reference.click()

time.sleep(2)

photo_reference = driver.find_element_by_class_name("eLAPa")
photo_reference.click()

time.sleep(2)

message = "@anesths_sps @_sarados_ @nikos_stasinopoulos"

comment_reference = driver.find_element_by_class_name("Ypffh")
comment_reference.click()

time.sleep(2)

comment_reference2 = driver.find_element_by_class_name("focus-visible")

comment_reference2.send_keys(message)

time.sleep(2)

form = driver.find_element_by_class_name("X7cDz")
form.submit()

time.sleep(5)