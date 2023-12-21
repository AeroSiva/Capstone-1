import pytest
from Pages.login_page import Login_page_cls
from Excel_Functions.excel_functions import Excel_Functions
from Data.data import OrangeHrm_data


@pytest.mark.usefixtures("setup")
class Test_login_logout:

     #TC_LOGIN_01,TC_LOGIN_02
     @pytest.mark.parametrize("username, password, row, exp_result", Excel_Functions
                         (OrangeHrm_data.excel_file_name,OrangeHrm_data.excel_sheet_name).read_excel_login_test_detail_util())
     def test_login(self,username, password, row, exp_result):
          try:
               lp = Login_page_cls(self.driver,self.wait)
               act_res = lp.tc_login(username, password, row, exp_result)
               assert act_res==exp_result
               print("Login test run successfully.")  
          except Exception as e:
               print("TC_Login_01/02 :  test_login failed : ",e)


     # TC_PIM_01     
     @pytest.mark.parametrize("username, password, row, exp_result,emp_id_da, employee_fname_da, employee_lname_da, \
          employee_user_name, employee_password, nick_name_da, other_id_da,driver_lic_da, lic_exp_da, ssn_da, sin_da,\
          dob_da, mili_ser_da", Excel_Functions("Capstone_1.xlsx","Sheet2").fetch_test_details_pim_01())
     def test_add_employee(self,username, password, row, exp_result,emp_id_da, employee_fname_da, employee_lname_da, \
          employee_user_name, employee_password, nick_name_da, other_id_da,driver_lic_da, lic_exp_da, ssn_da, sin_da, \
          dob_da, mili_ser_da):
          
          try:
               lp = Login_page_cls(self.driver, self.wait)
               
               lp.login_orangehrm(username, password)
               print("Step 1 :Logged in ")
               # Navigated to Dashboard page
               
               lp.click_pim()
               print("Step 2 : Clicked pim")
               # Navigated to Pim page
               
               lp.click_add()
               print("Step 3 : Clicked Add")
               # Navigated to add employee page
               
               lp.add_employee_details(emp_id_da,employee_fname_da, employee_lname_da, employee_user_name,employee_password)
               print("Step 4 : An Employee details are added")
               # Navigated to Personal details page
               
               actual_result_op = lp.tc_add_employee(row, exp_result, nick_name_da, other_id_da, driver_lic_da, lic_exp_da, ssn_da, sin_da, dob_da,mili_ser_da)
               print("Step 5 : TC_PIM_01 runned")
               lp.logout_Orangehrm()
               print("Step 6 ; Logged out successfully ")
               # Navigated to login page
               
               assert actual_result_op == exp_result
               print("Add employee test runned succesfully")    
          except Exception as e:
               print("Error : Tc_PIM_01 :test_add_employee failed : ",e)     

     
     # TC_PIM_02
     @pytest.mark.parametrize("username, password, row, exp_result,emp_id_da, employee_fname_da, employee_lname_da, \
          employee_user_name, employee_password, nick_name_da, other_id_da,driver_lic_da, lic_exp_da, ssn_da, \
          sin_da, dob_da, mili_ser_da,edited_fname_da, edited_nationality_da, edited_blood_type_da", \
               Excel_Functions("Capstone_1.xlsx","Sheet3").fetch_test_details_pim_02())
     def test_edit_employee_details(self,username, password, row, exp_result,emp_id_da, employee_fname_da, employee_lname_da, \
          employee_user_name, employee_password, nick_name_da, other_id_da,driver_lic_da, lic_exp_da, ssn_da, \
          sin_da, dob_da, mili_ser_da, edited_fname_da, edited_nationality_da, edited_blood_type_da):
         
          try:
               lp = Login_page_cls(self.driver, self.wait)
               lp.login_orangehrm(username, password)
               print("Step 1 :Logged in ")
               # Navigated to Dashboard page
               
               lp.click_pim()
               print("Step 2 : Clicked pim")
               # Navigated to Pim page
               
               lp.click_add()
               print("Step 3 : Clicked Add")
               # Navigated to add employee page
               
               lp.add_employee_details(emp_id_da,employee_fname_da, employee_lname_da, employee_user_name,employee_password)
               print("Step 4 : An Employee details are added")
               # Navigated to Personal details page
               
               lp.fill_personal_detail(row,exp_result,nick_name_da, other_id_da, driver_lic_da, lic_exp_da, ssn_da, sin_da, dob_da,mili_ser_da)
               print("Step 5 : Filled personal details")
               # Editing employee details
               actual_result = lp.tc_edit_employee(row,exp_result,edited_fname_da,edited_nationality_da ,edited_blood_type_da)
               print("Step 6 : TC_PIM_02 runned Successfully")
               # Navigated to login page
               
               lp.logout_Orangehrm()
               print("Step 7 : Logged out Successfully")
               assert actual_result == exp_result
          except Exception as e:
               print("Error : TC_PIM_02 :  test_edit_employee_details failed : ",e)

     
     # TC_PIM_03
     @pytest.mark.parametrize("username, password, row, exp_result, emp_id_da, employee_fname_da, employee_lname_da, \
          employee_user_name, employee_password, nick_name_da, other_id_da,driver_lic_da, lic_exp_da, ssn_da, \
          sin_da, dob_da, mili_ser_da", Excel_Functions("Capstone_1.xlsx","Sheet4").fetch_test_details_pim_03())
     def test_delete_employee_details(self,username, password, row, exp_result,emp_id_da, employee_fname_da, employee_lname_da, \
          employee_user_name, employee_password, nick_name_da, other_id_da,driver_lic_da, lic_exp_da, ssn_da, \
          sin_da, dob_da, mili_ser_da):
          
          try:
               lp= Login_page_cls(self.driver,self.wait)
               lp.login_orangehrm(username, password)
               print("Step 1 :Logged in ")
               # Navigated to Dashboard page
               
               lp.click_pim()
               print("Step 2 : Clicked pim")
               # Navigated to Pim page
               
               lp.click_add()
               print("Step 3 : Clicked Add")
               # Navigated to add employee page
               
               lp.add_employee_details(emp_id_da,employee_fname_da, employee_lname_da, employee_user_name,employee_password)
               print("Step 4 : An Employee details are added")
               # Navigated to Personal details page
               
               lp.fill_personal_detail(row,exp_result,nick_name_da, other_id_da, driver_lic_da, lic_exp_da, ssn_da, sin_da, dob_da,mili_ser_da)
               print("Step 5 : Filled personal details")
               # Navigated to Personal details page
               
               lp.click_pim()
               print("Step 6 : Clicked pim")
               # Navigated to Pim page
               
               # Deleting employee details
               actual_result = lp.tc_delete_employee(row,exp_result,emp_id_da)
               print("Step 7 : TC_PIM_03 runned successfully")
               
               lp.logout_Orangehrm()
               print("Step 8 : Logged out successfully")
               assert actual_result == exp_result
          except Exception as e:
               print("Error : TC_PIM_03 :  test_edit_employee_details failed : ",e)
