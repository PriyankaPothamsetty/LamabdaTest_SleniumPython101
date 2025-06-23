from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utilities.locators import SampleFormDemolocators


class SampleFormDemo(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.wait = WebDriverWait(driver, 20)  # 20 sec timeout

    def click_sampleDemoPage(self, page_name):
        self.page(page_name)

    def enter_message(self, Enter_Message_files, welcome_lambda):
        self.wait.until(EC.visibility_of_element_located(Enter_Message_files))
        self.set(Enter_Message_files, welcome_lambda)
        self.wait.until(EC.element_to_be_clickable(SampleFormDemolocators.Get_Checked_button))
        self.click(SampleFormDemolocators.Get_Checked_button)

    def output_text(self, get_Message_filed):
        # Wait until output message is visible
        self.wait.until(EC.visibility_of_element_located(get_Message_filed))
        return self.get_text(get_Message_filed)


