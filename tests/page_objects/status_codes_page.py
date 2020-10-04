from helpers.funkcje_modul6 import *

status_codes_tab = 'statuscodes-header'
status_codes_content = 'statuscodes-content'
status_codes_200 = '200siteAnchor'
status_codes_305 = '305siteAnchor'
status_codes_404 = '404siteAnchor'
status_codes_500 = '500siteAnchor'


def click_status_codes_tab(driver_instance):
    elem = driver_instance.find_element_by_id(status_codes_tab)
    elem.click()


def status_codes_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, status_codes_content)
    return elem.is_displayed()
