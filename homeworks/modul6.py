from selenium import webdriver


# Ustaw driver
driver = webdriver.Chrome()

# Otwórz stronę fabrykatestow.pl
driver.get('https://fabrykatestow.pl')
# Zmaksymalizj wielkosc okna - na niektorych rozdzielczosciach menu gorke zwija sie w hamburgera
driver.maximize_window()
# Otwórz zakładkę "KURS TAPS"
# Użyłam selectora id_element
kurs_taps = driver.find_element_by_id('menu-item-506')
kurs_taps.click()

# Przescrolluj do sekcji "Kim jest Twój instruktor?"
# Użyłam selectora xpath
element = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div/div/div/section[8]/div/div/div/div/div/div/div/h2')
element.location_once_scrolled_into_view

# Zrób screenshot strony - wersja podstawowa
driver.save_screenshot('file1.png')

# Zrób screenshot strony - wersja z zapisem pliku w określonej lokalizacji
# driver.save_screenshot('C:/Users/mongo/Desktop/Screenshots/file1.png')

# Zamknij okno przeglądarki
driver.quit()
