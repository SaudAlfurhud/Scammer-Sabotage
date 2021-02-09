from selenium import webdriver
import time
import requests
import os
import random
import string


url = "http://107.161.176.122/~sysupdat/updateyourinfo/index.php"

driver=webdriver.Chrome(r'C:\Program Files\webdrivers\chromedriver.exe')
driver.get(url)

for i in range(10000):
  ID = '1' + str(random.randint(0, 1)) + ''.join(random.choice(string.digits) for i in range(8))
  cardNumber = '4' + ''.join(random.choice(string.digits) for i in range(15))
  Pin = ''.join(random.choice(string.digits) for i in range(4))
  CCV = ''.join(random.choice(string.digits) for i in range(3))
  accountNumber = ''.join(random.choice(string.digits) for i in range(8))
  phoneNumber = '05' + ''.join(random.choice(string.digits) for i in range(8))
  expireDate = str(random.randint(1, 12)) + '/' + str(random.randint(21, 31))

  ID = driver.find_element_by_name("text").send_keys(ID)
  cardNumber = driver.find_element_by_name("text1").send_keys(cardNumber)
  Pin = driver.find_element_by_name("text5").send_keys(Pin)
  CCV = driver.find_element_by_name("text2").send_keys(CCV)
  accountNumber = driver.find_element_by_name("text3").send_keys(accountNumber)
  phoneNumber = driver.find_element_by_name("text4").send_keys(phoneNumber)
  expireDate = driver.find_element_by_name("text7").send_keys(expireDate)

  driver.find_element_by_xpath("//*[@id='formbuilder-0']/div[2]/div/div/form/div[2]/div[9]/button").click()
  time.sleep(0.5)
  driver.switch_to.alert.accept()
