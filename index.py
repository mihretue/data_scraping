from selenium import webdriver

try:
   driver = webdriver.Chrome()

   driver.get("http://selenium.dev")

except Exception as e:
    print("An error occurred:", e)
