from selenium.webdriver.common.by import By
import time
 
class HomePage:
    Home=(By.XPATH,'/html/body/app-root/div/app-side-panel-nav/nav/ul[1]/li[1]/a/img[1]')
    MyTransactions=(By.XPATH,'/html/body/app-root/div/app-side-panel-nav/nav/ul[1]/li[3]/a/img[1]')
    MySelf=(By.XPATH,'/html/body/app-root/div/app-side-panel-nav/nav/ul[1]/li[4]/a/img[1]')
    MyLearning=(By.XPATH,'/html/body/app-root/div/app-side-panel-nav/nav/ul[1]/li[5]/a/img[1]')
    MyOrganization=(By.XPATH,'/html/body/app-root/div/app-side-panel-nav/nav/ul[1]/li[6]/a/img[1]')
    MyCommunity=(By.XPATH,'/html/body/app-root/div/app-side-panel-nav/nav/ul[1]/li[7]/a/img[1]')
    Notifications=(By.XPATH,'/html/body/app-root/div/app-side-panel-nav/nav/ul[1]/li[8]/a/img[1]')
 
 
    def __init__(self,driver):
        self.driver=driver
 
    def get_home(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*HomePage.Home)
    
    def get_my_transactions(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*HomePage.MyTransactions)
    
    def get_myself(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*HomePage.MySelf)
    
    def get_my_learning(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*HomePage.MyLearning)
    
    def get_my_organization(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*HomePage.MyOrganization)
    
    def get_my_community(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*HomePage.MyCommunity)
    
    def get_notifications(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*HomePage.Notifications)
    
    
    GiveFeedBackHubHomeButton=(By.XPATH,"//app-myplan/div/div/div[1]/span")
    def GiveFeedBackHubHomePage(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*HomePage.GiveFeedBackHubHomeButton)
    
    def rateDceo(self,rating):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(f"//app-feedback-hub-popup/div[2]/form/div[2]/div/app-star-ratings/div/div[{rating}]")
        
    def rateHomePage(self,rating):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(f"//app-feedback-hub-popup/div[2]/form/div[4]/div/app-star-ratings/div/div[{rating}]")
    
    feedbackText=(By.XPATH,"//app-feedback-hub-popup/div[2]/form/app-reusable-textarea/div/textarea")
    def inputFeedbackText(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*HomePage.feedbackText)

    submitfeedbackbutton=(By.XPATH,"//app-feedback-hub-popup/div[2]/form/div[6]/app-action-button[2]/button")
    def submitFeedback(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*HomePage.submitfeedbackbutton)
    
    cancelfeedbackbutton=(By.XPATH,"//app-feedback-hub-popup/div[2]/form/div[6]/app-action-button[1]/button")
    def cancelFeedback(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*HomePage.cancelfeedbackbutton)
    
    feedbackOkButton=(By.XPATH,"//app-material-confirm-dialog-modal/div[3]/app-action-button/button")
    def FeedBackOk(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH,*HomePage.feedbackOkButton)
    