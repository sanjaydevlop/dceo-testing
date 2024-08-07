from selenium.webdriver.common.by import By
import time

class LeaderLeaveRequests:
    Leave_requests_tab=(By.XPATH,'/html/body/app-root/div/div/app-leader-leave-management/app-container/div/div[3]/mat-tab-group/mat-tab-header/div[2]/div/div/div/div[contains(text(),"Leave Requests")]')
    Leave_statement_tab=(By.XPATH,'/html/body/app-root/div/div/app-leader-leave-management/app-container/div/div[3]/mat-tab-group/mat-tab-header/div[2]/div/div/div/div[contains(text(),"Leave Statement")]')
    History_tab=(By.XPATH,'/html/body/app-root/div/div/app-leader-leave-management/app-container/div/div[3]/mat-tab-group/mat-tab-header/div[2]/div/div/div[div[contains(text(),"History")]]')
    Leader_name_search=(By.XPATH,'/html/body/app-root/div/div/app-leader-leave-management/app-container/div/div[3]/mat-tab-group/div/mat-tab-body/div/div/app-record-manager-grid/div/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/app-text-floating-filter/input')
    Leader_Id_search=(By.XPATH,'/html/body/app-root/div/div/app-leader-leave-management/app-container/div/div[3]/mat-tab-group/div/mat-tab-body/div/div/app-record-manager-grid/div/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[1]/app-text-floating-filter/input')
    Requested_date_search=(By.XPATH,'/html/body/app-root/div/div/app-leader-leave-management/app-container/div/div[3]/mat-tab-group/div/mat-tab-body/div/div/app-record-manager-grid/div/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[3]/div[1]/div/div[2]/div/div/div[2]/input')
    from_date_search=(By.XPATH,'/html/body/app-root/div/div/app-leader-leave-management/app-container/div/div[3]/mat-tab-group/div/mat-tab-body/div/div/app-record-manager-grid/div/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[4]/div[1]/div/div[2]/div/div/div[2]/input')
    to_date_search=(By.XPATH,'/html/body/app-root/div/div/app-leader-leave-management/app-container/div/div[3]/mat-tab-group/div/mat-tab-body/div/div/app-record-manager-grid/div/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[5]/div[1]/div/div[2]/div/div/div[2]/input')
    no_of_days_search=(By.XPATH,'/html/body/app-root/div/div/app-leader-leave-management/app-container/div/div[3]/mat-tab-group/div/mat-tab-body/div/div/app-record-manager-grid/div/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[6]/div[1]/div/div/div[2]/input')
    Type_of_leave_search=(By.XPATH,'/html/body/app-root/div/div/app-leader-leave-management/app-container/div/div[3]/mat-tab-group/div/mat-tab-body/div/div/app-record-manager-grid/div/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[7]/div[1]/app-text-floating-filter/input')
    reason_search=(By.XPATH,'/html/body/app-root/div/div/app-leader-leave-management/app-container/div/div[3]/mat-tab-group/div/mat-tab-body/div/div/app-record-manager-grid/div/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[8]/div[1]/app-text-floating-filter/input')
    Approve_button=(By.XPATH,'//button[span[text()=" Approve "]]')
    Reject_button=(By.XPATH,'//button[span[text()=" Reject "]]')
    Reject_reason=(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-view-leave-request-modal/div[2]/div[4]/app-reusable-select/div/ng-select/div/div/div[2]')
    Reason_unselect=(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-view-leave-request-modal/div[2]/div[4]/app-reusable-select/div/ng-select/div/span[1]')
    Cancel_reject_button=(By.XPATH,'//button[span[text()=" Cancel "]]')
    leave_dates=(By.XPATH,'//div[@class="leaveDatesRow"]/div/div')
    Leader_Name=(By.XPATH,'//div[div[1][text()="Leader Name"]]/div[2]')
    Leader_id=(By.XPATH,'//div[div[1][text()="Leader ID"]]/div[2]')
    Reason=(By.XPATH,'//div[div[1][text()="Reason"]]/div[2]')
    Available_Leave=(By.XPATH,'//div[div[1][text()="Available Leave"]]/div[2]')
    Applied_Leave=(By.XPATH,'//div[div[1][text()="Applied Leave"]]/div[2]')
    Loss_of_pay=(By.XPATH,'//div[div[1][text()="Loss of Pay"]]/div[2]')
    Back_dated_leave=(By.XPATH,'//div[@class="backdatedLeaveDiv ng-star-inserted"]')
    History_Status=(By.XPATH,'/html/body/app-root/div/div/app-leader-leave-management/app-container/div/div[3]/mat-tab-group/div/mat-tab-body[3]/div/div/app-record-manager-grid/div/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div[9]')
    Approve_reject_button=(By.XPATH,'//button[span[text()=" Approve/Reject "]]')
    Toast_container=(By.XPATH, '//*[@id="toast-container"]')
    clear_filters=(By.XPATH,'//button[span[text()=" Clear filters "]]')
    header=(By.XPATH,'//div/h2[@class="pageTitle"]')
    reason_header=(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-view-leave-request-modal/div[2]/div[4]/app-reusable-select/div')

    def __init__(self,driver):
        self.driver=driver

    def get_leave_requests_tab(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Leave_requests_tab)
    
    def get_leave_statement_tab(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Leave_statement_tab)

    def get_history_tab(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.History_tab)
    
    def get_leader_name_search(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Leader_name_search)
    
    def get_leader_id_search(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Leader_Id_search)
    
    def get_requested_date_search(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Requested_date_search)
    
    def get_from_date_search(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.from_date_search)
    
    def get_to_date_search(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.to_date_search)
    
    def get_number_of_days_search(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.no_of_days_search)
    
    def get_type_of_leave_search(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Type_of_leave_search)
    
    def get_reason_search(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.reason_search)
    
    def get_approve_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Approve_button)

    def get_reject_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Reject_button)
    
    def get_reject_reason(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Reject_reason)
    
    def select_reason_for_reject(self,reason):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH,f'//ng-dropdown-panel/div/div/div/span[text()="{reason}"]')
    
    def get_reject_reason_unselect_cross(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Reason_unselect)
    
    def get_cancel_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Cancel_reject_button)
    
    def get_leave_dates(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_elements(*LeaderLeaveRequests.leave_dates)
    
    def get_leader_name(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Leader_Name)
    
    def get_leader_id(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Leader_id)
    
    def get_reason(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Reason)
    
    def get_available_leave(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Available_Leave).text
    
    def get_applied_leave(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Applied_Leave).text
    
    def get_loss_of_pay(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Loss_of_pay).text
    
    def get_back_dated_leave(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Back_dated_leave).text

    def get_history_accept_status(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.History_Status).text
    
    def get_approve_reject_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Approve_reject_button)
    
    def get_toast(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.Toast_container).text
        
    def get_details_check_history(self,value):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH,f'/html/body/app-root/div/div/app-leader-leave-management/app-container/div/div[3]/mat-tab-group/div/mat-tab-body[3]/div/div/app-record-manager-grid/div/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[{value}]/div/span').text
    
    def get_clear_filters(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.clear_filters)
    
    def get_header(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.header)
    
    def get_reject_reason_header(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*LeaderLeaveRequests.reason_header)






    
    


    
    

