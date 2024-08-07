from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class LeaveManagementPage:
    ApplyLeaveButton=(By.XPATH,'//button/span[contains(text(),"Apply for Leave")]')
    LeaveStatementButton=(By.XPATH,'//button/span[contains(text(),"Leave Statement")]')
    Holiday_List_Button=(By.XPATH,'//button/span[contains(text(),"List of Holidays")]')
    LeavePolicyButton=(By.XPATH,'//button/span[contains(text(),"Leave Policy")]')
    FAQsButton=(By.XPATH,'//button/span[contains(text(),"FAQs")]')
    LeaderNameHeading=(By.XPATH,'/html/body/app-root/div/div/app-leave-management/app-container/div/div[3]/div[1]/div/div[1]/div/div/div[1]/h3/span[1]')
    LeaderName=(By.XPATH,'/html/body/app-root/div/div/app-leave-management/app-container/div/div[3]/div[1]/div/div[1]/div/div/div[1]/h3/span[2]')
    LeaderIdHeading=(By.XPATH,'/html/body/app-root/div/div/app-leave-management/app-container/div/div[3]/div[1]/div/div[1]/div/div/div[2]/h3/span[1]')
    LeaderID=(By.XPATH,'/html/body/app-root/div/div/app-leave-management/app-container/div/div[3]/div[1]/div/div[1]/div/div/div[2]/h3/span[2]')
    ReportingLeaderHeading=(By.XPATH,'/html/body/app-root/div/div/app-leave-management/app-container/div/div[3]/div[1]/div/div[1]/div/div/div[3]/h3/span[1]')
    ReportingLeaderName=(By.XPATH,'/html/body/app-root/div/div/app-leave-management/app-container/div/div[3]/div[1]/div/div[1]/div/div/div[3]/h3/span[2]')
    LeaveBalanceHeading=(By.XPATH,'/html/body/app-root/div/div/app-leave-management/app-container/div/div[3]/div[1]/div/div[2]/div/span')
    LeaveBalance=(By.XPATH,'/html/body/app-root/div/div/app-leave-management/app-container/div/div[3]/div[1]/div/div[2]/div/div/div')
    NameLogo=(By.XPATH,'/html/body/app-root/div/div/app-leave-management/app-container/div/div[3]/div[1]/div/div[1]/div/app-leader-avatar/div/span')
    consolidated_toggle_button=(By.XPATH,'/html/body/ngb-modal-window/div/div/div[2]/div/div/div[1]/div/div/div[1]')
    special_toggle_button=(By.XPATH,'/html/body/ngb-modal-window/div/div/div[2]/div/div/div[1]/div/div/div[2]')
    reason_for_leave=(By.XPATH,'//ngb-modal-window/div/div/div[2]/div/div/div[2]/div/div/ng-select/div')
    select_year_from_date=(By.CSS_SELECTOR,'select[aria-label="Select year"]')
    select_month_from_date=(By.CSS_SELECTOR,'select[aria-label="Select month"]')
    Available_leave_balance=(By.XPATH,'//div[text()=" Available Leave "]/span')
    Applied_leave_balance=(By.XPATH,'//div[text()=" Applied Leave "]/span')
    Loss_of_pay=(By.XPATH,'//div[text()=" Loss of Pay "]/span')
    from_date=(By.XPATH,'//input[@name="dpFromDate"]')
    to_date=(By.XPATH,'//input[@name="dpToDate"]')
    file=(By.ID,'file')
    Submit_button=(By.XPATH,'//button/span[contains(text(),"Submit")]')
    Toast_container=(By.XPATH, '//*[@id="toast-container"]')
    Proceed_button=(By.XPATH,'//button[span[contains(text(),"Proceed")]]')
    specialToDate=(By.XPATH,'//ngb-modal-window/div/div/div[2]/div/div/div[4]/div[2]/form/div/div[2]/input')
    confirm_edit=(By.XPATH,'//button[span[text()=" Edit Leave "]]')
    confirm_cancel_leave=(By.XPATH,'//button[span[text()=" Cancel Leave "]]')
    next_page_button=(By.XPATH,'//a[@aria-label="Next"]')
    cancel_yes=(By.XPATH,'//button[span[text()=" Yes "]]')
    cancel_no=(By.XPATH,'//button[span[text()=" No "]]')
    Delete_confirm=(By.XPATH,'//button[span[text()=" Delete "]]')
    Delete_button=(By.XPATH,"//button[span/mat-icon[text()='delete']]")
    def __init__(self,driver):
        self.driver=driver

    def get_apply_leave_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.ApplyLeaveButton)
    
    def get_leave_statement_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.LeaveStatementButton)
    
    def get_holiday_list_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.Holiday_List_Button)
    
    def get_Leave_Policy_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.LeavePolicyButton)
    
    def get_FAQs_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.FAQsButton)
    
    def get_leader_name_heading(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.LeaderNameHeading)
    
    def get_leader_name(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.LeaderName)
    
    def get_leader_ID_heading(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.LeaderIdHeading)
    
    def get_leader_ID(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.LeaderID)
    
    def get_reporting_leader_heading(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.ReportingLeaderHeading)
    
    def get_reporting_leader_name(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.ReportingLeaderName)
    
    def get_leave_balance_Heading(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.LeaveBalanceHeading)
    
    def get_leave_balance(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.LeaveBalance)
    
    def get_name_logo(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.NameLogo)
    
    def get_consolidated_leave_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.consolidated_toggle_button)
    
    def get_special_leave_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.special_toggle_button)
    
    def get_reason_for_leave(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.reason_for_leave)
    
    def select_reason_for_leave(self,reason):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH,f'//ng-dropdown-panel/div/div/div/span[text()=" {reason} "]')
    
    def get_available_leave_balance(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.Available_leave_balance).text
    
    def get_applied_leave_balance(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.Applied_leave_balance).text
    
    def get_loss_of_pay(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.Loss_of_pay).text
    
    def get_from_date(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.from_date)
    
    def get_to_date(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.to_date)
    
    def select_year(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.select_year_from_date)
    
    def select_month(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.select_month_from_date)
    
    def select_date(self,date):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH,f'//div[1]/ngb-datepicker-month-view/div/div/span[text()=" {date} "]')

    def get_file_element(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.file)    
    
    def get_submit_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.Submit_button)
    
    def get_toast(self):
        time.sleep(2)
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.Toast_container).text
    
    def get_proceed_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.Proceed_button)
    
    def get_partial(self,date):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH,f'//button[span[text()="{date}"]]')
    
    def get_partial_radio_button(self,type):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH,f'//div[label[text()="{type}"]]/input[@name="partial"]')
    
    def get_specialToDate(self):
        time.sleep(2)
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.specialToDate).get_attribute("value")
    
    def get_specialFromDate(self):
        time.sleep(2)
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.from_date).get_attribute("value")
    
    
    def click_on_edit(self,from_date,to_date,type,reason):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH,f'/html/body/app-root/div/div/app-leave-management/app-container/div/div[3]/div[2]/div/div[2]/mat-card/div/div/div/table/tbody/tr[contains(@class, "ng-star-inserted")][td[2][contains(text(),"{from_date}")] and td[3][contains(text(), "{to_date}")] and td[5][text()="{type}"] and td[6][text()="{reason}"]]/td[9]/app-action-button/button[span[text()=" Edit/Cancel "]]')
    
    def get_next_page(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.next_page_button)
    
    def get_cancel_yes(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.cancel_yes)
    
    def get_cancel_No(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.cancel_no)
    
    def get_confirm_edit(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.confirm_edit)
    
    def get_confirm_cancel_leave_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.confirm_cancel_leave)
    
    def click_confirm_delete(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.Delete_confirm).click()
    
    def get_delete_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaveManagementPage.Delete_button)


    
    

    