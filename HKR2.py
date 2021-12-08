from  selenium import  webdriver
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8080/HKR/")

driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/a[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="loginname"]').send_keys("jason")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("admin")

time.sleep(1)
driver.find_element_by_xpath('//*[@id="submit"]').click()
driver.find_element_by_xpath('//*[@id="_easyui_tree_18"]/span[4]/a').click()
driver.find_element_by_xpath('//*[@id="history"]/div/div/div[1]/table/tbody/tr/td[4]/a/span/span[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="history"]/div/div/div[3]/table/tbody/tr/td[7]/input').clear()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="history"]/div/div/div[3]/table/tbody/tr/td[7]/input').send_keys(5)
driver.find_element_by_xpath('//*[@id="history"]/div/div/div[3]/table/tbody/tr/td[10]/a/span/span[2]').click()

time.sleep(2)

driver.quit()