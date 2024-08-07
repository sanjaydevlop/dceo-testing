from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time
 
class DceoLandingPage:
    def __init__(self, driver):
        self.driver = driver
    arrowButton=(By.XPATH,'//app-dceo-chat/div/div[2]/figure/img')
    Dashboard_button=(By.XPATH,'//mat-button-toggle/button[div[text()=" Dashboard "]]')
    myTransactionsUnderArrow=(By.XPATH,'/html/body/app-root/div/div/app-dceo-chat/div/div/div/div/div/div[2]/p[text()="MyTransactions"]')
    def get_arrowButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*DceoLandingPage.arrowButton)
    
    def get_data(self,tab):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH,f'/html/body/ngb-modal-window/div/div/div/div[2]/div/div[3]/div/div/div[2]/p[text()="{tab}"]')
    
    def get_dashboard_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*DceoLandingPage.Dashboard_button)