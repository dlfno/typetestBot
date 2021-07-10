from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import logging
import random
import string

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

characters = string.ascii_letters + string.digits

def generateRandomChars(chars, num, qt):
  random_chars = []
  for i in range(qt):
    random_chars.append(''.join([random.choice(chars) for _ in range(num)]))
  return random_chars


def enter_text(driver, elem, text, delay=0):
  driver.find_element_by_css_selector(elem).send_keys(text)

  if delay:
    sleep(delay)


while True:
  driver = webdriver.Firefox()
  driver.maximize_window()
  # driver.get('https://typetest.io/signup')
  # username, password, email = generateRandomChars(characters, 8, 3)

  # email += "@gmail.com"

  # for elem, credential in zip(["username", "email", "password"], [username, email, password]):
  #   sleep(2)
  #   enter_text(driver, f'input#{elem}', credential)

  # sleep(2)
  # enter_text(driver, "input#password", Keys.ENTER)

  # with open('accounts.txt', 'a+') as f:
  #   for credential in [username, password, email]:
  #     f.write(f'{credential}\n')
  #   f.write('\n')

  driver.get('https://typetest.io/login')

  with open('credentials.txt', 'r+') as f:
    email, password, *_ = f.read().split('\n')

  email_elem = driver.find_element_by_css_selector("input#email")
  email_elem.send_keys(email)
  sleep(2)

  password_elem = driver.find_element_by_css_selector("input#password")
  password_elem.send_keys(password)

  password_elem.send_keys(Keys.ENTER)
  sleep(2)
  driver.get('https://www.typetest.io')

  sleep(5)

  try:
    driver.find_element_by_css_selector("span[value='10000']").click()

    test_input = driver.find_element_by_css_selector("input#test-input")

    sleep(1)

    # letterSpeed = .0005

    while True:
      words_elems = driver.find_elements_by_css_selector("span.test-word")
      words = [word.text for word in words_elems if len(word.get_attribute("class").split()) == 1]

      # Entire word
      # test_input.send_keys(f"{words[0]} ")
      # sleep(1)
      # Each letter
      for letter in words[0]:
        test_input.send_keys(letter)
        if random.randint(0, 35) == 0:
          test_input.send_keys(f"{random.choice(string.ascii_letters)}")
        sleep(random.randint(1, 10) / 999)
      test_input.send_keys(" ")
      #   # sleep(letterSpeed)

      # test_input.send_keys(" ")
  except Exception as err:
    print(str(err))

  driver.quit()
