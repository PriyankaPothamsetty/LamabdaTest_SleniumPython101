from pages.Drag_and_Drop import DragandDrog
from tests.base_test import BaseTest
from utilities.Test_Data import Test_Data
from utilities.locators import   DragandDrop
import conftest


class TestDragandDrop(BaseTest):

    def test_DragandDrop(self):
        Drag_page = DragandDrog(self.driver)
        Drag_page.click_DragandDropPage(Test_Data.Drag_Page_Name)
        Drag_page.Move_Slider(DragandDrop.Default_value_15, DragandDrop.Drag_Slider)
        expected_slider_size = Drag_page.get_slider_value(DragandDrop.Drag_Range)
        assert expected_slider_size == '95'
        conftest.change_test_status(self.driver, expected_slider_size == '95')
