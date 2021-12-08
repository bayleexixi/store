from  selenium import  webdriver
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8080/HKR/")

driver.maximize_window()
time.sleep(3)
#点击注册链接
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[1]").click()
time.sleep(1)
# 输入
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("baylee")
driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[2]").send_keys("希希")
driver.find_element_by_xpath("//*[@id='pwd']").send_keys(123456)
driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[4]").send_keys(123456)
driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[5]").click()


#第二步
driver.find_element_by_xpath("//*[@id='valid_age']").send_keys(22)
time.sleep(1)
driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/select[1]").send_keys("女")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='classname']").send_keys("测试开发")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/input[3]").click()

#第三步
driver.find_element_by_xpath("//*[@id='reg_mail']").send_keys("674352025@qq.com")
driver.find_element_by_xpath("//*[@id='reg_phone']").send_keys(13875554367)
time.sleep(1)
driver.find_element_by_xpath("//*[@id='msform']/fieldset[3]/textarea").send_keys("北大路清华街道")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='btn_reg']").click()

