import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date_obj = datetime.fromisoformat(iso_string)
    date_formatted = date_obj.strftime("%A %d %B %Y")
    return date_formatted
# date01="2021-07-05T07:00:00+08:00"
# date02=convert_date(date01)
# print(date02)
def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_celcius = 5*(temp_in_farenheit-32)/9
    temp_in_celcius_rounded = round(temp_in_celcius,1)
    return temp_in_celcius_rounded
# temp_f = 120
# temp_c = convert_f_to_c(temp_f)
# print(temp_c)
def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    total = 0
    count=len(weather_data)
    for i in range(count):
        total += weather_data[i]
        mean_value = total/count

    return mean_value
# list1=[100,90,20,45]
# list_mean=calculate_mean(list1)
# print(list_mean)
# data_list=[]
# with open(file="tests/data/example_one.csv") as my_file:
#     f_reader=csv.reader(my_file)
#     for line in f_reader:
#         data_list.append(line)
# print(data_list)

weather_data=[101,20,50,1000,1,89]
data_min = weather_data[0]
min_position = 0
for i in range(1,len(weather_data)):
    if weather_data[i] < data_min:
        data_min = weather_data[i]
        min_position = i
print(data_min, min_position)