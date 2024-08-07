from pageObjects.LoginPage import LoginPage
from pageObjects.MyselfPage import MyselfPage
from pageObjects.LeaveManagementPage import LeaveManagementPage
from ..TestScripts.BaseClass import BaseClass
from selenium.webdriver.support.ui import WebDriverWait,Select
from TestData.apply_leave_data import apply_leave_data
import pytest
import datetime,time
from datetime import datetime, timedelta

class Test_apply_leave(BaseClass):
    
    @pytest.mark.smoke
    @pytest.mark.parametrize("reason,fromDate,toDate,expectedResult",apply_leave_data.get_edit_leave_data("Sheet1"))
    def test_consolidated_valid_date_valid_reason(self,reason,fromDate,toDate,expectedResult):
        test_file_name="test_consolidated_valid_date_valid_reason"
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

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)
        leaveManagementPage.get_apply_leave_button().click()
        logger.info("Clicked on Apply Leave Button")

        
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
                return None
        if Loss_of_pay>0:
            leaveManagementPage.get_proceed_button().click()
            logger.info("Clicked on Proceed")
        leaveManagementPage.get_submit_button().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)

    @pytest.mark.smoke
    @pytest.mark.parametrize("reason,fromDate,toDate,expectedResult",apply_leave_data.get_edit_leave_data("Sheet2"))
    def test_overlapping_dates(self,reason,fromDate,toDate,expectedResult):
        test_file_name="test_overlapping_dates"
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

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)
        leaveManagementPage.get_apply_leave_button().click()
        logger.info("Clicked on Apply Leave Button")

        
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
                return None
        if Loss_of_pay>0:
            leaveManagementPage.get_proceed_button().click()
            logger.info("Clicked on Proceed")
        leaveManagementPage.get_submit_button().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)

    @pytest.mark.smoke
    @pytest.mark.parametrize("reason",apply_leave_data.get_edit_leave_data("Sheet3"))
    def test_consolidated_invalid_reason(self,reason):
        test_file_name="test_consolidated_valid_date_invalid_reason"
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

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)
        leaveManagementPage.get_apply_leave_button().click()
        logger.info("Clicked on Apply Leave Button")

        
        leaveManagementPage.get_consolidated_leave_button().click()
        logger.info("Clicked on Consolidate tab")

        leaveManagementPage.get_reason_for_leave().click()
        logger.info("Clicking Reason Dropdown")

        try:
            leaveManagementPage.select_reason_for_leave(reason).click()
            logger.error("Selected the reason")
        except:
            logger.info("Not found the reason")
            assert True
            return None
        assert False


    @pytest.mark.smoke
    @pytest.mark.partial
    @pytest.mark.parametrize("reason,fromDate,toDate,partialDates,expectedResult",apply_leave_data.get_edit_leave_data("Sheet4"))
    def test_consolidated_valid_date_partials(self,reason,fromDate,toDate,partialDates,expectedResult):
        test_file_name="test_consolidated_valid_date_partials"
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

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)
        leaveManagementPage.get_apply_leave_button().click()
        logger.info("Clicked on Apply Leave Button")

        
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
        
        result_list = [[int(key), value] for key, value in (pair.split(':') for pair in str(partialDates).split(','))]


        if partialDates is not None:
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
        leaveManagementPage.get_submit_button().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)
    

    @pytest.mark.smoke
    @pytest.mark.parametrize("reason,fromDate,toDate,expectedResult",apply_leave_data.get_edit_leave_data("Sheet5"))
    def test_consolidated_invalid_date(self,reason,fromDate,toDate,expectedResult):
        test_file_name="test_consolidated_invalid_date"
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

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)
        leaveManagementPage.get_apply_leave_button().click()
        logger.info("Clicked on Apply Leave Button")

        
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
        
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)

    @pytest.mark.withoutproceed
    @pytest.mark.parametrize("reason,fromDate,toDate,expectedResult",apply_leave_data.get_edit_leave_data("Sheet6"))
    def test_without_proceed(self,reason,fromDate,toDate,expectedResult):
        test_file_name="test_without proceed"
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

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)
        leaveManagementPage.get_apply_leave_button().click()
        logger.info("Clicked on Apply Leave Button")

        
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
    
        Loss_of_pay=float(leaveManagementPage.get_loss_of_pay())
        if Loss_of_pay>0:
            leaveManagementPage.get_submit_button().click()
            logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)


    @pytest.mark.regression
    @pytest.mark.parametrize("reason,fromDate,attachmentPath,expectedResult",apply_leave_data.get_edit_leave_data("Sheet7"))
    def test_maternity_special_valid_date_reason_days_check(self,reason,fromDate,attachmentPath,expectedResult):
        test_file_name="test_maternity_special_valid_date_reason_days_check"
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

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)
        leaveManagementPage.get_apply_leave_button().click()
        logger.info("Clicked on Apply Leave Button")

        
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
        time.sleep(4)
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
                    
        
        if(float(leaveManagementPage.get_applied_leave_balance())!=number_of_days):
            logger.error("The number of days between the from date and to date is not equal to 182")
            assert False
        
        #submit code
        leaveManagementPage.get_submit_button().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.parametrize("reason,fromDate,attachmentPath,expectedResult",apply_leave_data.get_edit_leave_data("Sheet8"))
    def test_paternity_special_valid_date_reason_days_check(self,reason,fromDate,attachmentPath,expectedResult):
        test_file_name="test_paternity_special_valid_date_reason_days_check"
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

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)
        leaveManagementPage.get_apply_leave_button().click()
        logger.info("Clicked on Apply Leave Button")

        
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
        time.sleep(4)
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
        if(float(leaveManagementPage.get_applied_leave_balance())!=number_of_days):
                logger.error("The number of days between the from date and to date is not equal to 5")
                assert False
        leaveManagementPage.get_submit_button().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)

    @pytest.mark.smoke
    @pytest.mark.parametrize("reason,fromDate,attachmentPath,expectedResult",apply_leave_data.get_edit_leave_data("Sheet9"))
    def test_tubectomy_special_valid_date_reason_days_check(self,reason,fromDate,attachmentPath,expectedResult):
        test_file_name="test_tubectomy_special_valid_date_reason_days_check"
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

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)
        leaveManagementPage.get_apply_leave_button().click()
        logger.info("Clicked on Apply Leave Button")

        
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
        time.sleep(4)
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
        if(float(leaveManagementPage.get_applied_leave_balance())!=number_of_days):
                logger.error("The number of days between the from date and to date is equal to 14")
                assert False
        leaveManagementPage.get_submit_button().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)


    @pytest.mark.regression
    @pytest.mark.parametrize("reason,fromDate,attachmentPath,expectedResult",apply_leave_data.get_edit_leave_data("Sheet10"))
    def test_miscarriage_special_valid_date_reason_days_check(self,reason,fromDate,attachmentPath,expectedResult):
        test_file_name="test_miscarriage_special_valid_date_reason_days_check"
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

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)
        leaveManagementPage.get_apply_leave_button().click()
        logger.info("Clicked on Apply Leave Button")

        
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
        time.sleep(4)
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
        if(float(leaveManagementPage.get_applied_leave_balance())!=number_of_days):
                logger.error("The number of days between the from date and to date is equal to 42")
                assert False
        leaveManagementPage.get_submit_button().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)

    @pytest.mark.ss
    @pytest.mark.parametrize("reason,expectedResult",apply_leave_data.get_edit_leave_data("Sheet11"))
    def test_special_no_from_date(self,reason,expectedResult):
        test_file_name="test_special_no_from_date"
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

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)
        leaveManagementPage.get_apply_leave_button().click()
        logger.info("Clicked on Apply Leave Button")

        
        leaveManagementPage.get_special_leave_button().click()
        leaveManagementPage.get_reason_for_leave().click()
        logger.info("Clicking Reason Dropdown")

        leaveManagementPage.select_reason_for_leave(reason).click()
        logger.info("Selected Reason")

        leaveManagementPage.get_submit_button().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)

    @pytest.mark.ss
    @pytest.mark.parametrize("reason,fromDate,expectedResult",apply_leave_data.get_edit_leave_data("Sheet12"))
    def test_special_no_attachment(self,reason,fromDate,expectedResult):
        test_file_name="test_special_no_attachment"
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

        dceoLandingPage.get_data("MySelf").click()
        logger.info("Clicked on Myself")

        MyselfPage(self.driver).get_leave_management().click()
        logger.info("Navigated to Leave Management")

        leaveManagementPage=LeaveManagementPage(self.driver)
        leaveManagementPage.get_apply_leave_button().click()
        logger.info("Clicked on Apply Leave Button")

        
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

        leaveManagementPage.get_submit_button().click()
        logger.info("Clicked on Submit")
        result=leaveManagementPage.get_toast()
        assert (expectedResult in result)


    

        




