from selenium.webdriver.common.by import By

class RaiseaRequest:
    request_history = (By.XPATH,'/html/body/app-root/div/div/app-os-ticket-creation/div/app-container/div/div[3]/div/div[2]/form/div/div[1]/div[2]/app-action-button/button')
    search_request = (By.XPATH,'/html/body/app-root/div/div/app-os-ticket-creation/div/app-container/div/div[3]/div/div[2]/form/div/div[1]/div[1]/app-reusable-select/div/ng-select')
    category = (By.XPATH,'/html/body/app-root/div/div/app-os-ticket-creation/div/app-container/div/div[3]/div/div[2]/form/div/div[1]/div[1]/div[1]/div[1]/app-reusable-select/div/ng-select')
    sub_category = (By.XPATH,'/html/body/app-root/div/div/app-os-ticket-creation/div/app-container/div/div[3]/div/div[2]/form/div/div[1]/div[1]/div[1]/div[2]/app-reusable-select/div/ng-select')
    priority = (By.XPATH,'/html/body/app-root/div/div/app-os-ticket-creation/div/app-container/div/div[3]/div/div[2]/form/div/div[1]/div[1]/div[1]/div[3]/app-reusable-select/div/ng-select')
    location = (By.XPATH,'/html/body/app-root/div/div/app-os-ticket-creation/div/app-container/div/div[3]/div/div[2]/form/div/div[1]/div[1]/div[2]/div[1]/app-reusable-select/div/ng-select')
    office = (By.XPATH,'/html/body/app-root/div/div/app-os-ticket-creation/div/app-container/div/div[3]/div/div[2]/form/div/div[1]/div[1]/div[2]/div[2]/app-reusable-select/div/ng-select')
    desk_id=(By.XPATH,'/html/body/app-root/div/div/app-os-ticket-creation/div/app-container/div/div[3]/div/div[2]/form/div/div[1]/div[1]/div[2]/div[3]/app-reusable-input/div/input')
    request_summary = (By.XPATH,'/html/body/app-root/div/div/app-os-ticket-creation/div/app-container/div/div[3]/div/div[2]/form/div/div[2]/app-reusable-textarea/div/textarea')
    request_description = (By.XPATH,'/html/body/app-root/div/div/app-os-ticket-creation/div/app-container/div/div[3]/div/div[2]/form/div/div[3]/app-reusable-textarea/div/textarea')
    upload_file = (By.XPATH,'/html/body/app-root/div/div/app-os-ticket-creation/div/app-container/div/div[3]/div/div[2]/form/div/div[4]/div/input')
    submit = (By.XPATH,'/html/body/app-root/div/div/app-os-ticket-creation/div/app-container/div/div[3]/div/div[2]/form/div/div[5]/app-action-button/button')
    # request_type_service = (By.XPATH,f'/html/body/app-root/div/div/app-os-ticket-creation/div/app-container/div/div[3]/div/div[1]/div/button[1]')
    # request_type_goods = (By.XPATH,'/html/body/app-root/div/div/app-os-ticket-creation/div/app-container/div/div[3]/div/div[1]/div/button[2]')
    # request_type_payments = (By.XPATH,'/html/body/app-root/div/div/app-os-ticket-creation/div/app-container/div/div[3]/div/div[1]/div/button[3]')
    unselect_search = (By.XPATH,'/html/body/app-root/div/div/app-os-ticket-creation/div/app-container/div/div[3]/div/div[2]/form/div/div[1]/div[1]/app-reusable-select/div/ng-select/div/span[1]')
    no_items_subcategory = (By.XPATH,'/html/body/ng-dropdown-panel/div/div[2]/div')
    
    def __init__(self,driver):
        self.driver=driver

    def get_request_history(self):
        self.driver.implictly_wait(10)
        return self.driver.find_element(*RaiseaRequest.request_history)
   
    def get_service(self):
        self.driver.implictly_wait(10)
        return self.driver.find_element(*RaiseaRequest.request_type_service)
    
    def get_goods(self):
        self.driver.implictly_wait(10)
        return self.driver.find_element(*RaiseaRequest.request_type_goods)
    
    def get_service(self):
        self.driver.implictly_wait(10)
        return self.driver.find_element(*RaiseaRequest.request_type_payments)
    
    def get_search_request(self):
        self.driver.implictly_wait(10)
        return self.driver.find_element(*RaiseaRequest.search_request)
    
    def select_reason_for_search(self,reason):
        self.driver.implictly_wait(10)
        return self.driver.find_element(By.XPATH,f'//ng-dropdown-panel/div/div/div/span[text()="{reason}"]')
    
    def get_unselect_search(self):
        self.driver.implictly_wait(10)
        return self.driver.find_element(*RaiseaRequest.unselect_search)
    
    def get_category(self):
        self.driver.implictly_wait(10)
        return self.driver.find_element(*RaiseaRequest.category)
    
    def select_reason_for_category(self,reason):
        self.driver.implictly_wait(10)
        return self.driver.find_element(By.XPATH,f'//ng-dropdown-panel/div/div/div/span[text()="{reason}"]')
    
    def get_sub_category(self):
        self.driver.implictly_wait(10)
        return self.driver.find_element(*RaiseaRequest.sub_category)
    
    def select_reason_for_sub_category(self,reason):
        self.driver.implictly_wait(10)
        return self.driver.find_element(By.XPATH,f'//ng-dropdown-panel/div/div/div/span[text()="{reason}"]')
    
    def get_priority(self):
        self.driver.implictly_wait(10)
        return self.driver.find_element(*RaiseaRequest.priority)
    
    def select_priority(self,priority):
        self.driver.implictly_wait(10)
        return self.driver.find_element(By.XPATH,f'//ng-dropdown-panel/div/div/div/span[text()="{priority}"]')
    
    def get_location(self):
        self.driver.implictly_wait(10)
        return self.driver.find_element(*RaiseaRequest.location)
    
    def select_location(self,location):
        self.driver.implictly_wait(10)
        return self.driver.find_element(By.XPATH,f'//ng-dropdown-panel/div/div/div/span[text()="{location}"]')
    
    def get_office(self):
        self.driver.implictly_wait(10)
        return self.driver.find_element(*RaiseaRequest.office)
    
    def select_office(self,office):
        self.driver.implictly_wait(10)
        return self.driver.find_element(By.XPATH,f'//ng-dropdown-panel/div/div/div/span[text()="{office}"]')
    
    def get_desk_id(self):
        self.driver.implictly_wait(10)
        return self.driver.find_element(*RaiseaRequest.desk_id)
    
    def select_desk_id(self,desk_id):
        self.driver.implictly_wait(10)
        return self.driver.find_element(By.XPATH,f'//ng-dropdown-panel/div/div/div/span[text()="{desk_id}"]')
    
    def get_request_summary(self):
        self.driver.implictly_wait(10)
        return self.driver.find_element(*RaiseaRequest.request_summary)
    
    def get_request_description(self):
        self.driver.implictly_wait(10)
        return self.driver.find_element(*RaiseaRequest.request_description)

    def get_upload_file(self):
        self.driver.implictly_wait(10)
        return self.driver.find_element(*RaiseaRequest.upload_file)
    
    def get_submit(self):
        self.driver.implictly_wait(10)
        return self.driver.find_element(*RaiseaRequest.submit)
    
    def get_request_type(self,requestType):
        self.driver.implicitly_wait(10)
        request_type_dictionary = {"Service":1,"Goods":2,"Payments":3}
        value = request_type_dictionary.get(requestType)
        return self.driver.find_element(By.XPATH,f'//app-os-ticket-creation/div/app-container/div/div[3]/div/div[1]/div/button[{value}]')
    
    def get_subcategory_no_items(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*RaiseaRequest.no_items_subcategory).text
    

    