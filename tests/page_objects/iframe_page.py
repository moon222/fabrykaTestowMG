from helpers.funkcje_modul6 import *

iframe_tab = 'iframe-header'
iframe_content = 'iframe-content'
iframe_button1 = 'simpleButton1'
iframe_button2 = 'simpleButton2'
which_button_is_clicked = 'whichButtonIsClickedMessage'


def click_iframe_tab(driver_instance):
    elem = driver_instance.find_element_by_id(iframe_tab)
    elem.click()


def iframe_content_visibility(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, iframe_content, time_to_wait=1)
    return elem.is_displayed()


def iframe_click_button1(driver_instance):
    iframes = driver_instance.find_elements_by_tag_name('iframe')

    driver_instance.switch_to.frame(iframes[0])

    elem1 = driver_instance.find_element_by_id(iframe_button1)
    elem1.click()

    elem2 = driver_instance.find_element_by_id(which_button_is_clicked)
    value1 = elem2.text
    value2 = 'Button 1 was clicked!'
    if value1 == value2:
        return True
    else:
        return False


def iframe_click_button2(driver_instance):
    iframes = driver_instance.find_elements_by_tag_name('iframe')

    driver_instance.switch_to.frame(iframes[0])

    elem1 = driver_instance.find_element_by_id(iframe_button2)
    elem1.click()

    elem2 = driver_instance.find_element_by_id(which_button_is_clicked)
    value1 = elem2.text
    value2 = 'Button 2 was clicked!'
    if value1 == value2:
        return True
    else:
        return False