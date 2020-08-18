# TO DO:
# - napisz funkcję, która będzie uderzać pod endpoint z kursami walut
# np. https://exchangeratesapi.io/
# - dodaj blok try/except aby zabezpieczyć ją przed Timeoutem
# - dodaj drugą funkcję - dekorator, która będzie mierzyła czas trwania zapytania oraz datę i godzinę,
# w której odbyło się zapytanie.
# Zwróć te czasy na ekran
# - Niech program wykonuje się w pętli z interwałem 15 sek.
# - Przykładowy output
#
# Kurs Euro: 4,2356
# Data i godzina: 23.03.2020 14:14:13
# Czas wykonania zapytania: 150ms

# importing the requests library
import requests

# api-endpoint
url = 'https://api.exchangeratesapi.io/latest?base=GBP'

# sending get request
response = requests.get(url)
print(response.text)
# extracting data in json format
data = response.json()

# extracting EUR currency
euro = data['rates']['EUR']
base = data['base']
date = data['date']
print('Kurs EUR wynosi: ', euro)
print('Bazowa waluta: ', base)
print('Data zapytania: ', date)