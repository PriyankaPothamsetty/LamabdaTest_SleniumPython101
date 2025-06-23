from selenium.webdriver.common.by import By
from utilities.Test_Data import Test_Data

class  SampleFormDemolocators:
    Enter_Message_files = (By.XPATH,"//input[@placeholder='Please enter your Message']")
    Get_Checked_button = (By.ID,"showInput")
    get_Message_filed = (By.XPATH,"//p[@id='message']")


class  DragandDrop:
    Default_value_15 = (By.XPATH,"//h4[text()='"+ Test_Data.Slider_To_Move +"']")
    Drag_Slider = (By.XPATH,"//h4[text()='"+ Test_Data.Slider_To_Move +"']/following-sibling::div//input[@class='sp__range']")
    Drag_Range = (By.XPATH,"//h4[text()='"+ Test_Data.Slider_To_Move +"']/following-sibling::div//output[@id='rangeSuccess']")

class  InputFormSubmitlocators:
    Input_validate = (By.XPATH, "//div[@class='container']//h2[text()='Input form validations']")
    Name_Field = (By.ID,"name")
    Email_Field = (By.ID,"inputEmail4")
    Password_Field = (By.ID, "inputPassword4")
    Company_Field = (By.ID, "company")
    Website_Field = (By.ID, "websitename")
    Country_Name = (By.NAME, "country")
    City_Field = (By.ID, "inputCity")
    Address1_Field = (By.ID, "inputAddress1")
    Address2_Field = (By.ID, "inputAddress2")
    State_Field = (By.XPATH, "//input[@placeholder='State']")
    Zip_code_field = (By.ID, "inputZip")
    Submit_button = (By.XPATH, "//button[text()='Submit']")
    confirmation_message = (By.XPATH,"//p[@class='success-msg hidden']")
