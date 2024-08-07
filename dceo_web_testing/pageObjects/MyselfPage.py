from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time
class MyselfPage:
    
    Leave_Management=(By.XPATH,f'//app-my-self/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Leave Management"]]/div[1]/div/div/div/img[1]')
    Event_Dynamics=(By.XPATH,f'//app-my-self/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Event Dynamics"]]/div[1]/div/div/div/img[1]')
    Leader_Reimbursements=(By.XPATH,f'//app-my-self/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Leader Reimbursements"]]/div[1]/div/div/div/img[1]')
    My_Profile=(By.XPATH,f'//app-my-self/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="My Profile"]]/div[1]/div/div/div/img[1]')
    Work_Meal=(By.XPATH,f'//app-my-self/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Work Meal"]]/div[1]/div/div/div/img[1]')
    Self_Assessment=(By.XPATH,f'//app-my-self/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Self-Assessment"]]/div[1]/div/div/div/img[1]')
    Reward_Program=(By.XPATH,f'//app-my-self/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Reward Program"]]/div[1]/div/div/div/img[1]')
    Collaboration_Quotient=(By.XPATH,f'//app-my-self/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Collaboration Quotient"]]/div[1]/div/div/div/img[1]')
    Lofty_goal_buowner_admin=(By.XPATH,f'//app-my-self/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Lofty Goals - BU Owners Admin"]]/div[1]/div/div/div/img[1]')

    def __init__(self, driver):
        self.driver = driver
        
    def get_leave_management(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyselfPage.Leave_Management)
    
    def get_event_dynamics(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyselfPage.Event_Dynamics)
    
    def get_work_meal(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyselfPage.Work_Meal)
    
    def get_leader_reimbursement(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyselfPage.Leader_Reimbursements)
    
    def get_self_assessment(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyselfPage.Self_Assessment)
    
    def get_my_profile(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyselfPage.My_Profile)
    
    def get_reward_program(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyselfPage.Reward_Program)
    
    def get_lofty_goal_bu_owner_admin(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyselfPage.Lofty_goal_buowner_admin)
    
    GiveFeedBackHubMyselfButton=(By.XPATH,"//app-myplan/div/div/div[1]/span")
    def GiveFeedBackHubMyselfPage(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(MyselfPage.GiveFeedBackHubMyselfButton)
    
    def rateDceo(self,rating):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(f"//app-feedback-hub-popup/div[2]/form/div[2]/div/app-star-ratings/div/div[{rating}]")
        
    def rateHomePage(self,rating):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(f"//app-feedback-hub-popup/div[2]/form/div[4]/div/app-star-ratings/div/div[{rating}]")
    
    feedbackText=(By.XPATH,"//app-feedback-hub-popup/div[2]/form/app-reusable-textarea/div/textarea")
    def inputFeedbackText(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(MyselfPage.feedbackText)

    submitfeedbackbutton=(By.XPATH,"//app-feedback-hub-popup/div[2]/form/div[6]/app-action-button[2]/button")
    def submitFeedback(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(MyselfPage.submitfeedbackbutton)
    
    cancelfeedbackbutton=(By.XPATH,"//app-feedback-hub-popup/div[2]/form/div[6]/app-action-button[1]/button")
    def cancelFeedback(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(MyselfPage.cancelfeedbackbutton)
    
    feedbackOkButton=(By.XPATH,"//app-material-confirm-dialog-modal/div[3]/app-action-button/button")
    def FeedBackOk(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH,MyselfPage.feedbackOkButton)