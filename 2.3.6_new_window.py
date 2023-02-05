from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


try: 
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)

	browser.find_element(By.CSS_SELECTOR, "button.trollface").click()

	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)

	#browser.switch_to.alert.accept()

	x = int(browser.find_element(By.ID, "input_value").text)
	y = math.log(abs(12*math.sin(x)))

	browser.find_element(By.ID, "answer").send_keys(str(y))
	browser.find_element(By.CSS_SELECTOR, "button.btn").click()
	print(browser.switch_to.alert.text)


finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(5)
	# закрываем браузер после всех манипуляций
	browser.quit()