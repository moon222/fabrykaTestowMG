from helpers.funkcje_modul6 import *

basic_auth_tab = 'basicauth-header'
basic_auth_content = 'basicauth-content'
basic_auth_username = 'ba_username'
basic_auth_password = 'ba_password'
basic_auth_login = '//*[@id="content"]/button'
basic_auth_error1 = 'loginFormMessage'
basic_auth_logged_in = 'loggedInMessage'


def click_basic_auth_tab(driver_instance):
    elem = driver_instance.find_element_by_id(basic_auth_tab)
    elem.click()


def basic_auth_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, basic_auth_content)
    return elem.is_displayed()


def login_with_empty_credentials(driver_instance):
    wait_for_visibility_of_element(driver_instance, basic_auth_login, time_to_wait=1)
    # Find the login button
    elem1 = driver_instance.find_element_by_xpath(basic_auth_login)
    elem1.click()
    # Find error message
    elem2 = driver_instance.find_element_by_id(basic_auth_error1)
    value1 = elem2.text
    value2 = 'Invalid credentials'
    if value1 == value2:
        return True
    else:
        return False


def login_with_correct_credentials(driver_instance):
    # Wait for username
    wait_for_visibility_of_element_by_id(driver_instance, basic_auth_username, time_to_wait=1)
    # Type correct username 'admin'
    elem1 = driver_instance.find_element_by_id(basic_auth_username)
    elem1.send_keys('admin')
    # Wait for password
    wait_for_visibility_of_element_by_id(driver_instance, basic_auth_password, time_to_wait=1)
    # Type correct password 'admin'
    elem2 = driver_instance.find_element_by_id(basic_auth_password)
    elem2.send_keys('admin')
    # Wait for Login button
    wait_for_visibility_of_element(driver_instance, basic_auth_login, time_to_wait=1)
    # Click login button
    elem3 = driver_instance.find_element_by_xpath(basic_auth_login)
    elem3.click()
    # Check if 'you are logged in' message is displayed
    elem4 = driver_instance.find_element_by_id(basic_auth_logged_in)
    value1 = elem4.text
    value2 = 'You are logged in!'
    if value1 == value2:
        return True
    else:
        return False


def login_with_incorrect_username_and_correct_password(driver_instance):
    # Wait for username
    wait_for_visibility_of_element_by_id(driver_instance, basic_auth_username, time_to_wait=1)
    # Type incorrect username 'abcd'
    elem1 = driver_instance.find_element_by_id(basic_auth_username)
    elem1.send_keys('abcd')
    # Wait for password
    wait_for_visibility_of_element_by_id(driver_instance, basic_auth_password, time_to_wait=1)
    # Type correct password 'admin'
    elem2 = driver_instance.find_element_by_id(basic_auth_password)
    elem2.send_keys('admin')
    # Wait for Login button
    wait_for_visibility_of_element(driver_instance, basic_auth_login, time_to_wait=1)
    # Click login button
    elem3 = driver_instance.find_element_by_xpath(basic_auth_login)
    elem3.click()
    # Check if 'Invalid credentials' message is displayed
    elem4 = driver_instance.find_element_by_id(basic_auth_error1)
    value1 = elem4.text
    value2 = 'Invalid credentials'
    if value1 == value2:
        return True
    else:
        return False


def login_with_correct_username_and_incorrect_password(driver_instance):
    # Wait for username
    wait_for_visibility_of_element_by_id(driver_instance, basic_auth_username, time_to_wait=1)
    # Type correct username 'admin'
    elem1 = driver_instance.find_element_by_id(basic_auth_username)
    elem1.send_keys('admin')
    # Wait for password
    wait_for_visibility_of_element_by_id(driver_instance, basic_auth_password, time_to_wait=1)
    # Type incorrect password '1234'
    elem2 = driver_instance.find_element_by_id(basic_auth_password)
    elem2.send_keys('1234')
    # Wait for Login button
    wait_for_visibility_of_element(driver_instance, basic_auth_login, time_to_wait=1)
    # Click login button
    elem3 = driver_instance.find_element_by_xpath(basic_auth_login)
    elem3.click()
    # Check if 'Invalid credentials' message is displayed
    elem4 = driver_instance.find_element_by_id(basic_auth_error1)
    value1 = elem4.text
    value2 = 'Invalid credentials'
    if value1 == value2:
        return True
    else:
        return False
