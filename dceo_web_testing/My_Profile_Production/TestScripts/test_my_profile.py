from pageObjects.LoginPage import LoginPage
from pageObjects.MyselfPage import MyselfPage
from pageObjects.MyProfileProductionPage import MyProfilePage
from ..TestScripts.BaseClass import BaseClass
from TestData.my_profile_data import my_profile_data
import time
import pytest
class Test_My_Profile(BaseClass):
    
    @pytest.mark.parametrize("idTypeOne, idNumberOne, idTypeTwo, idNumberTwo, emergencyContactNameOne, emergencyContactRelationshipOne, emergencyContactNumberOne, emergencyContactNameTwo, emergencyContactRelationshipTwo, emergencyContactNumberTwo, oldCertifcate, newCertificate, addCertification, addCertificationId, deleteCertification, deleteCertificationId, addPrimarySkill,deletePrimarySkill, addSecondarySkill,deleteSecondarySkill",my_profile_data.get_my_profile_data("test_update_personal_details"))
    def test_update_personal_details(self,idTypeOne, idNumberOne, idTypeTwo, idNumberTwo, emergencyContactNameOne, emergencyContactRelationshipOne, emergencyContactNumberOne, emergencyContactNameTwo, emergencyContactRelationshipTwo, emergencyContactNumberTwo, oldCertifcate, newCertificate, addCertification, addCertificationId, deleteCertification, deleteCertificationId, addPrimarySkill,deletePrimarySkill, addSecondarySkill, deleteSecondarySkill):
        test_file_name="test_my_profile"
        logger=self.getLogger(test_file_name)

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("testing2@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("EE2kkyXyidqHFqXI")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on MySelf")

        myselfPage=MyselfPage(self.driver)
        myselfPage.get_my_profile().click()

        myProfilePage=MyProfilePage(self.driver)

        myProfilePage.get_personal_details_tab().click()
        logger.info("Clicked on the Personal Details Tab")

        myProfilePage.get_personal_details_edit_button().click()
        logger.info("Clicked on the edit Personal Details Button")

        if(idTypeOne!=None):
            myProfilePage.get_dropdown_id_type_one().click()
            logger.info("Clicked on the Dropdown Id One")
            myProfilePage.send_data_select_id_type_one(idTypeOne)
            logger.info("id type one is selected")
        
        if(idNumberOne!=None):
           myProfilePage.get_input_id_number_one().clear()
           myProfilePage.get_input_id_number_one().send_keys(idNumberOne)
           logger.info("id number one is entered")
           
        if(idTypeTwo!=None):
            myProfilePage.get_dropdown_id_type_two().click()
            logger.info("Clicked on the Dropdown Id Two")
            myProfilePage.send_data_select_id_type_two(idTypeTwo)
            logger.info("Clicked on dropdown id type two")
        
        if(idNumberTwo!=None):
            myProfilePage.get_input_id_number_two().clear()
            myProfilePage.get_input_id_number_two().send_keys(idNumberTwo)
            logger.info("id number two is entered")

        myProfilePage.get_update_personal_button().click()
        logger.info("Clicked on the update button")
        time.sleep(5)

        flag=True
        if(idTypeOne!=None and (str(idTypeOne) not in myProfilePage.get_id_type_one().text)):
            flag=False
            logger.info("Id of Type one is not updated")
            assert False
            return
        if(idTypeTwo!=None and (str(idTypeTwo) not in myProfilePage.get_id_type_two().text)):
            flag=False
            logger.info("Id of Type Two is not updated")
            assert False
            return
        if(idNumberOne!=None and (str(idNumberOne) not in myProfilePage.get_id_type_one().text)):
            flag=False
            logger.info("Id of name one is not updated")
            assert False
            return
        if(idNumberTwo!=None and (str(idNumberTwo) not in myProfilePage.get_id_type_two().text)):
            flag=False
            logger.info("Id of name two is not updated")
            assert False
            return
        assert flag

    
    @pytest.mark.comm
    @pytest.mark.parametrize("idTypeOne, idNumberOne, idTypeTwo, idNumberTwo, emergencyContactNameOne, emergencyContactRelationshipOne, emergencyContactNumberOne, emergencyContactNameTwo, emergencyContactRelationshipTwo, emergencyContactNumberTwo, oldCertificate, newCertificate, addCertification, addCertificationId, deleteCertification, deleteCertificationId, addPrimarySkill,deletePrimarySkill, addSecondarySkill, deleteSecondarySkill",my_profile_data.get_my_profile_data("test_update_communication_details"))
    def test_update_communication_details(self,idTypeOne, idNumberOne, idTypeTwo, idNumberTwo, emergencyContactNameOne, emergencyContactRelationshipOne, emergencyContactNumberOne, emergencyContactNameTwo, emergencyContactRelationshipTwo, emergencyContactNumberTwo, oldCertificate, newCertificate, addCertification, addCertificationId, deleteCertification, deleteCertificationId, addPrimarySkill, deletePrimarySkill, addSecondarySkill,deleteSecondarySkill):
        test_file_name="test_my_profile"
        logger=self.getLogger(test_file_name)

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("testing2@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("EE2kkyXyidqHFqXI")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on MySelf")

        myselfPage=MyselfPage(self.driver)
        myselfPage.get_my_profile().click()
        logger.info("Clicked on My Profile")

        myProfilePage=MyProfilePage(self.driver)
        
        myProfilePage.get_communication_details_tab().click()
        logger.info("Clicked on the Communication details tab")

        myProfilePage.get_communication_details_edit_button().click()
        logger.info("Clicked on the edit communication details")

        if(emergencyContactNameOne!=None):
            myProfilePage.get_emergency_contact_name_one_update().clear()
            myProfilePage.get_emergency_contact_name_one_update().send_keys(emergencyContactNameOne)
        if(emergencyContactNumberOne!=None):
            myProfilePage.get_emergency_contact_number_one_update().clear()
            time.sleep(3)
            myProfilePage.get_emergency_contact_number_one_update().send_keys(emergencyContactNumberOne)
        if(emergencyContactRelationshipOne!=None):
            myProfilePage.get_emergency_contact_relationship_one_dropdown_update().click()
            myProfilePage.get_emergency_relationship_option_select_one(emergencyContactRelationshipOne)
        
        if(emergencyContactNameTwo!=None):
            myProfilePage.get_emergency_contact_name_two_update().clear()
            myProfilePage.get_emergency_contact_name_two_update().send_keys(emergencyContactNameOne)
        if(emergencyContactNumberTwo!=None):
            myProfilePage.get_emergency_contact_number_two_update().clear()
            myProfilePage.get_emergency_contact_number_two_update().send_keys(emergencyContactNumberTwo)
        if(emergencyContactRelationshipTwo!=None):
            myProfilePage.get_emergency_contact_relationship_two_dropdown_update().click()
            myProfilePage.get_emergency_relationship_option_select_two(emergencyContactRelationshipOne)
            
        myProfilePage.get_new_communication_update().click()
        time.sleep(5)
        flag=True
        if(emergencyContactNameOne!=None and (str(emergencyContactNameOne) not in myProfilePage.get_new_emergency_contact_name_one().text)):
            flag=False
            logger.info("Emergency Contact Name One is not updated")
            logger.info(myProfilePage.get_new_emergency_contact_name_one().text)
            assert False
            return
        if(emergencyContactNameTwo!=None and (str(emergencyContactNameTwo) not in myProfilePage.get_new_emergency_contact_name_two().text)):
            flag=False
            logger.info("Emergency Contact Name two is not updated")
            assert False
            return
        if(emergencyContactRelationshipTwo!=None and (str(emergencyContactRelationshipTwo) not in myProfilePage.get_new_emergency_contact_relationship_two().text)):
            flag=False
            f=myProfilePage.get_new_emergency_contact_relationship_two().text
            logger.info("Emergency Relationship Two is not updated")
            logger.info(f)
            assert False
            return
        if(emergencyContactRelationshipOne!=None and (str(emergencyContactRelationshipOne) not in myProfilePage.get_new_emergency_contact_relationship_one().text)):
            flag=False
            f=myProfilePage.get_new_emergency_contact_relationship_two().text
            logger.info("Emergency Relationship One is not updated")
            logger.info(f)
            assert False
            return
        if(emergencyContactNumberOne!=None and (str(emergencyContactNumberOne) not in myProfilePage.get_new_emergency_contact_number_one().text)):
            flag=False
            logger.info("Emergency Contact number One is not updated")
            logger.info(emergencyContactNumberOne)
            logger.info(myProfilePage.get_new_emergency_contact_number_one().text)
            assert False
            return
        if(emergencyContactNumberTwo!=None and (str(emergencyContactNumberTwo) not in myProfilePage.get_new_emergency_contact_number_two().text)):
            flag=False
            logger.info("Emergency Contact number Two is not updated")
            assert False
            return
        assert flag
        
        time.sleep(2)

    
    @pytest.mark.parametrize("idTypeOne, idNumberOne, idTypeTwo, idNumberTwo, emergencyContactNameOne, emergencyContactRelationshipOne, emergencyContactNumberOne, emergencyContactNameTwo, emergencyContactRelationshipTwo, emergencyContactNumberTwo, oldCertifcate, newCertificate, addCertification, addCertificationId, deleteCertification, deleteCertificationId, addPrimarySkill,deletePrimarySkill, addSecondarySkill, deleteSecondarySkill",my_profile_data.get_my_profile_data("test_add_educational_details"))
    def test_add_educational_details(self,idTypeOne, idNumberOne, idTypeTwo, idNumberTwo, emergencyContactNameOne, emergencyContactRelationshipOne, emergencyContactNumberOne, emergencyContactNameTwo, emergencyContactRelationshipTwo, emergencyContactNumberTwo, oldCertifcate, newCertificate, addCertification, addCertificationId, deleteCertification, deleteCertificationId, addPrimarySkill, deletePrimarySkill, addSecondarySkill,deleteSecondarySkill):
        test_file_name="test_my_profile"
        logger=self.getLogger(test_file_name)

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("testing2@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("EE2kkyXyidqHFqXI")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on MySelf")

        myselfPage=MyselfPage(self.driver)
        myselfPage.get_my_profile().click()
        logger.info("Clicked on My Profile")

        myProfilePage=MyProfilePage(self.driver)
        myProfilePage.get_education_details_tab().click()

        allCertificates=myProfilePage.get_all_certifications()
        n=len(allCertificates)
        myProfilePage.get_education_details_tab_edit_button().click()
        myProfilePage.add_new_certificate().click()
        myProfilePage.get_add_new_certificate_name(n,addCertification,addCertificationId)
        myProfilePage.get_update_education_button().click()
        newAllCertificates=myProfilePage.get_all_certifications()
        if((addCertification in newAllCertificates[-2]) or (addCertificationId in newAllCertificates[-1])):
            assert True
        else:
            logger.info("Certificates are not added")
            assert False
    
    
    @pytest.mark.parametrize("idTypeOne, idNumberOne, idTypeTwo, idNumberTwo, emergencyContactNameOne, emergencyContactRelationshipOne, emergencyContactNumberOne, emergencyContactNameTwo, emergencyContactRelationshipTwo, emergencyContactNumberTwo, oldCertifcate, newCertificate, addCertification, addCertificationId, deleteCertification, deleteCertificationId, addPrimarySkill, deletePrimarySkill, addSecondarySkill, deleteSecondarySkill",my_profile_data.get_my_profile_data("test_delete_educational_details"))
    def test_delete_educational_details(self,idTypeOne, idNumberOne, idTypeTwo, idNumberTwo, emergencyContactNameOne, emergencyContactRelationshipOne, emergencyContactNumberOne, emergencyContactNameTwo, emergencyContactRelationshipTwo, emergencyContactNumberTwo, oldCertifcate, newCertificate, addCertification, addCertificationId, deleteCertification, deleteCertificationId, addPrimarySkill, deletePrimarySkill, addSecondarySkill, deleteSecondarySkill):

        test_file_name="test_my_profile"
        logger=self.getLogger(test_file_name)

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("testing2@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("EE2kkyXyidqHFqXI")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on MySelf")

        myselfPage=MyselfPage(self.driver)
        myselfPage.get_my_profile().click()
        logger.info("Clicked on My Profile")

        myProfilePage=MyProfilePage(self.driver)
        myProfilePage.get_education_details_tab().click()

        allCertificates=myProfilePage.get_all_certifications()
        n=len(allCertificates)
        myProfilePage.get_education_details_tab_edit_button().click()
        i=1
        hm={}
        k=0
        while(k<n):
            hm[i]=[allCertificates[k],allCertificates[k+1]]
            i+=1
            k=k+2
        for m in hm:
            ll=hm[m]
            if((deleteCertification in ll[0]) and (deleteCertificationId in ll[1])):
                myProfilePage.get_delete_educational(m)
        
        myProfilePage.get_update_education_button().click()
        allCertificates=myProfilePage.get_all_certifications()
        m=len(allCertificates)
        if(m==n-2):
            assert True
            return
        assert False

    @pytest.mark.sss
    @pytest.mark.parametrize("idTypeOne, idNumberOne, idTypeTwo, idNumberTwo, emergencyContactNameOne, emergencyContactRelationshipOne, emergencyContactNumberOne, emergencyContactNameTwo, emergencyContactRelationshipTwo, emergencyContactNumberTwo, oldCertifcate, newCertificate, addCertification, addCertificationId, deleteCertification, deleteCertificationId, addPrimarySkill, deletePrimarySkill, addSecondarySkill, deleteSecondarySkill",my_profile_data.get_my_profile_data("test_add_primary_skill"))
    def test_add_primary_skill(self,idTypeOne, idNumberOne, idTypeTwo, idNumberTwo, emergencyContactNameOne, emergencyContactRelationshipOne, emergencyContactNumberOne, emergencyContactNameTwo, emergencyContactRelationshipTwo, emergencyContactNumberTwo, oldCertifcate, newCertificate, addCertification, addCertificationId, deleteCertification, deleteCertificationId, addPrimarySkill, deletePrimarySkill, addSecondarySkill, deleteSecondarySkill):
        test_file_name="test_my_profile"
        logger=self.getLogger(test_file_name)

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("testing2@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("EE2kkyXyidqHFqXI")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on MySelf")

        myselfPage=MyselfPage(self.driver)
        myselfPage.get_my_profile().click()
        logger.info("Clicked on My Profile")

        myProfilePage=MyProfilePage(self.driver)

        myProfilePage.get_skills_details_tab().click()

        primary_skills=myProfilePage.get_primary_details()
        n=len(primary_skills)

        myProfilePage.get_skills_details_tab_edit_button().click()
        myProfilePage.add_new_primary_skill().click()

        myProfilePage.get_add_new_primary_skill(n,addPrimarySkill)

        myProfilePage.get_update_skill_button().click()
        if(addPrimarySkill in myProfilePage.get_primary_details()):
            assert True
            return
        assert False


    @pytest.mark.ssss
    @pytest.mark.parametrize("idTypeOne, idNumberOne, idTypeTwo, idNumberTwo, emergencyContactNameOne, emergencyContactRelationshipOne, emergencyContactNumberOne, emergencyContactNameTwo, emergencyContactRelationshipTwo, emergencyContactNumberTwo, oldCertifcate, newCertificate, addCertification, addCertificationId, deleteCertification, deleteCertificationId, addPrimarySkill, deletePrimarySkill, addSecondarySkill, deleteSecondarySkill",my_profile_data.get_my_profile_data("test_add_secondary_skill")) 
    def test_add_secondary_skill(self,idTypeOne, idNumberOne, idTypeTwo, idNumberTwo, emergencyContactNameOne, emergencyContactRelationshipOne, emergencyContactNumberOne, emergencyContactNameTwo, emergencyContactRelationshipTwo, emergencyContactNumberTwo, oldCertifcate, newCertificate, addCertification, addCertificationId, deleteCertification, deleteCertificationId, addPrimarySkill, deletePrimarySkill, addSecondarySkill, deleteSecondarySkill):
        test_file_name="test_my_profile"
        logger=self.getLogger(test_file_name)

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("testing2@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("EE2kkyXyidqHFqXI")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on MySelf")

        myselfPage=MyselfPage(self.driver)
        myselfPage.get_my_profile().click()
        logger.info("Clicked on My Profile")

        myProfilePage=MyProfilePage(self.driver)

        myProfilePage.get_skills_details_tab().click()

        secondary_skills=myProfilePage.get_secondary_details()
        n=len(secondary_skills)

        myProfilePage.get_skills_details_tab_edit_button().click()
        myProfilePage.add_new_secondary_skill().click()

        myProfilePage.get_add_new_secondary_skill(n,addSecondarySkill)
        time.sleep(5)
        myProfilePage.get_update_skill_button().click()
        
        if(addSecondarySkill in myProfilePage.get_secondary_details()):
            assert True
            return
        assert False

    @pytest.mark.dele
    @pytest.mark.parametrize("idTypeOne, idNumberOne, idTypeTwo, idNumberTwo, emergencyContactNameOne, emergencyContactRelationshipOne, emergencyContactNumberOne, emergencyContactNameTwo, emergencyContactRelationshipTwo, emergencyContactNumberTwo, oldCertifcate, newCertificate, addCertification, addCertificationId, deleteCertification, deleteCertificationId, addPrimarySkill, deletePrimarySkill, addSecondarySkill, deleteSecondarySkill",my_profile_data.get_my_profile_data("test_delete_primary_skill")) 
    def test_delete_primary_skill(self,idTypeOne, idNumberOne, idTypeTwo, idNumberTwo, emergencyContactNameOne, emergencyContactRelationshipOne, emergencyContactNumberOne, emergencyContactNameTwo, emergencyContactRelationshipTwo, emergencyContactNumberTwo, oldCertifcate, newCertificate, addCertification, addCertificationId, deleteCertification, deleteCertificationId, addPrimarySkill, deletePrimarySkill, addSecondarySkill, deleteSecondarySkill):
        test_file_name="test_my_profile"
        logger=self.getLogger(test_file_name)

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("testing2@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("EE2kkyXyidqHFqXI")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on MySelf")

        myselfPage=MyselfPage(self.driver)
        myselfPage.get_my_profile().click()
        logger.info("Clicked on My Profile")

        myProfilePage=MyProfilePage(self.driver)
        
        myProfilePage.get_skills_details_tab().click()

        primary_skills=myProfilePage.get_primary_details()
        index_of_element = primary_skills.index(deletePrimarySkill)

        myProfilePage.get_skills_details_tab_edit_button().click()
        
        myProfilePage.get_delete_primary_skill(index_of_element+1)

        myProfilePage.get_update_skill_button().click()

        if(deletePrimarySkill not in myProfilePage.get_primary_details()):
            assert True
            return
        assert False
    
    @pytest.mark.delee
    @pytest.mark.parametrize("idTypeOne, idNumberOne, idTypeTwo, idNumberTwo, emergencyContactNameOne, emergencyContactRelationshipOne, emergencyContactNumberOne, emergencyContactNameTwo, emergencyContactRelationshipTwo, emergencyContactNumberTwo, oldCertifcate, newCertificate, addCertification, addCertificationId, deleteCertification, deleteCertificationId, addPrimarySkill, deletePrimarySkill, addSecondarySkill, deleteSecondarySkill",my_profile_data.get_my_profile_data("test_delete_secondary_skill")) 
    def test_delete_secondary_skill(self,idTypeOne, idNumberOne, idTypeTwo, idNumberTwo, emergencyContactNameOne, emergencyContactRelationshipOne, emergencyContactNumberOne, emergencyContactNameTwo, emergencyContactRelationshipTwo, emergencyContactNumberTwo, oldCertifcate, newCertificate, addCertification, addCertificationId, deleteCertification, deleteCertificationId, addPrimarySkill, deletePrimarySkill, addSecondarySkill, deleteSecondarySkill):
        test_file_name="test_my_profile"
        logger=self.getLogger(test_file_name)

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("testing2@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("EE2kkyXyidqHFqXI")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on MySelf")

        myselfPage=MyselfPage(self.driver)
        myselfPage.get_my_profile().click()
        logger.info("Clicked on My Profile")

        myProfilePage=MyProfilePage(self.driver)
        
        myProfilePage.get_skills_details_tab().click()

        secondary_skills=myProfilePage.get_secondary_details()
        index_of_element = secondary_skills.index(deleteSecondarySkill)

        myProfilePage.get_skills_details_tab_edit_button().click()
        
        myProfilePage.get_delete_secondary_skill(index_of_element+1)

        myProfilePage.get_update_skill_button().click()

        if(deleteSecondarySkill not in myProfilePage.get_secondary_details()):
            assert True
            return
        assert False
        

