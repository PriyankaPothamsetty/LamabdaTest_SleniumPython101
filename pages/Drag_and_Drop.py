from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utilities.locators import  DragandDrop



class  DragandDrog(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.wait = WebDriverWait(driver, 20)  # 10 sec timeout

    def click_DragandDropPage(self, page_name):
        self.page(page_name)

    def  Move_Slider(self,Default_value_15,Drag_Slider):
        self.wait.until(EC.visibility_of_element_located(Default_value_15))
        slider = self.wait.until(EC.visibility_of_element_located(Drag_Slider))
        actions = ActionChains(self.driver)
        offset =  215
        actions.click_and_hold(slider).move_by_offset(offset, 0).release().perform()


    def get_slider_value(self, Drag_Range):
        #slider_value = self.wait.until(EC.visibility_of_element_located(Drag_Range))
        return  self.get_text(Drag_Range)







    