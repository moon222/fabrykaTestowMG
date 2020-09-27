import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, checkboxes_page, hovers_page, users_page, inputs_page, dropdown_page
from tests.page_objects import add_remove_page, date_picker_page, basic_auth_page, form_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    def test2_checkboxes(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_visible(self.driver))
        checkboxes_page.click_checkboxes(self.driver)

    def test3_hovers(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hover_content_displayed(self.driver))
        hovers_page.hover_over_element_and_click(self.driver)
        self.assertTrue(users_page.error_info_displayed(self.driver))

    def test4_inputs_visibility(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.input_content_visible(self.driver))

    def test5_inputs_correct_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_correct_keys_to_input(self.driver))

    def test6_inputs_incorrect_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_incorrect_keys_to_input(self.driver))

    def test7_dropdown_select(self):
        dropdown_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_page.dropdown_content_visible(self.driver))
        dropdown_page.get_first_dropdown_value(self.driver)

    def test8_add_element(self):
        add_remove_page.click_and_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)

    def test9_delete_element(self):
        add_remove_page.click_and_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)
        add_remove_page.delete_element(self.driver)
        self.assertTrue(add_remove_page.element_invisible(self.driver))

    def test10_date_picker_correct_date(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.date_picker_content_visible(self.driver))
        self.assertTrue(date_picker_page.set_correct_date(self.driver))

    def test10_date_picker_incorrect_date(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.date_picker_content_visible(self.driver))
        self.assertTrue(date_picker_page.set_incorrect_date(self.driver))

    def test11_basic_auth_login_without_credentials(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))
        self.assertTrue(basic_auth_page.login_with_empty_credentials(self.driver))

    def test12_basic_auth_login_with_correct_credentials(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))
        self.assertTrue(basic_auth_page.login_with_correct_credentials(self.driver))

    def test13_basic_auth_login_with_incorrect_username(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))
        self.assertTrue(basic_auth_page.login_with_incorrect_username_and_correct_password(self.driver))

    def test14_basic_auth_login_with_incorrect_password(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))
        self.assertTrue(basic_auth_page.login_with_correct_username_and_incorrect_password(self.driver))

    def test15_form_filling(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_content_visible(self.driver))
        self.assertTrue(form_page.form_filled(self.driver))

if __name__ == '__main__':
    unittest.main()
