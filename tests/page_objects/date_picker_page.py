from helpers.funkcje_modul6 import *

date_picker_tab = 'datepicker-header'
date_picker_content = 'datepicker-content'
date_picker = 'start'


def click_date_picker_tab(driver_instance):
    elem = driver_instance.find_element_by_id(date_picker_tab)
    elem.click()


def date_picker_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, date_picker_content)
    return elem.is_displayed()


def set_correct_date(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, date_picker, time_to_wait=1)
    elem = driver_instance.find_element_by_id(date_picker)
    elem.send_keys('1402')
    value = '2020-02-14'
    if value == elem.get_attribute("value"):
        return True
    else:
        return False


def set_incorrect_date(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, date_picker, time_to_wait=1)
    elem = driver_instance.find_element_by_id(date_picker)
    elem.send_keys('4142')
    value = '2020-42-41'
    if value == elem.get_attribute("value"):
        return False
    else:
        return True
