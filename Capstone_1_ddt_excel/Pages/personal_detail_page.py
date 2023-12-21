from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import Orangehrm_locators
from selenium.webdriver.common.keys import Keys
from Utils.util import Util


class Personal_detail:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def fill_personal_detail(self,row,exp_result,nick_name_da,other_id_da,driver_lic_da,lic_exp_da,ssn_da,sin_da,dob_da,mili_ser_da):
        try:
            #time.sleep(4)
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, Orangehrm_locators.per_cus_field_save_btn_xpath)))
            nick_name = self.wait.until(EC.visibility_of_element_located((By.XPATH,Orangehrm_locators().per_nick_name_xpath)))
            nick_name.send_keys(nick_name_da)
            print("nick name given")

            other_id = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators().per_other_id__ip_xpath)))
            other_id.send_keys(other_id_da)
            print("Other id detail send")

            driver_lic = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators().per_driver_lic_ip_xpath)))
            driver_lic.send_keys(driver_lic_da)
            print("Driver license detail given")
            #time.sleep(4)

            lic_exp_cip = self.wait.until(EC.visibility_of_element_located((By.XPATH,Orangehrm_locators().per_lic_exp_dat_cip_xpath)))
            self.driver.execute_script(f"arguments[0].value = '{lic_exp_da}';", lic_exp_cip)
            print("Lic expirary filled")


            ssn_cipe = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators().per_ssn_n_ip_xpath)))
            ssn_cipe.send_keys(ssn_da)
            sin_cipe = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators().per_sin_n_ip_xpath)))
            sin_cipe.send_keys(sin_da)

            try:
                # Wait for the loader to disappear
                loader_disappear = self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'oxd-form-loader')))
            except Exception as e:
                print("loader not obsured")

            nationality_dde = self.wait.until(EC.visibility_of_element_located((By.XPATH,Orangehrm_locators().per_nationality_dd_xpath)))
            nationality_dde.click()
            print("Nationality detail given")

            self.driver.execute_script("window.scrollBy(0, 420);")
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH,Orangehrm_locators().per_nationality_dyop_xpath)))
            nationality_dyop_afgha =self.wait.until(EC.presence_of_element_located((By.XPATH,Orangehrm_locators().per_nationality_dyop_afgha_xpath)))
            nationality_dyop_afgha.click()
            marital_status_dde = self.wait.until(EC.visibility_of_element_located((By.XPATH,Orangehrm_locators().per_martial_status_dd_xpath)))
            marital_status_dde.click()

            self.wait.until(EC.presence_of_all_elements_located((By.XPATH,Orangehrm_locators().per_martial_status_dop_xpath)))
            marital_status_dop_single = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators().per_martial_status_dop_single_xpath)))
            marital_status_dop_single.click()

            dob_cipe = self.wait.until(EC.visibility_of_element_located((By.XPATH,Orangehrm_locators().per_dob_ip_xpath)))
            self.driver.execute_script(f"arguments[0].value = '{dob_da}';", dob_cipe)
            print("DOB filled")

            gender_rd_male = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators().per_gender_rd_xpath)))
            gender_rd_male.click()

            mili_ser_ipe = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators().per_military_ser_ip_xpath)))
            mili_ser_ipe.send_keys(mili_ser_da)

            personal_dat_save_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators().per_per_det_save_btn_xpath)))
            personal_dat_save_btn.click()

            blood_type_dde = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators().per_blood_type_dd_xpath)))
            blood_type_dde.click()

            blood_type_ap_ope = self.wait.until(EC.presence_of_element_located((By.XPATH,Orangehrm_locators().per_blood_type_ap_xpath)))
            blood_type_ap_ope.click()

            custom_field_save_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators().per_cus_field_save_btn_xpath)))
            custom_field_save_btn.click()

            notification_text = Util.notification_text_from_dynamic_notification(self,By.XPATH,Orangehrm_locators().saved_invalid_notification,Orangehrm_locators().saved_or_invalid_not_add_ele)
        
            return notification_text
        
        except Exception as e:
            print("Filleing personal details failed : ",e)
        
    def edit_personal_details(self,edited_fname_da,edited_nationality_da ,edited_blood_type_da):
        try:
            # Give wait for the page to load and therbythat time javascript functions also gets loaded
            waiter_for_pg_to_load = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, Orangehrm_locators.per_cus_field_save_btn_xpath)))
            
            employee_fname = self.wait.until(EC.element_to_be_clickable((By.NAME,Orangehrm_locators().first_name_name)))
            # Use a loop to check and clear the input field until it's empty
            # Use Backspace to clear the input field
            while employee_fname.get_attribute("value"):
                employee_fname.send_keys(Keys.BACKSPACE)
            employee_fname.send_keys(edited_fname_da)
            print("Name is edited to new spelling : ShivaC")
            edited_name = employee_fname.get_attribute("value")
            
            loader_disappear = self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'oxd-form-loader')))
            nationality_dde = self.wait.until(EC.visibility_of_element_located((By.XPATH,Orangehrm_locators().per_nationality_dd_xpath)))
            nationality_dde.click()
            print("Nationality dd snipe")
            self.driver.execute_script("window.scrollBy(0, 420);")
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH,Orangehrm_locators().per_nationality_dyop_xpath)))
            nationality_dyop_indie =self.wait.until(EC.presence_of_element_located((By.XPATH,Orangehrm_locators().per_nationality_dyop_indi_xpath)))
            nationality_dyop_indie.click()
            nationality_input = self.wait.until(EC.visibility_of_element_located((By.XPATH,Orangehrm_locators().per_nationality_ipv_xpath)))
            edited_nationality = nationality_input.text
            print(edited_nationality)

            personal_dat_save_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators().per_per_det_save_btn_xpath)))
            personal_dat_save_btn.click()

            blood_type_dde = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators().per_blood_type_dd_xpath)))
            blood_type_dde.click()
            blood_type_op_ope = self.wait.until(EC.presence_of_element_located((By.XPATH,Orangehrm_locators().per_blood_type_op_xpath)))
            blood_type_op_ope.click()
            blood_type_ip = self.wait.until(EC.visibility_of_element_located((By.XPATH,Orangehrm_locators().per_blood_type_it_xpath)))
            edited_blood_type = blood_type_ip.text

            custom_field_save_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators().per_cus_field_save_btn_xpath)))
            custom_field_save_btn.click()

            assert edited_name == edited_fname_da
            assert edited_nationality == edited_nationality_da
            assert edited_blood_type == edited_blood_type_da

            notification_text = Util.notification_text_from_dynamic_notification(self,By.XPATH,Orangehrm_locators().saved_invalid_notification,Orangehrm_locators().saved_or_invalid_not_add_ele)
        
            return notification_text


        
        except Exception as e:
            print("Editing Personal details failed",e)



    def tc_add_employee(self,row,exp_result,nick_name_da,other_id_da,driver_lic_da,lic_exp_da,ssn_da,sin_da,dob_da,mili_ser_da):
        
        try:
            print("Test case to add employee running")
            # Fill personal detail initiated
            notification_text = self.fill_personal_detail(row,exp_result,nick_name_da,
                                        other_id_da,driver_lic_da,lic_exp_da,ssn_da,sin_da,dob_da,mili_ser_da)
            print("Saved Personal detail : ",notification_text)
            actual_result = notification_text
            
            try:
                Util.write_date_time_actual_result_in_excel(self,row,actual_result)

                Util.write_test_pass_fail_in_excel(self,row,actual_result,exp_result)
                    
            except Exception as e:
                print("Error : getting text from dynamic notification for saved or invalid parameter error")

            return actual_result
        except Exception as e:
            print("Error : tc_add_employee failed : ",e)    

    def tc_edit_employee(self,row,exp_result,edited_fname_da,edited_nationality_da ,edited_blood_type_da):

        try:
            notification_text = self.edit_personal_details(edited_fname_da,edited_nationality_da ,edited_blood_type_da)

            print("Saved Personal detail : ",notification_text)
            actual_result = notification_text
            
            try:
                Util.write_date_time_actual_result_in_excel(self,row,actual_result)

                Util.write_test_pass_fail_in_excel(self,row,actual_result,exp_result)
                    
            except Exception as e:
                print("Error : getting text from dynamic notification for saved or invalid parameter error")

            return actual_result
        except Exception as e:
            print("Error : tc_edit_employee method failed : ",e)    