from helpers.funkcje_modul6 import *

drag_and_drop_tab = 'draganddrop-header'
drag_and_drop_content = 'draganddrop-content'
drag_and_drop_column_a = '//*[@id="column-a"]'
drag_and_drop_column_b = '//*[@id="column-b"]'


def click_drag_and_drop_tab(driver_instance):
    elem = driver_instance.find_element_by_id(drag_and_drop_tab)
    elem.click()


def drag_and_drop_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, drag_and_drop_content, time_to_wait=1)
    return elem.is_displayed()

