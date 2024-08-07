from pageObjects.CustomerReferralPage import CustomerReferral
from pageObjects.LoginPage import LoginPage 
from pageObjects.HomePage import HomePage
from pageObjects.MyTransactionPage import MyTransactionPage
from ..TestScripts.BaseClass import BaseClass
from selenium.webdriver.support.ui import WebDriverWait,Select
import time
import pytest

class Test_Feedback_Hub(BaseClass):
    
    def test_submit_feedback_rateStringer_rateMyTransactions_write_text(self):
        test_file_name="test_feedback_hub"
        logger=self.getLogger(test_file_name)
        loginPage=LoginPage(self.driver)
        loginPage.get_user_name().send_keys("vinay.dhandaveni@braneenterprises.com")
        logger.info('Entered Username')
        loginPage.get_password().send_keys("Test@1234")
        logger.info('Entered Password')
        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')
        dceoLandingPage.get_dashboard_button().click()
        homePage=HomePage(self.driver)
        homePage.get_my_transactions().click()
        myTransactionPage=MyTransactionPage(self.driver)
        myTransactionPage.GiveFeedBackHubMyTransactionPage().click()
        myTransactionPage.rateDceo(1).click()
        myTransactionPage.rateTransactionsPage(2).click()
        myTransactionPage.inputFeedbackText().send_keys("Good")
        myTransactionPage.submitFeedback().click()
        myTransactionPage.FeedBackOk().click()
        assert True

    def test_submit_feedback_rateStringer_write_text(self):
        test_file_name="test_feedback_hub"
        logger=self.getLogger(test_file_name)
        loginPage=LoginPage(self.driver)
        loginPage.get_user_name().send_keys("vinay.dhandaveni@braneenterprises.com")
        logger.info('Entered Username')
        loginPage.get_password().send_keys("Test@1234")
        logger.info('Entered Password')
        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')
        dceoLandingPage.get_dashboard_button().click()
        homePage=HomePage(self.driver)
        homePage.get_my_transactions().click()
        myTransactionPage=MyTransactionPage(self.driver)
        myTransactionPage.GiveFeedBackHubMyTransactionPage().click()
        myTransactionPage.rateDceo(1).click()
        # myTransactionPage.rateTransactionsPage(2).click()
        myTransactionPage.inputFeedbackText().send_keys("Good")
        myTransactionPage.submitFeedback().click()
        try:
            myTransactionPage.FeedBackOk().click()
            assert False
        except:
            assert True
    
    @pytest.mark.third
    def test_submit_feedback_rateStringer_rateMyTransactions(self):
        test_file_name="test_feedback_hub"
        logger=self.getLogger(test_file_name)
        loginPage=LoginPage(self.driver)
        loginPage.get_user_name().send_keys("vinay.dhandaveni@braneenterprises.com")
        logger.info('Entered Username')
        loginPage.get_password().send_keys("Test@1234")
        logger.info('Entered Password')
        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')
        dceoLandingPage.get_dashboard_button().click()
        homePage=HomePage(self.driver)
        homePage.get_my_transactions().click()
        myTransactionPage=MyTransactionPage(self.driver)
        myTransactionPage.GiveFeedBackHubMyTransactionPage().click()
        myTransactionPage.rateDceo(1).click()
        myTransactionPage.rateTransactionsPage(2).click()
        # myTransactionPage.inputFeedbackText().send_keys("Good")
        myTransactionPage.submitFeedback().click()
        myTransactionPage.FeedBackOk().click()
        assert True
    
    def test_submit_feedback_rateMyTransaction_write_text(self):
        test_file_name="test_feedback_hub"
        logger=self.getLogger(test_file_name)
        loginPage=LoginPage(self.driver)
        loginPage.get_user_name().send_keys("vinay.dhandaveni@braneenterprises.com")
        logger.info('Entered Username')
        loginPage.get_password().send_keys("Test@1234")
        logger.info('Entered Password')
        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')
        dceoLandingPage.get_dashboard_button().click()
        homePage=HomePage(self.driver)
        homePage.get_my_transactions().click()
        myTransactionPage=MyTransactionPage(self.driver)
        myTransactionPage.GiveFeedBackHubMyTransactionPage().click()
        myTransactionPage.rateTransactionsPage(2).click()
        myTransactionPage.inputFeedbackText().send_keys("Good")
        myTransactionPage.submitFeedback().click()
        try:
            myTransactionPage.FeedBackOk().click()
            assert False
        except:
            assert True

    
    

    




