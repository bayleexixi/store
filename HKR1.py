from  selenium import  webdriver
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8080/HKR/")

driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="loginname"]').send_keys("baylee")
driver.find_element_by_xpath('//*[@id="password"]').send_keys(123456)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="submit"]').click()
driver.find_element_by_xpath('//*[@id="img"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ul_pic"]/li[4]/img').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="file1"]').send_keys(r"C:\Users\admin\Desktop\u.jpg")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="pic_btn"]').click()
driver.find_element_by_xpath('//*[@id="tt"]/div[1]/div[3]/ul/li[1]/a/span[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="_easyui_tree_10"]/span[4]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="top"]/div/a[2]/img').click()
time.sleep(1)








time.sleep(2)

driver.quit()