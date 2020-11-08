from helpers.funkcje_modul6 import *


key_tab = 'keypresses-header'
key_content = 'keypresses-content'
key_input = 'target'
key_press_result = 'keyPressResult'


def click_key_presses_tab(driver_instance):
    elem = driver_instance.find_element_by_id(key_tab)
    elem.click()


def key_presses_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, key_content)
    return elem.is_displayed()


def key_press_enter_button(driver_instance):
    # wait for visibility of key input
    wait_for_visibility_of_element_by_id(driver_instance, key_input, time_to_wait=1)
    # Click on input
    elem1 = driver_instance.find_element_by_id(key_input)
    elem1.click()
    # press Enter button
    elem1.send_keys('\ue007')
    # find key press result
    wait_for_visibility_of_element_by_id(driver_instance, key_press_result, time_to_wait=1)
    elem2 = driver_instance.find_element_by_id(key_press_result)
    # get text from elem2
    value1 = elem2.text
    value2 = 'You entered: ENTER'
    if value1 == value1:
        return True
    else:
        return False


