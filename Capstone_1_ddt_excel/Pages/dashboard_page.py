from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import Orangehrm_locators
from Data.data import OrangeHrm_data
from Utils.util import Util


class Dashboard_cls:

    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def click_pim(self):
        try:
            pim_element = self.wait.until(EC.element_to_be_clickable((By.XPATH,Orangehrm_locators().PIM_module_xpath)))
            pim_element.click()
            Util.wait_for_url_change(self,OrangeHrm_data().loggedin_url,timeout=4)
        except Exception as e:
            print("Clicking Pim error : ", e)