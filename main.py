from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import logging
import random
from string import ascii_letters

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.typetest.io/login')

with open('credentials.txt', 'r+') as f:
  email, password, *_ = f.read().split('\n')

email_elem = driver.find_element_by_css_selector("input#email")
email_elem.send_keys(email)

sleep(2)

password_elem = driver.find_element_by_css_selector("input#password")
password_elem.send_keys(password, Keys.ENTER)

# driver.get('https://www.typetest.io')

sleep(2)

driver.find_element_by_css_selector("span[value='10000']").click()

test_input = driver.find_element_by_css_selector("input#test-input")

sleep(1)

letterSpeed = .0005

while True:
  words_elems = driver.find_elements_by_css_selector("span.test-word")
  words = [word.text for word in words_elems if len(word.get_attribute("class").split()) == 1]

  # Entire word
  if random.randint(0, 35) != 0:
    test_input.send_keys(f"{words[0]} ")
  else:
    test_input.send_keys("wtf ")

  # Each letter
  # for letter in words[0]:
  #   test_input.send_keys(letter)
  #   # sleep(letterSpeed)
  
  # if random.randint(0, 100) == 0:
  #   test_input.send_keys(f"{random.choice(ascii_letters)}")
  #   # sleep(letterSpeed)

  # test_input.send_keys(" ")
