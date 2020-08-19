# import used libraries
import requests
from datetime import datetime
from threading import Timer

# api-endpoint, global variable
url = 'https://api.exchangeratesapi.io/latest'

# exchange_rate() function print euro rate from get request
def exchange_rate():
    try:
        # send "get" request
        response = requests.get(url)

        # save data in json format
        data = response.json()

        # extract PLN currency from json file
        rate = data['rates']['PLN']
        print('Kurs euro:', rate)

    except TimeoutError:
        print('API unavailable. Timeout error. Try later.')

# exchange_information() function uses other function and returns more informations such as:
# current date and time and request response time.
def exchange_information(function):
    def date_and_time():
        # call exchange_rate() function
        function()

        # get current date and time in format RRRR-MM-DD HH:MM:SS:MS
        now = datetime.now()

        # convert to format dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print('Data i godzina:', dt_string)

        # measure execution time in milliseconds
        response = requests.get(url)

        # response.elapsed.total_seconds() returns seconds.
        # To get milliseconds I have to multiply the result by 1000
        response_time = response.elapsed.total_seconds() * 1000
        print('Czas wykonania zapytania:', response_time, 'ms')

    return date_and_time

# create a new function and assign 'exchange_information' with 'exchange_rate' function as parameter
# it's needed for call_interval function
new_function = exchange_information(exchange_rate)

# create 'call_interval' function with timer set to 15 seconds
def call_interval():
    text = "------------------------------------"
    # call new_function
    new_function()
    # print text variable content
    print(f"{text}")
    # set timer and start it
    Timer(15, call_interval).start()

# call 'call_interval' function
call_interval()
