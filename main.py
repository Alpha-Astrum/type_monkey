import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By

# Starting a chrome webdriver with suitable options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

# Giving the url to get
type_monkey = "https://monkeytype.com/"
driver.get(type_monkey)

# Delay added to resolve loading conflicts
time.sleep(3)

# Accept cookies button
accept_cookies = driver.find_element(By.XPATH, "/html/body/div[8]/dialog/div[2]/div[2]/div[2]/button[1]")
accept_cookies.click()
time.sleep(1)

# Select the proper config to type
click_words = driver.find_element(By.XPATH, "/html/body/div[9]/div[2]/main/div/div[1]/div/div[3]/div[2]")
click_words.click()
time.sleep(1)
change_num_words = driver.find_element(By.XPATH, "/html/body/div[9]/div[2]/main/div/div[1]/div/div[6]/div[1]")
change_num_words.click()
time.sleep(1)

# Getting all the words in the line to type
all_words = driver.find_elements(By.CLASS_NAME, "word")
time.sleep(1)

# Started the typing
for word in all_words:
    pyautogui.typewrite(word.text)
    pyautogui.press("space")

