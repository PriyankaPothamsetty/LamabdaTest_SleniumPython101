from tests.base_test import  BaseTest
from utilities.Test_Data import Test_Data
from utilities.locators import  InputFormSubmitlocators
from pages.Form_Submit import   InputFormSubmit
import conftest


class Test_FormSubmit(BaseTest):

    def test_FormSubmit(self):
        inputform_page = InputFormSubmit(self.driver)
        inputform_page.click_InputformPage(Test_Data.InputForm_Page_Name)
        name_field = self.driver.find_element(*InputFormSubmitlocators.Name_Field)
        inputform_page.submit_the_form(InputFormSubmitlocators.Submit_button)
        message = self.driver.execute_script("return arguments[0].validationMessage;", name_field)
        print("The message is:", message)
        assert "Please fill out this field" in message
        inputform_page.enter_name(InputFormSubmitlocators.Name_Field, Test_Data.Name_person)
        inputform_page.enter_email(InputFormSubmitlocators.Email_Field, Test_Data.Email)
        inputform_page.enter_password(InputFormSubmitlocators.Password_Field, Test_Data.Password)
        inputform_page.enter_company(InputFormSubmitlocators.Company_Field, Test_Data.Company)
        inputform_page.enter_website(InputFormSubmitlocators.Website_Field, Test_Data.Website)
        inputform_page.enter_countryname(InputFormSubmitlocators.Country_Name, Test_Data.Country)
        inputform_page.enter_cityname(InputFormSubmitlocators.City_Field, Test_Data.City)
        inputform_page.enter_Address1(InputFormSubmitlocators.Address1_Field, Test_Data.Address1)
        inputform_page.enter_Address2(InputFormSubmitlocators.Address2_Field, Test_Data.Address2)
        inputform_page.enter_State(InputFormSubmitlocators.State_Field, Test_Data.State)
        inputform_page.enter_zipcode(InputFormSubmitlocators.Zip_code_field, Test_Data.Zip_Code)
        inputform_page.submit_the_form(InputFormSubmitlocators.Submit_button)
        confirmation_message = inputform_page.verify_confirmation_message(InputFormSubmitlocators.confirmation_message)
        assert confirmation_message.__contains__("Thanks for contacting us, we will get back to you shortly.")
        conftest.change_test_status(self.driver, confirmation_message.__contains__("Thanks for contacting us, we will get back to you shortly."))
