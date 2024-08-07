from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
class MyProfilePage:
    def __init__(self,driver):
        self.driver=driver
    personal_details_tab=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[1]/div/div/div[5]/ul[1]")
    communication_details_tab=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[1]/div/div/div[5]/ul[2]")
    education_details_tab=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[1]/div/div/div[5]/ul[3]")
    skills_details_tab=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[1]/div/div/div[5]/ul[4]")
    personal_details_edit_button=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div[1]/span[2]")
    id_type_one=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div/span")
    id_type_two=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[4]/div/span")
    update_id_type_one=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/form/div[2]/div/select")
    update_id_type_two=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/form/div[4]/div/select")
    input_id_number_one=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/form/div[3]/div/input")
    input_id_number_two=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/form/div[5]/div/input")
    cancel_personal_details=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/form/div[6]/app-action-button[1]/button")
    update_personal_details=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/form/div[6]/app-action-button[2]/button")
    id_type_one=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div/span")
    id_type_two=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[4]/div/span")

    emergency_contact_name_one=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/span[1]")
    emergency_contact_relationship_one=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/span[2]")
    emergency_contact_number_one=(By.XPATH,"/html/body/app-root/div/div/app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/span[3]")
    emergency_contact_name_two=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div[2]/span[1]") 
    emergency_contact_relationship_two=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div[2]/span[2]")
    emergency_contact_number_two=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div[2]/span[3]")

    emergency_contact_name_update_one=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/form/div[1]/div[2]/div[1]/div[1]/div/input")
    emergency_contact_number_update_one=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/form/div[1]/div[2]/div[1]/div[2]/div/input")
    emergency_contact_relationship_dropdown_one=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/form/div[1]/div[2]/div[1]/div[3]/div/div/select")
    emergency_contact_name_update_two=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/form/div[1]/div[2]/div[2]/div[1]/div/input")
    emergency_contact_number_update_two=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/form/div[1]/div[2]/div[2]/div[2]/div/input")
    emergency_contact_relationship_dropdown_two=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/form/div[1]/div[2]/div[2]/div[3]/div/div/select")

    cancel_communication_details=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/form/div[2]/app-action-button[1]/button")
    update_communication_details=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/form/div[2]/app-action-button[2]/button")
    
    communication_details_edit_button=(By.XPATH,"/html/body/app-root/div/div/app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/span[2]")
    education_details_edit_button=(By.XPATH,"/html/body/app-root/div/div/app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/span[2]")
    addCertification=(By.XPATH,'//span[text()="Add Certification"]')
    addPrimarySkills=(By.XPATH,'//span[text()="Add Primary Skills"]')
    addSecondarySkills=(By.XPATH,'//span[text()="Add Secondary Skills"]')
    skills_edit_button=(By.XPATH,"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/span[2]/img")
    update_skills_button=(By.XPATH,"/html/body/app-root/div/div/app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[3]/app-action-button[2]/button")
    cancel_skills_button=(By.XPATH,"/html/body/app-root/div/div/app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[3]/app-action-button[1]/button")

    def get_new_communication_update(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*MyProfilePage.update_communication_details)

    
    def get_new_emergency_contact_name_one(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.emergency_contact_name_one)
    def get_new_emergency_contact_name_two(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.emergency_contact_name_two)
    def get_new_emergency_contact_relationship_one(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.emergency_contact_relationship_one)
    def get_new_emergency_contact_relationship_two(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.emergency_contact_relationship_two)
    def get_new_emergency_contact_number_one(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.emergency_contact_number_one)
    def get_new_emergency_contact_number_two(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.emergency_contact_number_two)
    
    

    def get_personal_details_tab(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.personal_details_tab)
    def get_communication_details_tab(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.communication_details_tab)
    def get_education_details_tab(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.education_details_tab)
    def get_skills_details_tab(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.skills_details_tab)
    def get_personal_details_edit_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.personal_details_edit_button)
    def get_id_type_one(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.id_type_one)
    def get_id_type_two(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.id_type_two)
    def get_dropdown_id_type_one(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.update_id_type_one)
    def get_dropdown_id_type_two(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.update_id_type_two)
    def send_data_select_id_type_one(self,value):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,f"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/form/div[2]/div/select/option[text()=' {value} ']").click()
    def send_data_select_id_type_two(self,value):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,f"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/form/div[4]/div/select/option[text()=' {value} ']").click()
    def get_input_id_number_one(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.input_id_number_one)
    def get_input_id_number_two(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.input_id_number_two)
    def get_update_personal_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.update_personal_details)
    
    def get_cancel_personal_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.cancel_personal_details)
    
    def get_communication_details_edit_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.communication_details_edit_button)
    
    def get_emergency_contact_name_one_update(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.emergency_contact_name_update_one)
    
    def get_emergency_contact_name_two_update(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.emergency_contact_name_update_two)
    
    def get_emergency_contact_number_one_update(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.emergency_contact_number_update_one)
    
    def get_emergency_contact_number_two_update(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.emergency_contact_number_update_two)
    
    def get_emergency_contact_relationship_one_dropdown_update(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.emergency_contact_relationship_dropdown_one)
    
    def get_emergency_contact_relationship_two_dropdown_update(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.emergency_contact_relationship_dropdown_two)
    
    def get_emergency_relationship_option_select_one(self,val):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH,f"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/form/div[1]/div[2]/div[1]/div[3]/div/div/select/option[text()='{val}']").click()

    def get_emergency_relationship_option_select_two(self,val):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH,f"/html/body/app-root/div/div/app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/form/div[1]/div[2]/div[2]/div[3]/div/div/select/option[text()='{val}']").click()
    
    def get_cancel_education_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.cancel_communication_details)
    
    def get_update_education_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.update_)
    
    def get_education_details_tab_edit_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.education_details_edit_button)
     
    def get_all_certifications(self):
        ls=[]
        for i in range(1,100000):
            try:
                ls.append(self.driver.find_element(By.XPATH,f"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[{i}]/div[1]/div/div/span").text)
                ls.append(self.driver.find_element(By.XPATH,f"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[{i}]/div[2]/div/div/span").text)
            except:
                break
        print("Helloo")
        print(ls)
        return ls
    
    def get_add_new_certificate_name(self,i,val1,val2):
        self.driver.implicitly_wait(10)
        if(val1!=None):
            self.driver.find_element(By.XPATH,f"//html/body/app-root/div/div/app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div/form/div/div[{i//2+2}]/div[1]/div/input").send_keys(val1)
        if(val2!=None):
            self.driver.find_element(By.XPATH,f"//html/body/app-root/div/div/app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div/form/div/div[{i//2+2}]/div[2]/div/input").send_keys(val2)

    def get_add_new_primary_skill(self,i,val1):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,f"/html/body/app-root/div/div/app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div[{i+2}]/div[1]/input").send_keys(val1)
    def get_add_new_secondary_skill(self,i,val1):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,f"/html/body/app-root/div/div/app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[{i+2}]/div[1]/input").send_keys(val1)

    def add_new_certificate(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.addCertification)
    
    def add_new_primary_skill(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.addPrimarySkills)
    
    def add_new_secondary_skill(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.addSecondarySkills)
    
    def get_primary_details_with_ratings(self):
        ls=[]
        for i in range(2,10000):
            try:
                ms=[]
                ms.append(self.driver.find_element(By.XPATH,f"/html/body/app-root/div/div/app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[{i}]/div[1]").text)
                k=1
                while(k<=5):
                    if self.driver.find_element(By.XPATH, f"/html/body/app-root/div/div/app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[{i}]/div[2]/div[{k}]").value_of_css_property("background-color")== "rgb(65, 65, 65)":

                        k+=1
                    else:
                        break
                ms.append(k)
                ls.append(ms)
            except:
                break
        return ls
    
    def get_primary_details(self):
        ls=[]
        for i in range(2,10000):
            try:
                ls.append(self.driver.find_element(By.XPATH,f"/html/body/app-root/div/div/app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[{i}]/div[1]").text)
            except:
                break
        return ls
    def get_secondary_details(self):
        ls=[]
        for i in range(2,100000):
            try:
                ls.append(self.driver.find_element(By.XPATH,f"/html/body/app-root/div/div/app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[{i}]/div[1]").text)
            except:
                break
        return ls

    def get_skills_details_tab_edit_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.skills_edit_button)
    
    def get_cancel_skill_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.cancel_skills_button)
    def get_update_skill_button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*MyProfilePage.update_skills_button)

    def get_delete_primary_skill(self,i):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,f"//app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div[{i+1}]/div[3]/button").click()
    
    def get_delete_secondary_skill(self,i):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,f"/html/body/app-root/div/div/app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[{i+1}]/div[3]/button").click()

    def get_delete_educational(self,i):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,f"/html/body/app-root/div/div/app-my-profile/app-container/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/form/div[1]/div[{i+1}]/div[3]/button").click()


    