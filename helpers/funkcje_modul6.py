from selenium import webdriver

# import biblioteki do funkcji nr 1
from selenium.webdriver.common.action_chains import ActionChains
# import bibliotek do funkcji nr 2
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

# import danych z pliku DataGenerator.py
# wcześniej trzeba utworzyć plik __init__.py w katalogu 'helpers'
from helpers.DataGenerator import DataGenerator

# 1 - Funkcja, która sprawdza tekst na nieaktywnym przycisku
def hover_over_element(driver_instance, xpath):
    elem = driver_instance.find_element_by_xpath(xpath)
    hover = ActionChains(driver_instance).move_to_element(elem)
    hover.perform()


# 2 - Funkcja, która czeka na pojawienie się elementu na ekranie
def wait_for_visibility_of_element(driver_instance, xpath, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.XPATH,xpath)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_visibility_of_element_by_id(driver_instance, ID, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.ID,ID)))
    except TimeoutException:
        elem = False
    return elem

# 3 - Funkcja, która czeka aż element zniknie
def wait_for_invisibility_of_element(inv_driver_instance, id, time_to_wait=8):
    inv_element = WebDriverWait(inv_driver_instance, time_to_wait).until(EC.invisibility_of_element_located((By.ID,id)))
    return inv_element


def wait_for_invisibility_of_element_by_xpath(inv_driver_instance, xpath, time_to_wait=8):
    inv_element = WebDriverWait(inv_driver_instance, time_to_wait).until(EC.invisibility_of_element_located((By.XPATH,xpath)))
    return inv_element

# Użycie generatora danych
test = DataGenerator.generateProperEmail()

print(test)