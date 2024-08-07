from pageObjects.LoginPage import LoginPage
from pageObjects.MyselfPage import MyselfPage
from pageObjects.LeaveManagementPage import LeaveManagementPage
from ..TestScripts.BaseClass import BaseClass
from selenium.webdriver.support.ui import WebDriverWait,Select
from TestData.apply_leave_data import apply_leave_data
import pytest
import datetime,time
from datetime import datetime, timedelta
from TestData.edit_leave_data import edit_leave_data

class Test_edit_leave(BaseClass):
    
    @pytest.mark.parametrize("leaveType,reason,fromDate,toDate,expectedResult",edit_leave_data.get_edit_leave_data("Sheet1"))
    def test_cancel_leave(self,leaveType,reason,fromDate,toDate,expectedResult):
        test_file_name="test_edit_leave"
        logger=self.getLogger(test_file_name)
        

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automation.three@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("HXo5YeKWPB4ePYoB")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)

        while True:
            try:
                leaveManagementPage.click_on_edit(fromDate,toDate,leaveType,reason).click()
                break
            except:
                leaveManagementPage.get_next_page().click()

        logger.info("Clicked on edit Leave Button")
        leaveManagementPage.get_confirm_cancel_leave_button().click()
        leaveManagementPage.get_cancel_yes().click()
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)
    @pytest.mark.test1
    @pytest.mark.parametrize("old_from_date,old_to_date,old_type,old_reason,fromDate,toDate,expectedResult",edit_leave_data.get_edit_leave_data("Sheet2"))
    def test_change_consolidated_dates_without_partials(self,old_from_date,old_to_date,old_type,old_reason,fromDate,toDate,expectedResult):
        test_file_name="test_edit_leave"
        logger=self.getLogger(test_file_name)
        

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automation.three@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("HXo5YeKWPB4ePYoB")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)

        while True:
            try:
                leaveManagementPage.click_on_edit(old_from_date,old_to_date,old_type,old_reason).click()
                break
            except:
                leaveManagementPage.get_next_page().click()

        leaveManagementPage.get_from_date().click()

        from_date=fromDate.strftime("%d/%m/%Y").split('/')
        to_date=toDate.strftime("%d/%m/%Y").split('/')
        
        Select_year = Select(leaveManagementPage.select_year())

        Select_year.select_by_value(str(from_date[2]))
        logger.info("Selected the from Year")

        Select_month = Select(leaveManagementPage.select_month())
        
        Select_month.select_by_value(str(int(from_date[1])))
        logger.info("Selected the from Month")

        leaveManagementPage.select_date(str(int(from_date[0]))).click()
        logger.info("Selected the from date")

        leaveManagementPage.get_to_date().click()

        Select_year = Select(leaveManagementPage.select_year())

        Select_year.select_by_value(str(to_date[2]))
        logger.info("Selected the to Year")

        Select_month = Select(leaveManagementPage.select_month())
        
        Select_month.select_by_value(str(int(to_date[1])))
        logger.info("Selected the to Month")

        leaveManagementPage.select_date(str(int(to_date[0]))).click()
        logger.info("Selected the to date")
        Available_leave=float(leaveManagementPage.get_available_leave_balance())
        Applied_leave=float(leaveManagementPage.get_applied_leave_balance())
        Loss_of_pay=float(leaveManagementPage.get_loss_of_pay())
        logger.info("Available is checking")
        if Applied_leave>Available_leave:
            if Loss_of_pay==(Applied_leave-Available_leave):
                logger.info('Loss of pay is equal to difference in Applied and Available Leave')
            else:
                logger.error('Loss of pay is incorrect')
                assert False
        if Loss_of_pay>0:
            leaveManagementPage.get_proceed_button().click()
            logger.info("Clicked on Proceed")
        leaveManagementPage.get_confirm_edit().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)
     
    @pytest.mark.parametrize("old_from_date,old_to_date,old_type,old_reason,fromDate,toDate,partialDates,expectedResult",edit_leave_data.get_edit_leave_data("Sheet3"))
    def test_change_consolidated_dates_with_partials(self,old_from_date,old_to_date,old_type,old_reason,fromDate,toDate,partialDates,expectedResult):
        test_file_name="test_edit_leave"
        logger=self.getLogger(test_file_name)
        

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automation.three@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("HXo5YeKWPB4ePYoB")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)

        while True:
            try:
                leaveManagementPage.click_on_edit(old_from_date,old_to_date,old_type,old_reason).click()
                break
            except:
                leaveManagementPage.get_next_page().click()

        leaveManagementPage.get_from_date().click()

        from_date=fromDate.strftime("%d/%m/%Y").split('/')
        to_date=toDate.strftime("%d/%m/%Y").split('/')
        
        Select_year = Select(leaveManagementPage.select_year())

        Select_year.select_by_value(str(from_date[2]))
        logger.info("Selected the from Year")

        Select_month = Select(leaveManagementPage.select_month())
        
        Select_month.select_by_value(str(int(from_date[1])))
        logger.info("Selected the from Month")

        leaveManagementPage.select_date(str(int(from_date[0]))).click()
        logger.info("Selected the from date")

        leaveManagementPage.get_to_date().click()

        Select_year = Select(leaveManagementPage.select_year())

        Select_year.select_by_value(str(to_date[2]))
        logger.info("Selected the to Year")

        Select_month = Select(leaveManagementPage.select_month())
        
        Select_month.select_by_value(str(int(to_date[1])))
        logger.info("Selected the to Month")

        leaveManagementPage.select_date(str(int(to_date[0]))).click()
        logger.info("Selected the to date")
        if partialDates is not None:
            result_list = [[int(key), value] for key, value in (pair.split(':') for pair in str(partialDates).split(','))]

            for partial in result_list:
                leaveManagementPage.get_partial(partial[0]).click()
                logger.info("Clicked on date")
                
                leaveManagementPage.get_partial_radio_button(partial[1]).click()
                logger.info("Selected Partials Reason")
        Available_leave=float(leaveManagementPage.get_available_leave_balance())
        Applied_leave=float(leaveManagementPage.get_applied_leave_balance())
        Loss_of_pay=float(leaveManagementPage.get_loss_of_pay())
        logger.info("Available is checking")
        if Applied_leave>Available_leave:
            if Loss_of_pay==(Applied_leave-Available_leave):
                logger.info('Loss of pay is equal to difference in Applied and Available Leave')
            else:
                logger.error('Loss of pay is incorrect')
                assert False
        if Loss_of_pay>0:
            leaveManagementPage.get_proceed_button().click()
            logger.info("Clicked on Proceed")
        leaveManagementPage.get_confirm_edit().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)

    @pytest.mark.parametrize("old_from_date,old_to_date,old_type,old_reason,reason,expectedResult",edit_leave_data.get_edit_leave_data("Sheet4"))
    def test_change_consolidated_reason(self,old_from_date,old_to_date,old_type,old_reason,reason,expectedResult):
        test_file_name="test_edit_leave"
        logger=self.getLogger(test_file_name)
        

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automation.three@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("HXo5YeKWPB4ePYoB")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)

        while True:
            try:
                leaveManagementPage.click_on_edit(old_from_date,old_to_date,old_type,old_reason).click()
                break
            except:
                leaveManagementPage.get_next_page().click()
        leaveManagementPage.get_reason_for_leave().click()
        logger.info("Clicking Reason Dropdown")

        leaveManagementPage.select_reason_for_leave(reason).click()
        logger.info("Selected Reason")
        leaveManagementPage.get_confirm_edit().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)

    @pytest.mark.parametrize("old_from_date,old_to_date,old_type,old_reason,fromDate,expectedResult",edit_leave_data.get_edit_leave_data("Sheet5"))
    def test_change_special_dates(self,old_from_date,old_to_date,old_type,old_reason,fromDate,expectedResult):
        test_file_name="test_edit_leave"
        logger=self.getLogger(test_file_name)
        

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automation.three@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("HXo5YeKWPB4ePYoB")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)

        while True:
            try:
                leaveManagementPage.click_on_edit(old_from_date,old_to_date,old_type,old_reason).click()
                break
            except:
                leaveManagementPage.get_next_page().click()

        leaveManagementPage.get_from_date().click()

        from_date=fromDate.strftime("%d/%m/%Y").split('/')
        
        
        Select_year = Select(leaveManagementPage.select_year())

        Select_year.select_by_value(str(from_date[2]))
        logger.info("Selected the from Year")

        Select_month = Select(leaveManagementPage.select_month())
        
        Select_month.select_by_value(str(int(from_date[1])))
        logger.info("Selected the from Month")

        leaveManagementPage.select_date(str(int(from_date[0]))).click()
        logger.info("Selected the from date")

        #validations missing
        specialToDate=leaveManagementPage.get_specialToDate()
        logger.info(specialToDate)
        specialfromDate=str(from_date[0])+'/'+str(from_date[1])+'/'+str(from_date[2])
        date_format = "%d/%m/%Y"
        # Convert strings to datetime objects
        convert_from_date = datetime.strptime(specialfromDate, date_format)
        convert_to_date = datetime.strptime(specialToDate, date_format)
        # Calculate the difference in days
        difference = convert_to_date-convert_from_date
        number_of_days = difference.days + 1  # Adding 1 to include both the start and end dates
                    
        if(old_reason=="Maternity"):
            if(float(leaveManagementPage.get_applied_leave_balance())!=number_of_days):
                logger.error("The number of days between the from date and to date is not equal to 182")
                assert False
        elif(old_reason=="Tubectomy"):
            if(float(leaveManagementPage.get_applied_leave_balance())!=number_of_days):
                    logger.error("The number of days between the from date and to date is equal to 14")
                    assert False
        
        elif(old_reason=="Miscarriage"):
            if(float(leaveManagementPage.get_applied_leave_balance())!=number_of_days):
                logger.error("The number of days between the from date and to date is equal to 42")
                assert False
        elif(old_reason=="Paternity"):
            if(float(leaveManagementPage.get_applied_leave_balance())!=number_of_days):
                logger.error("The number of days between the from date and to date is not equal to 5")
                assert False
        
        leaveManagementPage.get_confirm_edit().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)

    @pytest.mark.parametrize("old_from_date,old_to_date,old_type,old_reason,reason,expectedResult",edit_leave_data.get_edit_leave_data("Sheet6"))
    def test_change_special_reason_to_maternity(self,old_from_date,old_to_date,old_type,old_reason,reason,expectedResult):
        test_file_name="test_edit_leave"
        logger=self.getLogger(test_file_name)
        

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automation.three@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("HXo5YeKWPB4ePYoB")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)

        while True:
            try:
                leaveManagementPage.click_on_edit(old_from_date,old_to_date,old_type,old_reason).click()
                break
            except:
                leaveManagementPage.get_next_page().click()
        leaveManagementPage.get_reason_for_leave().click()
        logger.info("Clicking Reason Dropdown")

        leaveManagementPage.select_reason_for_leave(reason).click()
        logger.info("Selected Reason")
        specialToDate=leaveManagementPage.get_specialToDate()
        logger.info(specialToDate)
        specialfromDate=leaveManagementPage.get_specialFromDate()
        date_format = "%d/%m/%Y"
        # Convert strings to datetime objects
        convert_from_date = datetime.strptime(specialfromDate, date_format)
        convert_to_date = datetime.strptime(specialToDate, date_format)
        # Calculate the difference in days
        difference = convert_to_date-convert_from_date
        number_of_days = difference.days + 1  # Adding 1 to include both the start and end dates
                    
        
        if(float(leaveManagementPage.get_applied_leave_balance())!=number_of_days):
            logger.error("The number of days between the from date and to date is not equal to 182")
            assert False

        leaveManagementPage.get_confirm_edit().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)

    @pytest.mark.parametrize("old_from_date,old_to_date,old_type,old_reason,reason,expectedResult",edit_leave_data.get_edit_leave_data("Sheet7"))
    def test_change_special_reason_to_paternity(self,old_from_date,old_to_date,old_type,old_reason,reason,expectedResult):
        test_file_name="test_edit_leave"
        logger=self.getLogger(test_file_name)
        

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automation.three@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("HXo5YeKWPB4ePYoB")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)

        while True:
            try:
                leaveManagementPage.click_on_edit(old_from_date,old_to_date,old_type,old_reason).click()
                break
            except:
                leaveManagementPage.get_next_page().click()
        leaveManagementPage.get_reason_for_leave().click()
        logger.info("Clicking Reason Dropdown")

        leaveManagementPage.select_reason_for_leave(reason).click()
        logger.info("Selected Reason")

        specialToDate=leaveManagementPage.get_specialToDate()
        logger.info(specialToDate)
        specialfromDate=leaveManagementPage.get_specialFromDate()
        date_format = "%d/%m/%Y"
        # Convert strings to datetime objects
        convert_from_date = datetime.strptime(specialfromDate, date_format)
        convert_to_date = datetime.strptime(specialToDate, date_format)
        # Calculate the difference in days
        difference = convert_to_date-convert_from_date
        number_of_days = difference.days + 1  # Adding 1 to include both the start and end dates
                    
        
        if(float(leaveManagementPage.get_applied_leave_balance())!=number_of_days):
            logger.error("The number of days between the from date and to date is not equal to 5")
            assert False

        leaveManagementPage.get_confirm_edit().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)


    @pytest.mark.parametrize("old_from_date,old_to_date,old_type,old_reason,reason,expectedResult",edit_leave_data.get_edit_leave_data("Sheet8"))
    def test_change_special_reason_to_miscarriage(self,old_from_date,old_to_date,old_type,old_reason,reason,expectedResult):
        test_file_name="test_edit_leave"
        logger=self.getLogger(test_file_name)
        

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automation.three@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("HXo5YeKWPB4ePYoB")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)

        while True:
            try:
                leaveManagementPage.click_on_edit(old_from_date,old_to_date,old_type,old_reason).click()
                break
            except:
                leaveManagementPage.get_next_page().click()
        leaveManagementPage.get_reason_for_leave().click()
        logger.info("Clicking Reason Dropdown")

        leaveManagementPage.select_reason_for_leave(reason).click()
        logger.info("Selected Reason")

        specialToDate=leaveManagementPage.get_specialToDate()
        logger.info(specialToDate)
        specialfromDate=leaveManagementPage.get_specialFromDate()
        date_format = "%d/%m/%Y"
        # Convert strings to datetime objects
        convert_from_date = datetime.strptime(specialfromDate, date_format)
        convert_to_date = datetime.strptime(specialToDate, date_format)
        # Calculate the difference in days
        difference = convert_to_date-convert_from_date
        number_of_days = difference.days + 1  # Adding 1 to include both the start and end dates
                    
        
        if(float(leaveManagementPage.get_applied_leave_balance())!=number_of_days):
            logger.error("The number of days between the from date and to date is not equal to 42")
            assert False

        leaveManagementPage.get_confirm_edit().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)

    @pytest.mark.parametrize("old_from_date,old_to_date,old_type,old_reason,reason,expectedResult",edit_leave_data.get_edit_leave_data("Sheet9"))
    def test_change_special_reason_to_tubectomy(self,old_from_date,old_to_date,old_type,old_reason,reason,expectedResult):
        test_file_name="test_edit_leave"
        logger=self.getLogger(test_file_name)
        

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automation.three@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("HXo5YeKWPB4ePYoB")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)

        while True:
            try:
                leaveManagementPage.click_on_edit(old_from_date,old_to_date,old_type,old_reason).click()
                break
            except:
                leaveManagementPage.get_next_page().click()
        leaveManagementPage.get_reason_for_leave().click()
        logger.info("Clicking Reason Dropdown")

        leaveManagementPage.select_reason_for_leave(reason).click()
        logger.info("Selected Reason")

        specialToDate=leaveManagementPage.get_specialToDate()
        logger.info(specialToDate)
        specialfromDate=leaveManagementPage.get_specialFromDate()
        date_format = "%d/%m/%Y"
        # Convert strings to datetime objects
        convert_from_date = datetime.strptime(specialfromDate, date_format)
        convert_to_date = datetime.strptime(specialToDate, date_format)
        # Calculate the difference in days
        difference = convert_to_date-convert_from_date
        number_of_days = difference.days + 1  # Adding 1 to include both the start and end dates
                    
        
        if(float(leaveManagementPage.get_applied_leave_balance())!=number_of_days):
            logger.error("The number of days between the from date and to date is not equal to 14")
            assert False

        leaveManagementPage.get_confirm_edit().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)

    @pytest.mark.parametrize("old_from_date,old_to_date,old_type,old_reason,attachmentPath,expectedResult",edit_leave_data.get_edit_leave_data("Sheet10"))
    def test_edit_special_attachment(self,old_from_date,old_to_date,old_type,old_reason,attachmentPath,expectedResult):
        test_file_name="test_edit_leave"
        logger=self.getLogger(test_file_name)
        

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automation.three@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("HXo5YeKWPB4ePYoB")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)

        while True:
            try:
                leaveManagementPage.click_on_edit(old_from_date,old_to_date,old_type,old_reason).click()
                break
            except:
                leaveManagementPage.get_next_page().click()
        leaveManagementPage.get_delete_button().click()
        leaveManagementPage.click_confirm_delete()
        leaveManagementPage.get_file_element().send_keys(attachmentPath)
        logger.info("Uploaded the File")

        #validations

        leaveManagementPage.get_confirm_edit().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)
    
    @pytest.mark.parametrize("old_from_date,old_to_date,old_type,old_reason,reason,fromDate,toDate,expectedResult",edit_leave_data.get_edit_leave_data("Sheet11"))
    def test_change_leave_type_to_consolidated(self,old_from_date,old_to_date,old_type,old_reason,reason,fromDate,toDate,expectedResult):
        #no partial leaves
        test_file_name="test_edit_leave"
        logger=self.getLogger(test_file_name)
        

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automation.three@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("HXo5YeKWPB4ePYoB")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)

        while True:
            try:
                leaveManagementPage.click_on_edit(old_from_date,old_to_date,old_type,old_reason).click()
                break
            except:
                leaveManagementPage.get_next_page().click()
        leaveManagementPage.get_consolidated_leave_button().click()
        logger.info("Clicked on Consolidate tab")

        leaveManagementPage.get_reason_for_leave().click()
        logger.info("Clicking Reason Dropdown")

        leaveManagementPage.select_reason_for_leave(reason).click()
        logger.info("Selected Reason")

        leaveManagementPage.get_from_date().click()

        from_date=fromDate.strftime("%d/%m/%Y").split('/')
        to_date=toDate.strftime("%d/%m/%Y").split('/')
        
        Select_year = Select(leaveManagementPage.select_year())

        Select_year.select_by_value(str(from_date[2]))
        logger.info("Selected the from Year")

        Select_month = Select(leaveManagementPage.select_month())
        
        Select_month.select_by_value(str(int(from_date[1])))
        logger.info("Selected the from Month")

        leaveManagementPage.select_date(str(int(from_date[0]))).click()
        logger.info("Selected the from date")

        leaveManagementPage.get_to_date().click()

        Select_year = Select(leaveManagementPage.select_year())

        Select_year.select_by_value(str(to_date[2]))
        logger.info("Selected the to Year")

        Select_month = Select(leaveManagementPage.select_month())
        
        Select_month.select_by_value(str(int(to_date[1])))
        logger.info("Selected the to Month")

        leaveManagementPage.select_date(str(int(to_date[0]))).click()
        logger.info("Selected the to date")
        
        Available_leave=float(leaveManagementPage.get_available_leave_balance())
        Applied_leave=float(leaveManagementPage.get_applied_leave_balance())
        Loss_of_pay=float(leaveManagementPage.get_loss_of_pay())
        logger.info("Available is checking")
        if Applied_leave>Available_leave:
            if Loss_of_pay==(Applied_leave-Available_leave):
                logger.info('Loss of pay is equal to difference in Applied and Available Leave')
            else:
                logger.error('Loss of pay is incorrect')
                assert False
        if Loss_of_pay>0:
            leaveManagementPage.get_proceed_button().click()
            logger.info("Clicked on Proceed")
        leaveManagementPage.get_confirm_edit().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)


    @pytest.mark.parametrize("old_from_date,old_to_date,old_type,old_reason,reason,fromDate,attachmentPath,expectedResult",edit_leave_data.get_edit_leave_data("Sheet12"))
    def test_change_leave_type_to_special(self,old_from_date,old_to_date,old_type,old_reason,reason,fromDate,attachmentPath,expectedResult):
        test_file_name="test_edit_leave"
        logger=self.getLogger(test_file_name)
        

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automation.three@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("HXo5YeKWPB4ePYoB")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)

        while True:
            try:
                leaveManagementPage.click_on_edit(old_from_date,old_to_date,old_type,old_reason).click()
                break
            except:
                leaveManagementPage.get_next_page().click()
        leaveManagementPage.get_special_leave_button().click()
        leaveManagementPage.get_reason_for_leave().click()
        logger.info("Clicking Reason Dropdown")

        leaveManagementPage.select_reason_for_leave(reason).click()
        logger.info("Selected Reason")

        leaveManagementPage.get_from_date().click()

        from_date=fromDate.strftime("%d/%m/%Y").split('/')
        
        Select_year = Select(leaveManagementPage.select_year())

        Select_year.select_by_value(str(from_date[2]))
        logger.info("Selected the from Year")

        Select_month = Select(leaveManagementPage.select_month())
        
        Select_month.select_by_value(str(int(from_date[1])))
        logger.info("Selected the from Month")
        
        logger.info(str(from_date[0]))
        leaveManagementPage.select_date(str(int(from_date[0]))).click()
        logger.info("Selected the from date")


        leaveManagementPage.get_file_element().send_keys(attachmentPath)
        logger.info("Uploaded the File")
        leaveManagementPage.get_confirm_edit().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)

    @pytest.mark.test1
    @pytest.mark.parametrize("old_from_date,old_to_date,old_type,old_reason,fromDate,toDate,expectedResult",edit_leave_data.get_edit_leave_data("Sheet13"))
    def test_change_dates_with_loss_of_pay_without_proceed(self,old_from_date,old_to_date,old_type,old_reason,fromDate,toDate,expectedResult):
        #consolidated
        test_file_name="test_edit_leave"
        logger=self.getLogger(test_file_name)
        

        loginPage=LoginPage(self.driver)

        loginPage.get_user_name().send_keys("automation.three@braneenterprises.com")
        logger.info('Entered Username')

        loginPage.get_password().send_keys("HXo5YeKWPB4ePYoB")
        logger.info('Entered Password')

        dceoLandingPage=loginPage.login()
        logger.info('Logged in ')

        dceoLandingPage.get_arrowButton().click()
        logger.info('Clicked on Hamburger')

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)

        while True:
            try:
                leaveManagementPage.click_on_edit(old_from_date,old_to_date,old_type,old_reason).click()
                break
            except:
                leaveManagementPage.get_next_page().click()

        leaveManagementPage.get_from_date().click()

        from_date=fromDate.strftime("%d/%m/%Y").split('/')
        to_date=toDate.strftime("%d/%m/%Y").split('/')
        
        Select_year = Select(leaveManagementPage.select_year())

        Select_year.select_by_value(str(from_date[2]))
        logger.info("Selected the from Year")

        Select_month = Select(leaveManagementPage.select_month())
        
        Select_month.select_by_value(str(int(from_date[1])))
        logger.info("Selected the from Month")

        leaveManagementPage.select_date(str(int(from_date[0]))).click()
        logger.info("Selected the from date")

        leaveManagementPage.get_to_date().click()

        Select_year = Select(leaveManagementPage.select_year())

        Select_year.select_by_value(str(to_date[2]))
        logger.info("Selected the to Year")

        Select_month = Select(leaveManagementPage.select_month())
        
        Select_month.select_by_value(str(int(to_date[1])))
        logger.info("Selected the to Month")

        leaveManagementPage.select_date(str(int(to_date[0]))).click()
        logger.info("Selected the to date")
        Available_leave=float(leaveManagementPage.get_available_leave_balance())
        Applied_leave=float(leaveManagementPage.get_applied_leave_balance())
        Loss_of_pay=float(leaveManagementPage.get_loss_of_pay())
        logger.info("Available is checking")
        if Applied_leave>Available_leave:
            if Loss_of_pay==(Applied_leave-Available_leave):
                logger.info('Loss of pay is equal to difference in Applied and Available Leave')
            else:
                logger.error('Loss of pay is incorrect')
                assert False
        if Loss_of_pay>0:
            leaveManagementPage.get_confirm_edit().click()
            logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)





        
        



        
            
