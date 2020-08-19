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

# import the requests and datetime library
import requests
from datetime import datetime


# api-endpoint, global variable
url = 'https://api.exchangeratesapi.io/latest'



def exchange_rate():
    try:
        # send "get" request
        response = requests.get(url)

        # save data in json format
        data = response.json()

        # extract PLN currency from json file
        rate = data['rates']['PLN']
        print('Kurs euro: ', rate)

    except TimeoutError:
        print('API unavailable. Timeout error. Try later.')


def exchange_information(function):
    def date_and_time():
        # call exchange_rate() function
        function()

        # get current date and time in format RRRR-MM-DD HH:MM:SS:MS
        now = datetime.now()

        # convert to format dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print('Data i godzina: ', dt_string)

        # measure execution time in milliseconds
        response = requests.get(url)

        # response.elapsed.total_seconds() returns seconds.
        # To get milliseconds I have to multiply the result by 1000
        response_time = response.elapsed.total_seconds() * 1000
        print('Czas wykonania zapytania: ', response_time, 'ms')
    return date_and_time()

# call the function with other function as a parameter
exchange_information(exchange_rate)

# def getDateAndTime2():
#     # get current date and time in format RRRR-MM-DD HH:MM:SS:MS
#     now = datetime.now()
#
#     # dd/mm/YY H:M:S
#     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#     print('Data i godzina: ', dt_string)
#
#     # measure execution time in milliseconds
#     response = requests.get(url)
#     # response.elapsed.total_seconds() returns seconds.
#     # To get milliseconds I have to multiply the result by 1000
#     responseTime = response.elapsed.total_seconds() * 1000
#     print('Czas wykonania zapytania: ', responseTime, 'ms')



# exchange_rate()
# getDateAndTime()

