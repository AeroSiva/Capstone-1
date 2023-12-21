from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import time
from Data.data import OrangeHrm_data
from Excel_Functions.excel_functions import Excel_Functions
from Utils.util import Util
from Locators.locators import Orangehrm_locators
from Pages.dashboard_page import Dashboard_cls
from Pages.pim_page import Pim_cls
from Pages.add_emp_page import Add_employee_cls
from Pages.personal_detail_page import Personal_detail


class Login_page_cls(Orangehrm_locators,OrangeHrm_data,Util,Dashboard_cls,Pim_cls,Add_employee_cls,Personal_detail):
    def __init__(self,driver,wait):
        super().__init__(driver,wait)
        self.driver = driver
        self.wait = wait
        self.action = ActionChains(self.driver)
        self.date = datetime.datetime.now()
        self.excel_func = Excel_Functions(OrangeHrm_data().excel_file_name, OrangeHrm_data().excel_sheet_name)
        self.row = self.excel_func.row_count()
    
    
    # Login test case for valid and invalid username and password 
    def tc_login(self,username,password,row,expected_result):
            print("Test case for Login running")
            try:
                Util.login_orangehrm(self,username,password)
            except Exception as e:
                print("login error in login)Orangehrm",e)

            actual_result = ''
            # This method checks for any change in url if url doesn' change return False
            try:
                page_load = self.wait_for_url_change(old_url=OrangeHrm_data.login_url)
                if page_load:
                    actual_result = "The user is Logged in successfully"
                    Util.logout_Orangehrm(self)
                    Util.wait_for_url_change(self,old_url=OrangeHrm_data.loggedin_url)
                    print("logged out successfully")
                else:
                    alert_element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,Orangehrm_locators.invalid_login_alert_css)))
                    actual_result = alert_element.text
                print("Actual result",actual_result)
            except Exception as e:
                print("Defining page load error : ",e )
    
            try:
                Util.write_date_time_actual_result_in_excel(self,row,actual_result)
            except Exception as e:
                print("write in excel error : ",e )

            try:
                Util.write_test_pass_fail_in_excel(self,row,actual_result,expected_result)
            except Exception as e:
                print("Checking actual result against expected and wrinting whether test pass or fail failed: ",e)
            
            return actual_result
   