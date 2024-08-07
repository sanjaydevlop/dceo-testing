from selenium.webdriver.common.by import By

class MyOrganizationPage:
    BusinessPresentation=(By.C,'//app-my-organisation/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Business Presentation"]]/div[1]/div/div/div/img[1]')
    CarnivalsDemonstartion=(By.XPATH,'//app-my-organisation/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Carnivals Demonstration"]]/div[1]/div/div/div/img[1]')
    CustomerReferral=(By.XPATH,'//app-my-organisation/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Customer Referral"]]/div[1]/div/div/div/img[1]')
    FacilitiesManagment=(By.XPATH,'//app-my-organisation/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Facilities Management"]]/div[1]/div/div/div/img[1]')
    FormsAndTemplates=(By.XPATH,'//app-my-organisation/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Forms and Templates"]]/div[1]/div/div/div/img[1]')
    IPmanagement=(By.XPATH,'//app-my-organisation/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="IP Management"]]/div[1]/div/div/div/img[1]')
    IdeaHub=(By.XPATH,'//app-my-organisation/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Idea Hub"]]/div[1]/div/div/div/img[1]')
    InternalJobPosting=(By.XPATH,'//app-my-organisation/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Internal Job Posting"]]/div[1]/div/div/div/img[1]')
    LeaderDirectory=(By.XPATH,'//app-my-organisation/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Leader Directory"]]/div[1]/div/div/div/img[1]')
    ListofHolidays=(By.XPATH,'//app-my-organisation/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="List of Holidays"]]/div[1]/div/div/div/img[1]')
    MeasuresDashboard=(By.XPATH,'//app-my-organisation/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Measures Dashboard"]]/div[1]/div/div/div/img[1]')
    ModuleDemonstrations=(By.XPATH,'//app-my-organisation/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Module Demonstrations"]]/div[1]/div/div/div/img[1]')
    NewsLetter=(By.XPATH,'//app-my-organisation/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Newsletter"]]/div[1]/div/div/div/img[1]')
    Organizational_chart=(By.XPATH,'//app-my-organisation/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Organizational Chart"]]/div[1]/div/div/div/img[1]')
    Organizational_guides=(By.XPATH,'//app-my-organisation/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Organizational Guides"]]/div[1]/div/div/div/img[1]')
    Policies_and_Procedures=(By.XPATH,'//app-my-organisation/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Policies and Procedures"]]/div[1]/div/div/div/img[1]')
    Refer_a_leader=(By.XPATH,'//app-my-organisation/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Refer a Leader"]]/div[1]/div/div/div/img[1]')
    Self_Declaration=(By.XPATH,'//app-my-organisation/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Self-Declaration"]]/div[1]/div/div/div/img[1]')
    dCEOresources=(By.XPATH,'//app-my-organisation/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="dCEO Resources"]]/div[1]/div/div/div/img[1]')

    def __init__(self,driver):
        self.driver=driver

    def get_business_presentation(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyOrganizationPage.BusinessPresentation)
    
    def get_carnivals_demonstration(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyOrganizationPage.CarnivalsDemonstartion)
    
    def get_customer_referral(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyOrganizationPage.CustomerReferral)
    
    def get_facilities_management(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyOrganizationPage.FacilitiesManagment)

    def get_forms_and_templates(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyOrganizationPage.FormsAndTemplates)
    
    def get_ip_management(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyOrganizationPage.IPmanagement)
    
    def get_idea_hub(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyOrganizationPage.IdeaHub)
    
    def get_internal_job_posting(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyOrganizationPage.InternalJobPosting)
    
    def get_leader_directory(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyOrganizationPage.LeaderDirectory)

    def get_list_of_holidays(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyOrganizationPage.ListofHolidays)
    
    def get_measures_dashboard(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyOrganizationPage.MeasuresDashboard)
    
    def get_module_demonstrations(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyOrganizationPage.ModuleDemonstrations)
    
    def get_newsletter(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyOrganizationPage.NewsLetter)
    
    def get_organizational_chart(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyOrganizationPage.Organizational_chart)
    
    def get_organizational_guides(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyOrganizationPage.Organizational_guides)
    
    def get_policies_and_procedures(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyOrganizationPage.Policies_and_Procedures)
    
    def get_refer_a_leader(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyOrganizationPage.Refer_a_leader)
    
    def get_self_declaration(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyOrganizationPage.Self_Declaration)
    
    def get_dceo_resources(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyOrganizationPage.dCEOresources)