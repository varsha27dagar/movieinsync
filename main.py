from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

driver = webdriver.Chrome(
    service=ChromiumService(
        ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
    )
)
driver.get("https://demoqa.com/login")

userNameSelector = "userName"
passwordSelector = "password"
loginBtnSelector = "login"


userName = input("Enter username: ")
password = input("Enter password: ")

el = driver.find_element(By.ID, userNameSelector)
el.send_keys(userName)
el = driver.find_element(By.ID, passwordSelector)
el.send_keys(password)

input("Press any key to continue")
el = driver.find_element(By.ID, loginBtnSelector)
el.click()

input("Logged In")
