from helpers.funkcje_modul6 import *
import time

form_tab = 'form-header'
form_content = 'form-content'
form_first_name = 'fname'
form_last_name = 'lname'
form_submit = 'formSubmitButton'


def click_form_tab(driver_instance):
    elem = driver_instance.find_element_by_id(form_tab)
    elem.click()


def form_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, form_content)
    return elem.is_displayed()


def form_filled(driver_instance):
    # Wait for first name input
    wait_for_visibility_of_element_by_id(driver_instance, form_first_name, time_to_wait=1)
    # Find first name input and type John
    elem1 = driver_instance.find_element_by_id(form_first_name)
    elem1.send_keys('John')
    # Wait for last name input
    wait_for_visibility_of_element_by_id(driver_instance, form_last_name, time_to_wait=1)
    # Find first name input and type John
    elem2 = driver_instance.find_element_by_id(form_last_name)
    elem2.send_keys('von Smith')
    # Wait for 'Submit' button
    wait_for_visibility_of_element_by_id(driver_instance, form_submit, time_to_wait=1)
    # Find 'Submit' button
    elem3 = driver_instance.find_element_by_id(form_submit)
    elem3.click()
    time.sleep(3)
    # Check if 'success' message is displayed
    alert = driver_instance.switch_to.alert
    # Extract text from alert
    value1 = alert.text
    value2 = 'success'
    if value1 == value2:
        return True
    else:
        return False
