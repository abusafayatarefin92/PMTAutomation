from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


#Install driver
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.maximize_window()

#Open the app
driver.get("https://testpmt.azurewebsites.net/")
driver.implicitly_wait(time_to_wait= 20)

#Go to Login Page
driver.find_element(By.XPATH, '(//a[@class=\'btn login-button\'])[1]').click()
time.sleep(5)

#Login to the System
driver.find_element(By.XPATH, '(//input[@id=\'Email\'])[1]').send_keys('bangladeshuser@gmail.com')
time.sleep(1)
driver.find_element(By.XPATH, '(//input[@id=\'Password\'])[1]').send_keys('12345')
time.sleep(1)
driver.find_element(By.XPATH, '(//button[normalize-space()=\'LOGIN\'])[1]').click()
time.sleep(5)

#Select Region & Implementing Office
driver.find_element(By.XPATH, '(//span[@class="select2-selection select2-selection--single"])[1]').click()
time.sleep(2)
driver.find_element(By.XPATH, '(//li[@role="option"])[1]').click()
time.sleep(3)
driver.find_element(By.XPATH, '(//span[@role=\'combobox\'])[2]').click()
time.sleep(2)
driver.find_element(By.XPATH, '(//li[@role="option"])[2]').click() #(//li[@id='select2-CountryIdvmwo810d6sk4ky8zev7qk-result-1enx-5'])[1]
time.sleep(3)

#Strategy Milestone Monitoring
driver.find_element(By.XPATH, '(//a[@class=\'nav-link dropdown-toggle tw-text-gray-700 tw-text-xl\'])[1]').click()
time.sleep(1)

#Strategic Goals
driver.find_element(By.XPATH, '(//a[@class=\'dropdown-item tw-text-gray-700 tw-text-xl hover:tw-bg-gray-800 hover:tw-text-white\'][normalize-space()=\'Strategic Goals\'])[1]').click()
time.sleep(5)
driver.find_element(By.XPATH, '(//span[@class=\'kt-input-icon__icon kt-input-icon__icon--right\'])[1]').click()
time.sleep(1)
driver.find_element(By.XPATH, '(//span[@role=\'combobox\'])[3]').click()
time.sleep(1)
driver.find_element(By.XPATH, '(//li[@role="option"])[1]').click()
time.sleep(2)
driver.find_element(By.XPATH, '(//span[@role=\'combobox\'])[4]').click()
time.sleep(1)
driver.find_element(By.XPATH, '(//li[@role="option"])[2]').click()
time.sleep(2)
driver.find_element(By.XPATH, '(//span[@id=\'jfSearch\'])[1]').click()
time.sleep(5)


time.sleep(5)
driver.close()
driver.quit()