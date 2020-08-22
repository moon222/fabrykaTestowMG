from selenium import webdriver

import time

# webdriver służy do komunikacji z przeglądarką
driver = webdriver.Chrome('/Users/mongo/PycharmProjects/kurs_taps_windows/chromedriver.exe')

# otwiera podaną stronę
driver.get('https://google.pl')

search_box = driver.find_element_by_name('q')

search_box.send_keys('selenium python')

search_box.submit()

time.sleep(5)

# zamyka wszystkie okna przeglądarki
driver.quit()

# zamyka tylko jedno okno przeglądrki
# driver.close()