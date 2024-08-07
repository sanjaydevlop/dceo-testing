from pageObjects.LoginPage import LoginPage
from pageObjects.MyTransactionPage import MyTransactionPage
from pageObjects.LeaderLeaveRequests import LeaderLeaveRequests
from ..TestScripts.BaseClass import BaseClass
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver import ActionChains
from TestData.approve_reject_leave_data import approve_reject_leave_data
import pytest
import datetime,time
from datetime import datetime, timedelta


class Test_approve_reject_leave(BaseClass):
    
    @pytest.mark.parametrize("leaderName,leaderId,requestedDate,fromDate,toDate,noOfDays,typeOfLeave,reason,expectedResult",approve_reject_leave_data.get_approve_reject_leave_data("Sheet1"))
    def test_approve_leave(self,leaderName,leaderId,requestedDate,fromDate,toDate,noOfDays,typeOfLeave,reason,expectedResult):

        test_file_name="test_approve_leave"
        logger=self.getLogger(test_file_name)
        

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("sanjaysurya.thulluru@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("Surya@2527")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MyTransactions").click()
        logger.info("Clicked on MyTransactions")

        MyTransactionPage(self.driver).get_Leader_Leave_Requests().click()
        logger.info("Navigated to Leader Leave Requests")

        leaderleaverequests=LeaderLeaveRequests(self.driver)
        
        ActionChains(self.driver)\
            .scroll_to_element(leaderleaverequests.get_leave_requests_tab())\
                .perform()
        leaderleaverequests.get_leader_name_search().send_keys(leaderName)
        logger.info("Searched by leader name")

        leaderleaverequests.get_leader_id_search().send_keys(leaderId)
        logger.info("Searched by leader Id")

        leaderleaverequests.get_requested_date_search().send_keys(requestedDate)
        logger.info("Searched by requested date")
        
        leaderleaverequests.get_to_date_search().send_keys(toDate)
        logger.info("Searched by to date")

        leaderleaverequests.get_from_date_search().send_keys(fromDate)
        logger.info("Searched by from date")

        leaderleaverequests.get_number_of_days_search().send_keys(noOfDays)
        logger.info("Searched by number of days")

        leaderleaverequests.get_type_of_leave_search().send_keys(typeOfLeave)
        logger.info("Searched by type of leave")

        leaderleaverequests.get_reason_search().send_keys(reason)
        logger.info("Searched by Reason for leave")
        
        leaderleaverequests.get_approve_reject_button().click()
        logger.info('Clicked on approve/reject tab')

        # available_balance=float(leaderleaverequests.get_available_leave())
        # applied_leave=float(leaderleaverequests.get_applied_leave())
        # loss_of_pay=float(leaderleaverequests.get_loss_of_pay())
        # if applied_leave>available_balance:
        #     if loss_of_pay!=(applied_leave-available_balance):
        #         logger.error('loss of pay is incorrect')
        #         assert False

        leaderleaverequests.get_approve_button().click() 
        result=leaderleaverequests.get_toast()
        assert (expectedResult in result)

    @pytest.mark.parametrize("leaderName,leaderId,requestedDate,fromDate,toDate,noOfDays,typeOfLeave,reason,reject_reason,expectedResult",approve_reject_leave_data.get_approve_reject_leave_data("Sheet2"))
    def test_reject_with_reason(self,leaderName,leaderId,requestedDate,fromDate,toDate,noOfDays,typeOfLeave,reason,reject_reason,expectedResult):
    
        test_file_name="test_reject_with_reason"
        logger=self.getLogger(test_file_name)
        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("sanjaysurya.thulluru@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("Surya@2527")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MyTransactions").click()
        logger.info("Clicked on MyTransactions")

        MyTransactionPage(self.driver).get_Leader_Leave_Requests().click()
        logger.info("Navigated to Leader Leave Requests")

        leaderleaverequests=LeaderLeaveRequests(self.driver)
        
        ActionChains(self.driver)\
            .scroll_to_element(leaderleaverequests.get_leave_requests_tab())\
                .perform()
        
        leaderleaverequests.get_leader_name_search().send_keys(leaderName)
        logger.info("Searched by leader name")

        leaderleaverequests.get_leader_id_search().send_keys(leaderId)
        logger.info("Searched by leader Id")

        leaderleaverequests.get_requested_date_search().send_keys(requestedDate)
        logger.info("Searched by requested date")
        
        leaderleaverequests.get_to_date_search().send_keys(toDate)
        logger.info("Searched by to date")

        leaderleaverequests.get_from_date_search().send_keys(fromDate)
        logger.info("Searched by from date")

        leaderleaverequests.get_number_of_days_search().send_keys(noOfDays)
        logger.info("Searched by number of days")

        leaderleaverequests.get_type_of_leave_search().send_keys(typeOfLeave)
        logger.info("Searched by type of leave")

        leaderleaverequests.get_reason_search().send_keys(reason)
        logger.info("Searched by Reason for leave")
        
        leaderleaverequests.get_approve_reject_button().click()
        logger.info('Clicked on approve/reject tab')
        
        leaderleaverequests.get_reject_button().click() 
        logger.info('Clicked on Reject button')

        leaderleaverequests.get_reject_reason().click() 
        logger.info('Clicked on reject reason dropdown')

        leaderleaverequests.select_reason_for_reject(reject_reason).click()
        logger.info('Selected reason for rejection')
        
        leaderleaverequests.get_reject_button().click() 
        logger.info('Clicked on Reject button')
        time.sleep(3)
        result=leaderleaverequests.get_toast()
        assert (expectedResult in result)

        
    @pytest.mark.parametrize("leaderName,leaderId,requestedDate,fromDate,toDate,noOfDays,typeOfLeave,reason,expectedResult",approve_reject_leave_data.get_approve_reject_leave_data("Sheet3"))
    def test_reject_leave_without_reason(self,leaderName,leaderId,requestedDate,fromDate,toDate,noOfDays,typeOfLeave,reason,expectedResult):
        
        test_file_name="test_reject_leave_without_reason"
        logger=self.getLogger(test_file_name)
        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("sanjaysurya.thulluru@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("Surya@2527")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MyTransactions").click()
        logger.info("Clicked on MyTransactions")

        MyTransactionPage(self.driver).get_Leader_Leave_Requests().click()
        logger.info("Navigated to Leader Leave Requests")

        leaderleaverequests=LeaderLeaveRequests(self.driver)
        
        ActionChains(self.driver)\
            .scroll_to_element(leaderleaverequests.get_leave_requests_tab())\
                .perform()
        
        leaderleaverequests.get_leader_name_search().send_keys(leaderName)
        logger.info("Searched by leader name")

        leaderleaverequests.get_leader_id_search().send_keys(leaderId)
        logger.info("Searched by leader Id")

        leaderleaverequests.get_requested_date_search().send_keys(requestedDate)
        logger.info("Searched by requested date")
        
        leaderleaverequests.get_to_date_search().send_keys(toDate)
        logger.info("Searched by to date")

        leaderleaverequests.get_from_date_search().send_keys(fromDate)
        logger.info("Searched by from date")

        leaderleaverequests.get_number_of_days_search().send_keys(noOfDays)
        logger.info("Searched by number of days")

        leaderleaverequests.get_type_of_leave_search().send_keys(typeOfLeave)
        logger.info("Searched by type of leave")

        leaderleaverequests.get_reason_search().send_keys(reason)
        logger.info("Searched by Reason for leave")
        
        leaderleaverequests.get_approve_reject_button().click()
        logger.info('Clicked on approve/reject tab')
        
        leaderleaverequests.get_reject_button().click() 
        logger.info('Clicked on Reject button')

        check = leaderleaverequests.get_reject_button().is_enabled() 
        logger.info('Checked whether button is enabled or disabled')

        if check:
             result = 'enabled'
        else:
             result = 'disabled'
        assert (expectedResult in result)
    
    @pytest.mark.parametrize("leaderName,leaderId,requestedDate,fromDate,toDate,noOfDays,typeOfLeave,reason,reject_reason,expectedResult",approve_reject_leave_data.get_approve_reject_leave_data("Sheet4"))
    def test_reject_after_unselect_reason(self,leaderName,leaderId,requestedDate,fromDate,toDate,noOfDays,typeOfLeave,reason,reject_reason,expectedResult):
        
        test_file_name="test_reject_after_unselect_reason"
        logger=self.getLogger(test_file_name)
        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("sanjaysurya.thulluru@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("Surya@2527")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MyTransactions").click()
        logger.info("Clicked on MyTransactions")

        MyTransactionPage(self.driver).get_Leader_Leave_Requests().click()
        logger.info("Navigated to Leader Leave Requests")

        leaderleaverequests=LeaderLeaveRequests(self.driver)
        
        ActionChains(self.driver)\
            .scroll_to_element(leaderleaverequests.get_leave_requests_tab())\
                .perform()
        
        leaderleaverequests.get_leader_name_search().send_keys(leaderName)
        logger.info("Searched by leader name")

        leaderleaverequests.get_leader_id_search().send_keys(leaderId)
        logger.info("Searched by leader Id")

        leaderleaverequests.get_requested_date_search().send_keys(requestedDate)
        logger.info("Searched by requested date")
        
        leaderleaverequests.get_to_date_search().send_keys(toDate)
        logger.info("Searched by to date")

        leaderleaverequests.get_from_date_search().send_keys(fromDate)
        logger.info("Searched by from date")

        leaderleaverequests.get_number_of_days_search().send_keys(noOfDays)
        logger.info("Searched by number of days")

        leaderleaverequests.get_type_of_leave_search().send_keys(typeOfLeave)
        logger.info("Searched by type of leave")

        leaderleaverequests.get_reason_search().send_keys(reason)
        logger.info("Searched by Reason for leave")
        
        leaderleaverequests.get_approve_reject_button().click()
        logger.info('Clicked on approve/reject tab')
        
        leaderleaverequests.get_reject_button().click() 
        logger.info('Clicked on Reject button')

        
        leaderleaverequests.get_reject_reason().click() 
        logger.info('Clicked on reject reason dropdown')

        leaderleaverequests.select_reason_for_reject(reject_reason).click()
        logger.info('Selected reason for rejection')
        # ActionChains(self.driver)\
        #     .move_to_element_with_offset(leaderleaverequests.get_reason(),0,-150)\
        #         .perform()
        ActionChains(self.driver)\
            .scroll_to_element(leaderleaverequests.get_reject_reason_header())\
                .perform()

        leaderleaverequests.get_reject_reason_unselect_cross().click()
        logger.info('Unselected the reason which was previously selected')

        check = leaderleaverequests.get_reject_button().is_enabled() 
        logger.info('Checked whether button is enabled or disabled')

        if check:
             result = 'enabled'
        else:
             result = 'disabled'
        assert (expectedResult in result)

    
    @pytest.mark.parametrize("leaderName,leaderId,requestedDate,fromDate,toDate,noOfDays,typeOfLeave,reason,reject_reason,expectedResult",approve_reject_leave_data.get_approve_reject_leave_data("Sheet5"))
    def test_cancel_in_reject(self,leaderName,leaderId,requestedDate,fromDate,toDate,noOfDays,typeOfLeave,reason,reject_reason,expectedResult):
    
        test_file_name="test_cancel_in_reject"
        logger=self.getLogger(test_file_name)
        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("sanjaysurya.thulluru@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("Surya@2527")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MyTransactions").click()
        logger.info("Clicked on MyTransactions")

        MyTransactionPage(self.driver).get_Leader_Leave_Requests().click()
        logger.info("Navigated to Leader Leave Requests")

        leaderleaverequests=LeaderLeaveRequests(self.driver)
        
        ActionChains(self.driver)\
            .scroll_to_element(leaderleaverequests.get_leave_requests_tab())\
                .perform()
        
        leaderleaverequests.get_leader_name_search().send_keys(leaderName)
        logger.info("Searched by leader name")

        leaderleaverequests.get_leader_id_search().send_keys(leaderId)
        logger.info("Searched by leader Id")

        leaderleaverequests.get_requested_date_search().send_keys(requestedDate)
        logger.info("Searched by requested date")
        
        leaderleaverequests.get_to_date_search().send_keys(toDate)
        logger.info("Searched by to date")

        leaderleaverequests.get_from_date_search().send_keys(fromDate)
        logger.info("Searched by from date")

        leaderleaverequests.get_number_of_days_search().send_keys(noOfDays)
        logger.info("Searched by number of days")

        leaderleaverequests.get_type_of_leave_search().send_keys(typeOfLeave)
        logger.info("Searched by type of leave")

        leaderleaverequests.get_reason_search().send_keys(reason)
        logger.info("Searched by Reason for leave")
        
        leaderleaverequests.get_approve_reject_button().click()
        logger.info('Clicked on approve/reject tab')
        
        leaderleaverequests.get_reject_button().click() 
        logger.info('Clicked on Reject button')

        leaderleaverequests.get_reject_reason().click() 
        logger.info('Clicked on reject reason dropdown')

        leaderleaverequests.select_reason_for_reject(reject_reason).click()
        logger.info('Selected reason for rejection')

        leaderleaverequests.get_cancel_button().click()
        logger.info('Clicked on Cancel button')

        leaderleaverequests.get_clear_filters().click()

        leaderleaverequests.get_leader_name_search().send_keys(leaderName)
        logger.info("Check search by leader name")

        leaderleaverequests.get_leader_id_search().send_keys(leaderId)
        logger.info("Check search by leader Id")

        leaderleaverequests.get_requested_date_search().send_keys(requestedDate)
        logger.info("Check search by requested date")
        
        leaderleaverequests.get_to_date_search().send_keys(toDate)
        logger.info("Check search by to date")

        leaderleaverequests.get_from_date_search().send_keys(fromDate)
        logger.info("Check search by from date")

        leaderleaverequests.get_number_of_days_search().send_keys(noOfDays)
        logger.info("Check search by number of days")

        leaderleaverequests.get_type_of_leave_search().send_keys(typeOfLeave)
        logger.info("Check search by type of leave")

        leaderleaverequests.get_reason_search().send_keys(reason)
        logger.info("Check search by Reason for leave")   

        if leaderleaverequests.get_approve_reject_button().is_enabled():
            result = 'as expected'
        else:
            result = 'different than expected'
        assert (expectedResult==result)

    

    @pytest.mark.parametrize("leaderName,leaderId,requestedDate,fromDate,toDate,noOfDays,typeOfLeave,reason,expectedResult",approve_reject_leave_data.get_approve_reject_leave_data("Sheet6"))
    def test_check_history_match(self,leaderName,leaderId,requestedDate,fromDate,toDate,noOfDays,typeOfLeave,reason,expectedResult):
        test_file_name="test_check_history_match"
        logger=self.getLogger(test_file_name)
        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("sanjaysurya.thulluru@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("Surya@2527")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MyTransactions").click()
        logger.info("Clicked on MyTransactions")

        MyTransactionPage(self.driver).get_Leader_Leave_Requests().click()
        logger.info("Navigated to Leader Leave Requests")

        leaderleaverequests=LeaderLeaveRequests(self.driver)

        ActionChains(self.driver)\
            .scroll_to_element(leaderleaverequests.get_header())\
                .perform()
        time.sleep(3)
        leaderleaverequests.get_history_tab().click()
        logger.info("Navigated to history tab")
        
        leaderleaverequests.get_leader_name_search().send_keys(leaderName)
        logger.info("Searched by leader name")

        leaderleaverequests.get_leader_id_search().send_keys(leaderId)
        logger.info("Searched by leader Id")

        leaderleaverequests.get_requested_date_search().send_keys(requestedDate)
        logger.info("Searched by requested date")
        
        leaderleaverequests.get_to_date_search().send_keys(toDate)
        logger.info("Searched by to date")

        leaderleaverequests.get_from_date_search().send_keys(fromDate)
        logger.info("Searched by from date")

        leaderleaverequests.get_number_of_days_search().send_keys(noOfDays)
        logger.info("Searched by number of days")

        leaderleaverequests.get_type_of_leave_search().send_keys(typeOfLeave)
        logger.info("Searched by type of leave")

        leaderleaverequests.get_reason_search().send_keys(reason)
        logger.info("Searched by Reason for leave")

        result = leaderleaverequests.get_history_accept_status()
        assert(expectedResult in result)
        

       



      
    

    