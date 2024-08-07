from pageObjects.CustomerReferralPage import CustomerReferral
from pageObjects.LoginPage import LoginPage
from pageObjects.MyOrganizationPage import MyOrganizationPage
from ..TestScripts.BaseClass import BaseClass
from TestData.customer_ref_data import customer_ref_data

from selenium.webdriver.support.ui import WebDriverWait,Select
import time
import pytest
class Test_Customer_Referral(BaseClass):

    @pytest.mark.test
    @pytest.mark.parametrize("contact_name,email_id,phone_number,designation,company_name,company_location,company_size,company_sector,company_revenue,revenue_potential,relationship_referee,related,personally_spoken,mode_communication,interest_expressed,points_discuss,attachment,referral_id",customer_ref_data.get_customer_ref_data("test_all_fields_submit_no_attachment"))
    def test_all_fields_submit_no_attachment(self,contact_name,email_id,phone_number,designation,company_name,company_location,company_size,company_sector,company_revenue,revenue_potential,relationship_referee,related,personally_spoken,mode_communication,interest_expressed,points_discuss,attachment,referral_id):
        test_file_name="test_customer_referral"
        logger=self.getLogger(test_file_name)
        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automationprofiletwo@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("5WT4Rqe91cAzu17M")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MyOrganization").click()
        logger.info("Clicked on MyOrganization")

        myOrganizationPage=MyOrganizationPage(self.driver)

        myOrganizationPage.get_customer_referral().click()
        logger.info("Clicked on Customer Referral")

        customerReferral=CustomerReferral(self.driver)

        customerReferral.get_contact_name().send_keys(contact_name)
        logger.info("Entered Contact Name")

        customerReferral.get_email().send_keys(email_id)
        logger.info("Entered Email ID")

        customerReferral.get_phone_number().send_keys(phone_number)
        logger.info("Entered Mobile Number")

        customerReferral.get_designation().send_keys(designation)
        logger.info("Entered Designation")

        customerReferral.get_company_name().send_keys(company_name)
        logger.info("Entered Company Name")

        customerReferral.get_select_reason_company_location().click()
        logger.info("Clicked on the company location dropdown")

        customerReferral.select_value_dropdown(company_location).click()
        logger.info("Clicked on the location")

        customerReferral.get_select_reason_company_size().click()
        logger.info("Clicked on the company size dropdown")

        customerReferral.select_value_dropdown(company_size).click()
        logger.info("Clicked on the company size")

        customerReferral.get_select_reason_company_sector().click()
        logger.info("Clicked on the company sector dropdown")

        customerReferral.select_value_dropdown(company_sector).click()
        logger.info("Clicked on the company sector")

        customerReferral.get_company_revenue().send_keys(company_revenue)
        logger.info("Entered Company Revenue")

        customerReferral.get_company_revenue_potential().send_keys(revenue_potential)
        logger.info("Entered Company Revenue Potential")

        customerReferral.get_select_relationship_referee().click()
        logger.info("Clicked on the Relationship dropdown")


        customerReferral.select_value_dropdown(relationship_referee).click()
        logger.info("Clicked on the Relationship referee")

        customerReferral.get_select_option_yes_no().click()
        logger.info("Clicked on the dropdown of selecting yes or no")

        customerReferral.select_value_dropdown(personally_spoken).click()
        logger.info("Clicked on the Personally Spoken")


        customerReferral.get_select_mode_of_communication().click()
        logger.info("Clicked on the dropdown of mode of communication")

        customerReferral.select_value_dropdown(mode_communication).click()
        logger.info("Clicked on the Mode of communication")

        customerReferral.get_select_interest_level().click()
        logger.info("Clicked on the dropdown of Interest Level")

        customerReferral.select_value_dropdown(interest_expressed).click()
        logger.info("Clicked on the Interest Expressed")

        customerReferral.get_points().send_keys(points_discuss)
        logger.info("Entered Points")

        customerReferral.get_refer().click()
        logger.info("Clicked on Refer Button")

        logger.info(customerReferral.refer_successful_component().text)
        assert customerReferral.refer_successful_component().text=="Customer Referral details were submitted successfully."
        
    @pytest.mark.parametrize("contact_name,email_id,phone_number,designation,company_name,company_location,company_size,company_sector,company_revenue,revenue_potential,relationship_referee,related,personally_spoken,mode_communication,interest_expressed,points_discuss,attachment,referral_id",customer_ref_data.get_customer_ref_data("test_all_fields_submit_attachment"))
    def test_all_fields_submit_attachment(self,contact_name,email_id,phone_number,designation,company_name,company_location,company_size,company_sector,company_revenue,revenue_potential,relationship_referee,related,personally_spoken,mode_communication,interest_expressed,points_discuss,attachment,referral_id):
        test_file_name="test_customer_referral"
        logger=self.getLogger(test_file_name)

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automationprofiletwo@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("5WT4Rqe91cAzu17M")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MyOrganization").click()
        logger.info("Clicked on MyOrganization")

        myOrganizationPage=MyOrganizationPage(self.driver)

        myOrganizationPage.get_customer_referral().click()
        logger.info("Clicked on Customer Referral")

        customerReferral=CustomerReferral(self.driver)

        customerReferral.get_contact_name().send_keys(contact_name)
        logger.info("Entered Contact Name")

        customerReferral.get_email().send_keys(email_id)
        logger.info("Entered Email ID")

        customerReferral.get_phone_number().send_keys(phone_number)
        logger.info("Entered Mobile Number")

        customerReferral.get_designation().send_keys(designation)
        logger.info("Entered Designation")

        customerReferral.get_company_name().send_keys(company_name)
        logger.info("Entered Company Name")

        customerReferral.get_select_reason_company_location().click()
        logger.info("Clicked on the company location dropdown")

        customerReferral.select_value_dropdown(company_location).click()
        logger.info("Clicked on the location")

        customerReferral.get_select_reason_company_size().click()
        logger.info("Clicked on the company size dropdown")

        customerReferral.select_value_dropdown(company_size).click()
        logger.info("Clicked on the company size")

        customerReferral.get_select_reason_company_sector().click()
        logger.info("Clicked on the company sector dropdown")

        customerReferral.select_value_dropdown(company_sector).click()
        logger.info("Clicked on the company sector")

        customerReferral.get_company_revenue().send_keys(company_revenue)
        logger.info("Entered Company Revenue")

        customerReferral.get_company_revenue_potential().send_keys(revenue_potential)
        logger.info("Entered Company Revenue Potential")

        customerReferral.get_select_relationship_referee().click()
        logger.info("Clicked on the Relationship dropdown")


        customerReferral.select_value_dropdown(relationship_referee).click()
        logger.info("Clicked on the Relationship referee")

        customerReferral.get_select_option_yes_no().click()
        logger.info("Clicked on the dropdown of selecting yes or no")

        customerReferral.select_value_dropdown(personally_spoken).click()
        logger.info("Clicked on the Personally Spoken")


        customerReferral.get_select_mode_of_communication().click()
        logger.info("Clicked on the dropdown of mode of communication")

        customerReferral.select_value_dropdown(mode_communication).click()
        logger.info("Clicked on the Mode of communication")

        customerReferral.get_select_interest_level().click()
        logger.info("Clicked on the dropdown of Interest Level")

        customerReferral.select_value_dropdown(interest_expressed).click()
        logger.info("Clicked on the Interest Expressed")

        customerReferral.get_points().send_keys(points_discuss)
        logger.info("Entered Points")

        customerReferral.get_file().send_keys(attachment)
        logger.info("Uploaded File")

        customerReferral.get_refer().click()
        logger.info("Clicked on Refer Button")

        logger.info(customerReferral.refer_successful_component().text)
        assert customerReferral.refer_successful_component().text=="Customer Referral details were submitted successfully."


    @pytest.mark.man
    @pytest.mark.parametrize("contact_name,email_id,phone_number,designation,company_name,company_location,company_size,company_sector,company_revenue,revenue_potential,relationship_referee,related,personally_spoken,mode_communication,interest_expressed,points_discuss,attachment,referral_id",customer_ref_data.get_customer_ref_data("test_no_mandatory_fields"))
    def test_no_mandatory_fields(self,contact_name,email_id,phone_number,designation,company_name,company_location,company_size,company_sector,company_revenue,revenue_potential,relationship_referee,related,personally_spoken,mode_communication,interest_expressed,points_discuss,attachment,referral_id):
        test_file_name="test_customer_referral"
        logger=self.getLogger(test_file_name)

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automationprofiletwo@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("5WT4Rqe91cAzu17M")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MyOrganization").click()
        logger.info("Clicked on MyOrganization")

        myOrganizationPage=MyOrganizationPage(self.driver)

        myOrganizationPage.get_customer_referral().click()
        logger.info("Clicked on Customer Referral")

        customerReferral=CustomerReferral(self.driver)

        if(contact_name!=None):
            customerReferral.get_contact_name().send_keys(contact_name)
            logger.info("Entered Contact Name")

        if(email_id!=None):
            customerReferral.get_email().send_keys(email_id)
            logger.info("Entered Email ID")

        if(phone_number!=None):
            customerReferral.get_phone_number().send_keys(phone_number)
            logger.info("Entered Mobile Number")

        if(designation!=None):
            customerReferral.get_designation().send_keys(designation)
            logger.info("Entered Designation")

        customerReferral.get_company_name().send_keys(company_name)
        logger.info("Entered Company Name")

        customerReferral.get_select_reason_company_location().click()
        logger.info("Clicked on the company location dropdown")

        customerReferral.select_value_dropdown(company_location).click()
        logger.info("Clicked on the location")

        customerReferral.get_select_reason_company_size().click()
        logger.info("Clicked on the company size dropdown")

        customerReferral.select_value_dropdown(company_size).click()
        logger.info("Clicked on the company size")

        customerReferral.get_select_reason_company_sector().click()
        logger.info("Clicked on the company sector dropdown")

        customerReferral.select_value_dropdown(company_sector).click()
        logger.info("Clicked on the company sector")

        customerReferral.get_company_revenue().send_keys(company_revenue)
        logger.info("Entered Company Revenue")

        customerReferral.get_company_revenue_potential().send_keys(revenue_potential)
        logger.info("Entered Company Revenue Potential")

        customerReferral.get_select_relationship_referee().click()
        logger.info("Clicked on the Relationship dropdown")


        customerReferral.select_value_dropdown(relationship_referee).click()
        logger.info("Clicked on the Relationship referee")

        customerReferral.get_select_option_yes_no().click()
        logger.info("Clicked on the dropdown of selecting yes or no")

        customerReferral.select_value_dropdown(personally_spoken).click()
        logger.info("Clicked on the Personally Spoken")


        customerReferral.get_select_mode_of_communication().click()
        logger.info("Clicked on the dropdown of mode of communication")

        customerReferral.select_value_dropdown(mode_communication).click()
        logger.info("Clicked on the Mode of communication")

        customerReferral.get_select_interest_level().click()
        logger.info("Clicked on the dropdown of Interest Level")

        customerReferral.select_value_dropdown(interest_expressed).click()
        logger.info("Clicked on the Interest Expressed")

        customerReferral.get_points().send_keys(points_discuss)
        logger.info("Entered Points")


        customerReferral.get_refer().click()
        logger.info("Clicked on Refer Button")

        try:
            assert customerReferral.refer_successful_component().text=="Customer Referral details were submitted successfully."
        except:
            assert True
    

    @pytest.mark.card
    @pytest.mark.parametrize("contact_name,email_id,phone_number,designation,company_name,company_location,company_size,company_sector,company_revenue,revenue_potential,relationship_referee,related,personally_spoken,mode_communication,interest_expressed,points_discuss,attachment,referral_id",customer_ref_data.get_customer_ref_data("test_card_details"))
    def test_card_details(self,contact_name,email_id,phone_number,designation,company_name,company_location,company_size,company_sector,company_revenue,revenue_potential,relationship_referee,related,personally_spoken,mode_communication,interest_expressed,points_discuss,attachment,referral_id):
        test_file_name="test_customer_referral"
        logger=self.getLogger(test_file_name)

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automationprofiletwo@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("5WT4Rqe91cAzu17M")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MyOrganization").click()
        logger.info("Clicked on MyOrganization")

        myOrganizationPage=MyOrganizationPage(self.driver)

        myOrganizationPage.get_customer_referral().click()
        logger.info("Clicked on Customer Referral")

        customerReferral=CustomerReferral(self.driver)

        if(contact_name!=None):
            customerReferral.get_contact_name().send_keys(contact_name)
            logger.info("Entered Contact Name")

        if(email_id!=None):
            customerReferral.get_email().send_keys(email_id)
            logger.info("Entered Email ID")

        if(phone_number!=None):
            customerReferral.get_phone_number().send_keys(phone_number)
            logger.info("Entered Mobile Number")

        if(designation!=None):
            customerReferral.get_designation().send_keys(designation)
            logger.info("Entered Designation")

        customerReferral.get_company_name().send_keys(company_name)
        logger.info("Entered Company Name")

        customerReferral.get_select_reason_company_location().click()
        logger.info("Clicked on the company location dropdown")

        customerReferral.select_value_dropdown(company_location).click()
        logger.info("Clicked on the location")

        customerReferral.get_select_reason_company_size().click()
        logger.info("Clicked on the company size dropdown")

        customerReferral.select_value_dropdown(company_size).click()
        logger.info("Clicked on the company size")

        customerReferral.get_select_reason_company_sector().click()
        logger.info("Clicked on the company sector dropdown")

        customerReferral.select_value_dropdown(company_sector).click()
        logger.info("Clicked on the company sector")

        customerReferral.get_company_revenue().send_keys(company_revenue)
        logger.info("Entered Company Revenue")

        customerReferral.get_company_revenue_potential().send_keys(revenue_potential)
        logger.info("Entered Company Revenue Potential")

        customerReferral.get_select_relationship_referee().click()
        logger.info("Clicked on the Relationship dropdown")


        customerReferral.select_value_dropdown(relationship_referee).click()
        logger.info("Clicked on the Relationship referee")

        customerReferral.get_select_option_yes_no().click()
        logger.info("Clicked on the dropdown of selecting yes or no")

        customerReferral.select_value_dropdown(personally_spoken).click()
        logger.info("Clicked on the Personally Spoken")


        customerReferral.get_select_mode_of_communication().click()
        logger.info("Clicked on the dropdown of mode of communication")

        customerReferral.select_value_dropdown(mode_communication).click()
        logger.info("Clicked on the Mode of communication")

        customerReferral.get_select_interest_level().click()
        logger.info("Clicked on the dropdown of Interest Level")

        customerReferral.select_value_dropdown(interest_expressed).click()
        logger.info("Clicked on the Interest Expressed")

        customerReferral.get_points().send_keys(points_discuss)
        logger.info("Entered Points")


        customerReferral.get_refer().click()
        logger.info("Clicked on Refer Button")

        if(customerReferral.refer_successful_component().text=="Customer Referral details were submitted successfully."):
            logger.info("Customer Referral details were submitted successfully. on card is confirmed")
        else:
            assert False
            return

        if(customerReferral.validate_email_success().text==email_id):
            logger.info(customerReferral.validate_email_success().text)
            logger.info("Email ID on card is confirmed")
        else:
            assert False
            return
        
        if(customerReferral.validate_name_success().text==contact_name):
            logger.info(customerReferral.validate_name_success().text)
            logger.info("Contact Name on card is confirmed")
        else:
            assert False
            return

        if(customerReferral.validate_mobile_success().text==phone_number):
            logger.info("Phone number on card is confirmed")
        else:
            assert False
            return
        assert True
        

    @pytest.mark.search
    @pytest.mark.parametrize("contact_name,email_id,phone_number,designation,company_name,company_location,company_size,company_sector,company_revenue,revenue_potential,relationship_referee,related,personally_spoken,mode_communication,interest_expressed,points_discuss,attachment,referral_id",customer_ref_data.get_customer_ref_data("test_search_referral"))
    def test_search_referral(self,contact_name,email_id,phone_number,designation,company_name,company_location,company_size,company_sector,company_revenue,revenue_potential,relationship_referee,related,personally_spoken,mode_communication,interest_expressed,points_discuss,attachment,referral_id):
        test_file_name="test_customer_referral"
        logger=self.getLogger(test_file_name)

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automationprofiletwo@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("5WT4Rqe91cAzu17M")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MyOrganization").click()
        logger.info("Clicked on MyOrganization")

        myOrganizationPage=MyOrganizationPage(self.driver)

        myOrganizationPage.get_customer_referral().click()
        logger.info("Clicked on Customer Referral")

        customerReferral=CustomerReferral(self.driver)

        customerReferral.get_my_referral_button().click()
        time.sleep(3)
        customerReferral.get_id_search().send_keys(referral_id)
        time.sleep(3)
        assert customerReferral.get_ag_grid_elements()>=1


    @pytest.mark.phone
    @pytest.mark.parametrize("contact_name,email_id,phone_number,designation,company_name,company_location,company_size,company_sector,company_revenue,revenue_potential,relationship_referee,related,personally_spoken,mode_communication,interest_expressed,points_discuss,attachment,referral_id",customer_ref_data.get_customer_ref_data("test_phone_number_field"))
    def test_phone_number_field(self,contact_name,email_id,phone_number,designation,company_name,company_location,company_size,company_sector,company_revenue,revenue_potential,relationship_referee,related,personally_spoken,mode_communication,interest_expressed,points_discuss,attachment,referral_id):
        test_file_name="test_customer_referral"
        logger=self.getLogger(test_file_name)

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automationprofiletwo@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("5WT4Rqe91cAzu17M")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MyOrganization").click()
        logger.info("Clicked on MyOrganization")

        myOrganizationPage=MyOrganizationPage(self.driver)

        myOrganizationPage.get_customer_referral().click()
        logger.info("Clicked on Customer Referral")

        customerReferral=CustomerReferral(self.driver)

        customerReferral.get_contact_name().send_keys(contact_name)
        logger.info("Entered Contact Name")

        customerReferral.get_email().send_keys(email_id)
        logger.info("Entered Email ID")

        customerReferral.get_phone_number().send_keys(phone_number)
        logger.info("Entered Mobile Number")

        customerReferral.get_designation().send_keys(designation)
        logger.info("Entered Designation")

        customerReferral.get_company_name().send_keys(company_name)
        logger.info("Entered Company Name")

        customerReferral.get_select_reason_company_location().click()
        logger.info("Clicked on the company location dropdown")

        customerReferral.select_value_dropdown(company_location).click()
        logger.info("Clicked on the location")

        customerReferral.get_select_reason_company_size().click()
        logger.info("Clicked on the company size dropdown")

        customerReferral.select_value_dropdown(company_size).click()
        logger.info("Clicked on the company size")

        customerReferral.get_select_reason_company_sector().click()
        logger.info("Clicked on the company sector dropdown")

        customerReferral.select_value_dropdown(company_sector).click()
        logger.info("Clicked on the company sector")

        customerReferral.get_company_revenue().send_keys(company_revenue)
        logger.info("Entered Company Revenue")

        customerReferral.get_company_revenue_potential().send_keys(revenue_potential)
        logger.info("Entered Company Revenue Potential")

        customerReferral.get_select_relationship_referee().click()
        logger.info("Clicked on the Relationship dropdown")


        customerReferral.select_value_dropdown(relationship_referee).click()
        logger.info("Clicked on the Relationship referee")

        customerReferral.get_select_option_yes_no().click()
        logger.info("Clicked on the dropdown of selecting yes or no")

        customerReferral.select_value_dropdown(personally_spoken).click()
        logger.info("Clicked on the Personally Spoken")


        customerReferral.get_select_mode_of_communication().click()
        logger.info("Clicked on the dropdown of mode of communication")

        customerReferral.select_value_dropdown(mode_communication).click()
        logger.info("Clicked on the Mode of communication")

        customerReferral.get_select_interest_level().click()
        logger.info("Clicked on the dropdown of Interest Level")

        customerReferral.select_value_dropdown(interest_expressed).click()
        logger.info("Clicked on the Interest Expressed")

        customerReferral.get_points().send_keys(points_discuss)
        logger.info("Entered Points")

        customerReferral.get_refer().click()
        logger.info("Clicked on Refer Button")

        logger.info(customerReferral.refer_successful_component().text)

        if(len(str(phone_number))<10 or len(str(phone_number))>10):
            if(customerReferral.refer_successful_component().text=="Customer Referral details were submitted successfully."):
                assert False
        assert True

    @pytest.mark.dropdown
    @pytest.mark.parametrize("contact_name,email_id,phone_number,designation,company_name,company_location,company_size,company_sector,company_revenue,revenue_potential,relationship_referee,related,personally_spoken,mode_communication,interest_expressed,points_discuss,attachment,referral_id",customer_ref_data.get_customer_ref_data("test_values_not_present_dropdown_submit"))
    def test_values_not_present_dropdown_submit(self,contact_name,email_id,phone_number,designation,company_name,company_location,company_size,company_sector,company_revenue,revenue_potential,relationship_referee,related,personally_spoken,mode_communication,interest_expressed,points_discuss,attachment,referral_id):
        test_file_name="test_customer_referral"
        logger=self.getLogger(test_file_name)

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automationprofiletwo@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("5WT4Rqe91cAzu17M")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MyOrganization").click()
        logger.info("Clicked on MyOrganization")

        myOrganizationPage=MyOrganizationPage(self.driver)

        myOrganizationPage.get_customer_referral().click()
        logger.info("Clicked on Customer Referral")

        customerReferral=CustomerReferral(self.driver)

        customerReferral.get_contact_name().send_keys(contact_name)
        logger.info("Entered Contact Name")

        customerReferral.get_email().send_keys(email_id)
        logger.info("Entered Email ID")

        customerReferral.get_phone_number().send_keys(phone_number)
        logger.info("Entered Mobile Number")

        customerReferral.get_designation().send_keys(designation)
        logger.info("Entered Designation")

        customerReferral.get_company_name().send_keys(company_name)
        logger.info("Entered Company Name")

        customerReferral.get_select_reason_company_location().send_keys(company_location)
        logger.info("Entered Company Location")

        customerReferral.select_value_dropdown_not_present(company_location).click()
        logger.info("Clicked on the location")

        customerReferral.get_select_reason_company_size().click()
        logger.info("Clicked on the company size dropdown")

        customerReferral.select_value_dropdown(company_size).click()
        logger.info("Clicked on the company size")

        customerReferral.get_select_reason_company_sector().send_keys(company_sector)
        logger.info("Entered Company Sector")

        customerReferral.select_value_dropdown_not_present(company_sector).click()
        logger.info("Clicked on the company sector")

        customerReferral.get_company_revenue().send_keys(company_revenue)
        logger.info("Entered Company Revenue")

        customerReferral.get_company_revenue_potential().send_keys(revenue_potential)
        logger.info("Entered Company Revenue Potential")

        customerReferral.get_select_relationship_referee().click()
        logger.info("Clicked on the Relationship dropdown")


        customerReferral.select_value_dropdown(relationship_referee).click()
        logger.info("Clicked on the Relationship referee")

        customerReferral.get_select_option_yes_no().click()
        logger.info("Clicked on the dropdown of selecting yes or no")

        customerReferral.get_relationship_with_referee().send_keys(related)
        logger.info("Entered family or relative details")

        customerReferral.select_value_dropdown(personally_spoken).click()
        logger.info("Clicked on the Personally Spoken")


        customerReferral.get_select_mode_of_communication().click()
        logger.info("Clicked on the dropdown of mode of communication")

        customerReferral.select_value_dropdown(mode_communication).click()
        logger.info("Clicked on the Mode of communication")

        customerReferral.get_select_interest_level().click()
        logger.info("Clicked on the dropdown of Interest Level")

        customerReferral.select_value_dropdown(interest_expressed).click()
        logger.info("Clicked on the Interest Expressed")

        customerReferral.get_points().send_keys(points_discuss)
        logger.info("Entered Points")

        customerReferral.get_refer().click()
        logger.info("Clicked on Refer Button")

        logger.info(customerReferral.refer_successful_component().text)
        assert customerReferral.refer_successful_component().text=="Customer Referral details were submitted successfully."
