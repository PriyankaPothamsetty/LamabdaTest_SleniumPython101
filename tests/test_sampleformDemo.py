from pages.Sample_Form_Demo_Page import SampleFormDemo
from utilities.Test_Data import Test_Data
from tests.base_test import BaseTest
from utilities.locators import SampleFormDemolocators
import conftest

class TestSampleFormDemo(BaseTest):

    def test_SampleFormDemo(self):
        Sampleform_page = SampleFormDemo(self.driver)
        Sampleform_page.click_sampleDemoPage(Test_Data.Page_Name)
        page_url = self.driver.current_url
        assert "simple-form-demo" in page_url
        Sampleform_page.enter_message(SampleFormDemolocators.Enter_Message_files, Test_Data.welcome_lambda)
        actual_text = Sampleform_page.output_text(SampleFormDemolocators.get_Message_filed)
        assert actual_text == Test_Data.welcome_lambda
        conftest.change_test_status(self.driver , actual_text == Test_Data.welcome_lambda)






