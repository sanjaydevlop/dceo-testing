from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time

class CustomerReferral:
    def __init__(self, driver):
        self.driver = driver
    my_referrals_button=(By.XPATH,"//app-action-button[2]/button/span[text()=' My Referrals ']")
    id_search=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[1]/app-text-floating-filter/input")
    contact_Name_Input=(By.XPATH,'//input[@placeholder="Enter Contact\'s Name"]')
    email_Input=(By.XPATH,"//input[@placeholder='Enter Email ID']")
    phone_Number_Input=(By.XPATH,"//input[@placeholder='Enter Phone Number']")
    designation_Input=(By.XPATH,"//input[@placeholder='Enter Designation']")
    company_Name_Input=(By.XPATH,"//input[@placeholder='Enter Company Name']")
    select_reason_company_location=(By.XPATH,"//ng-select/div/div[div[text()='Select Company Location (City)']]/div/input")
    select_reason_company_size=(By.XPATH,"//ng-select/div/div[div[text()='Select Company Size']]/div/input")
    select_reason_company_sector=(By.XPATH,"//ng-select/div/div[div[text()='Select Company Sector']]/div/input")
    company_revenue_Input=(By.XPATH,"//input[@placeholder='Enter Company Revenue']")
    company_revenue_potential=(By.XPATH,"//input[@placeholder='Enter Revenue Potential']")
    select_relationship_referee=(By.XPATH,"//ng-select/div/div[div[text()='Select Relationship with the Referee']]/div/input")
    select_option_yes_no=(By.XPATH,"//ng-select/div/div[div[text()='Select an option']]/div/input")
    select_mode_of_communication=(By.XPATH,"//ng-select/div/div[div[text()='Select Mode of Communication']]/div/input")
    select_interest_level=(By.XPATH,"//ng-select/div/div[div[text()='Select Interest level']]/div/input")   
    relationship_with_referee_input=(By.XPATH,"//input[@placeholder='Enter the relation with referee (if family or relative)']")
    points_text_area_input=(By.XPATH,"//textarea[@placeholder='Enter the points']")
    file=(By.XPATH,"//input[@id='file']")
    refer_button=(By.XPATH,"//app-action-button/button/span[contains(text(),' Refer ')]")
    refer_successful=(By.XPATH,"//app-referral-successful/div[1]")
    refer_successful_name=(By.XPATH,"//app-referral-successful/div[2]/table/tr[1]/td[2]")
    refer_successful_mobile=(By.XPATH,"//app-referral-successful/div[2]/table/tr[2]/td[2]")
    refer_successful_email=(By.XPATH,"//app-referral-successful/div[2]/table/tr[3]/td[2]")
    ag_grid_elements=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div")
    def __init__(self,driver):
        self.driver=driver
    def get_contact_name(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.contact_Name_Input)
    
    def get_email(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.email_Input)
    
    def get_phone_number(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.phone_Number_Input)
    
    def get_designation(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.designation_Input)
    
    def get_company_name(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.company_Name_Input)
    
    def get_select_reason_company_location(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.select_reason_company_location)
    
    def get_select_reason_company_size(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.select_reason_company_size)
    
    def get_select_reason_company_sector(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.select_reason_company_sector)
    
    def get_company_revenue(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.company_revenue_Input)
    
    def get_company_revenue_potential(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.company_revenue_potential)
    
    def get_select_relationship_referee(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.select_relationship_referee)
    
    def get_select_option_yes_no(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.select_option_yes_no)
    
    def get_select_mode_of_communication(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.select_mode_of_communication)
    
    def get_select_interest_level(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.select_interest_level)
    
    def get_relationship_with_referee(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.relationship_with_referee_input)
    
    def get_points(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.points_text_area_input)
    
    def get_file(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.file)
    
    def get_refer(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.refer_button)

    def select_value_dropdown(self,value):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH,f"//ng-dropdown-panel/div/div/div/span[text()='{value}']")

    def select_value_dropdown_not_present(self,value):
        self.driver.implicitly_wait(10)
        newVal='"'+value+'"'
        return self.driver.find_element(By.XPATH,f"//ng-dropdown-panel/div/div/div/span[span[text()='Add item']][text()='{newVal}']")

    def refer_successful_component(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.refer_successful)
    
    def validate_name_success(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.refer_successful_name)
    def validate_mobile_success(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.refer_successful_mobile)
    def validate_email_success(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.refer_successful_email)

    def get_my_referral_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.my_referrals_button)
    
    def get_id_search(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*CustomerReferral.id_search)

    def get_ag_grid_elements(self):
        self.driver.implicitly_wait(10)
        print(self.driver.find_elements(*CustomerReferral.ag_grid_elements))
        print(len(self.driver.find_elements(*CustomerReferral.ag_grid_elements)))
        return len(self.driver.find_elements(*CustomerReferral.ag_grid_elements))
    

    