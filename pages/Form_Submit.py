from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utilities.locators import InputFormSubmitlocators



class  InputFormSubmit(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.wait = WebDriverWait(driver, 20)  # 20 sec timeout

    def click_InputformPage(self, page_name):
        self.page(page_name)
        self.wait.until(EC.presence_of_element_located(InputFormSubmitlocators.Input_validate))

    def enter_name(self, Name_Field, Name_person):
        self.wait.until(EC.visibility_of_element_located(Name_Field))
        self.set(Name_Field, Name_person)

    def enter_email(self, Email_Field, Email):
        self.wait.until(EC.visibility_of_element_located(Email_Field))
        self.set(Email_Field, Email)

    def enter_password(self, Password_Field, Password):
        self.wait.until(EC.visibility_of_element_located(Password_Field))
        self.set(Password_Field, Password)

    def enter_company(self, Company_Field, Company):
        self.wait.until(EC.visibility_of_element_located(Company_Field))
        self.set(Company_Field, Company)

    def enter_website(self, Website_Field, Website):
        self.wait.until(EC.visibility_of_element_located(Website_Field))
        self.set(Website_Field, Website)

    def enter_countryname(self, Country_Name, Country):
        dropdown_element = self.wait.until(EC.visibility_of_element_located(Country_Name))
        select = Select(dropdown_element)
        select.select_by_visible_text(Country)

    def enter_cityname(self, City_Field, City):
        self.wait.until(EC.visibility_of_element_located(City_Field))
        self.set(City_Field, City)

    def enter_Address1(self, Address1_Field, Address1):
        self.wait.until(EC.visibility_of_element_located(Address1_Field))
        self.set(Address1_Field, Address1)

    def enter_Address2(self, Address2_Field, Address2):
        self.wait.until(EC.visibility_of_element_located(Address2_Field))
        self.set(Address2_Field, Address2)

    def enter_State(self, State_Field, State):
        self.wait.until(EC.visibility_of_element_located(State_Field))
        self.set(State_Field, State)

    def enter_zipcode(self, Zip_code_field, Zip_Code):
        self.wait.until(EC.visibility_of_element_located(Zip_code_field))
        self.set(Zip_code_field, Zip_Code)

    def  submit_the_form(self,Submit_button):
        self.click(Submit_button)

    def verify_confirmation_message(self, confirmation_message):
        self.wait.until(EC.presence_of_element_located(confirmation_message))
        return  self.get_text(confirmation_message)







