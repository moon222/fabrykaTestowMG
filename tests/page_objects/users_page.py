from helpers.funkcje_modul6 import *

error_info = 'container'


def error_info_displayed(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, error_info)
    return elem.is_displayed()