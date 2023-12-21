from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
import time
from Locators.locators import Orangehrm_locators
from Data.data import OrangeHrm_data
from Utils.util import Util

class Add_employee_cls:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def add_employee_details(self,emp_id_da,employee_fname_da,employee_lname_da,employee_user_name,employee_password,):
        try:
            employee_fname = self.wait.until(EC.element_to_be_clickable((By.NAME,Orangehrm_locators().first_name_name)))
            employee_fname.send_keys(employee_fname_da)
            
            employee_lname = self.wait.until(EC.element_to_be_clickable((By.NAME,Orangehrm_locators().last_name_name)))
            employee_lname.send_keys(employee_lname_da)
            
            emp_id = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators().employee_id_xpath)))
            while emp_id.get_attribute("value"):
                emp_id.send_keys(Keys.BACKSPACE)
            emp_id.send_keys(emp_id_da)
            
            try:
                create_login_details_switch = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,Orangehrm_locators().create_login_details_css)))
                self.driver.execute_script("arguments[0].click();", create_login_details_switch)

                emp_username_ip = self.wait.until(EC.visibility_of_element_located((By.XPATH,Orangehrm_locators().username_ip_cre_login_xpath)))
                emp_username_ip.send_keys(employee_user_name)
                emp_password_ip = self.wait.until(EC.visibility_of_element_located((By.XPATH,Orangehrm_locators().password_ip_cre_login_xpath)))
                emp_password_ip.send_keys(employee_password)
                emp_cpassword_ip = self.wait.until(EC.visibility_of_element_located((By.XPATH,Orangehrm_locators().confirm_password_ip_cre_login_xpath)))
                emp_cpassword_ip.send_keys(employee_password)
                
                # Wait for the loader to disappear
                loader_disappear = self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'oxd-form-loader')))
                
                save_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators().save_button_xpath)))
                save_btn.click()
                Util.wait_for_url_change(self,OrangeHrm_data().add_employee_url)
            
            except Exception as e:
                print("clicking create login button failure : ",e)
        except Exception as e:
            print("Error : Add employeee account in Add employee page failed : ",e)