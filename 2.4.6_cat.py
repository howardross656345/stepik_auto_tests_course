from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


try: 
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser = webdriver.Chrome()
	browser.get(link)

	button = WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element ((By.ID, "price"), "$100")
	)
	browser.find_element(By.ID, "book").click()

	x = int(browser.find_element(By.ID, "input_value").text)
	y = math.log(abs(12*math.sin(x)))

	browser.find_element(By.ID, "answer").send_keys(str(y))
	browser.find_element(By.ID, "solve").click()
	print(browser.switch_to.alert.text)

finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(15)
	# закрываем браузер после всех манипуляций
	browser.quit()
