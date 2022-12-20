from datetime import datetime as dt


def temperature_logger(data):
    with open('log.csv', 'a') as file:
        file.write(f'{get_now()};temperature;{data}\n')


def pressure_logger(data):
    with open('log.csv', 'a') as file:
        file.write(f'{get_now()};pressure;{data}\n')


def wind_speed_logger(data):
    with open('log.csv', 'a') as file:
        file.write(f'{get_now()};wind_speed;{data}\n')


def get_now():
    return dt.now().strftime("%H:%M:%S")