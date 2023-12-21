from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import Orangehrm_locators
from Data.data import OrangeHrm_data
from Utils.util import Util

class Pim_cls:
    def __init__(self,driver):
        self.driver = driver

    # Clicking Add available in pim module page
    def click_add(self):
        try:
            add_element = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators().pim_add_xpah)))
            add_element.click()
            Util.wait_for_url_change(self,OrangeHrm_data().pim_url,timeout=4)
        except Exception as e:
            print("Error : Clicking Add on Pim module page failed : ", e)

    # Method to delete employee account
    def delete_employee_data(self,emp_id_da):
        try:
            id_ipe = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators().pim_employee_id_xpath)))
            id_ipe.send_keys(emp_id_da)

            search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators.search_button_xpath)))
            search_button.click()

            matched_id = self.wait.until(EC.presence_of_element_located((By.XPATH,Orangehrm_locators().id_record_es_xpath)))
            
            record_cbes = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators().select_record_cbes_xpath)))
            record_cbes.click()

            delete_selected_e = self.wait.until(EC.presence_of_element_located((By.XPATH,Orangehrm_locators().delete_selected_dye_xpath)))
            delete_selected_e.click()

            delete_alert_yes_e = self.wait.until(EC.presence_of_element_located((By.XPATH,Orangehrm_locators().delete_notifi_yes_btn_xpath)))
            delete_alert_yes_e.click()

            notification_text = Util.notification_text_from_dynamic_notification(self,By.XPATH,Orangehrm_locators().saved_invalid_notification,Orangehrm_locators().saved_or_invalid_not_add_ele)
            
            return notification_text
        except Exception as e:
            print("Error : Deleting the Employee account completely in PIM module page failed : ",e)

    # Test case written which call method to delete employee details and 
    # Write the test result in the excel sheet Sheet1 as well return test result to pytest page.
    def tc_delete_employee(self,row,exp_result,emp_id_da):
        try:
            notification_text = self.delete_employee_data(emp_id_da)
            print("Delete Employee detail detail : ",notification_text)
            
            actual_result = notification_text
            
            try:
                Util.write_date_time_actual_result_in_excel(self,row,actual_result)

                Util.write_test_pass_fail_in_excel(self,row,actual_result,exp_result)
                    
            except Exception as e:
                print("Error : getting text from dynamic notification for saved or invalid parameter error")

            return actual_result
        except Exception as e:
            print("Errpr tc_delete_employee method failed : ",e)