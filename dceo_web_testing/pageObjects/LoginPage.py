from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.DceoLandingPage import DceoLandingPage
import time
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    user_name=(By.XPATH,'//app-login/div/div/div[2]/div[2]/form/div[1]/div[1]/input')
    password=(By.XPATH,'//input[@type="password"]')
    loginButton=(By.XPATH,'//button[contains(text(),"Login")]')

    def get_user_name(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LoginPage.user_name)
    def get_password(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LoginPage.password)
    def login(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*LoginPage.loginButton).click()
        
        dceoLandingPage=DceoLandingPage(self.driver)
        return dceoLandingPage