from selenium.webdriver.common.by import By

class MyModulesPage:
    
    Module_stack=(By.XPATH,'//app-my-work-modules/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="Module Stack"]]/div[1]/div/div/div/img[1]')
    MyObjectives=(By.XPATH,'//app-my-work-modules/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="MyObjectives"]]/div[1]/div/div/div/img[1]')
    MyTeam=(By.XPATH,'//app-my-work-modules/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="MyTeam"]]/div[1]/div/div/div/img[1]')
    MyWorkModules=(By.XPATH,'//app-my-work-modules/app-container/div/app-dashboard-card/div/div/div[div[2]/h3[text()="MyWork Modules"]]/div[1]/div/div/div/img[1]')

    def __init__(self, driver):
        self.driver = driver

    def get_module_stack(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyModulesPage.Module_stack)
    
    def get_my_objectives(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyModulesPage.MyObjectives)
    
    def get_my_team(self):
        self.driver.implictly_wait(10)
        return self.driver.find_element(*MyModulesPage.MyTeam)
    
    def get_my_work_modules(self):
        self.driver.implictly_wait(10)
        return self.driver.find_element(*MyModulesPage.MyWorkModules)
    