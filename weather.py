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

def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_farenheit = float(temp_in_farenheit)
    temp_in_celcius_original = (temp_in_farenheit-32)*5/9
    temp_in_celcius = round(temp_in_celcius_original,1)
    return temp_in_celcius



def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    total = 0
    count=len(weather_data)
    # for i in range(count):
    #     total += float(weather_data[i])
    # mean_value = total/count
    for i in weather_data:
        total +=float(i)
    mean_value = total/count
    return mean_value


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data_list=[]
    with open(csv_file, mode="r", encoding="utf-8") as my_file:
        f_reader=csv.reader(my_file)
        next (f_reader)
        for line in f_reader:
            if len(line)>=3:
                line_data = [line[0], int(line[1]), int(line[2])]
                data_list.append(line_data)
    return data_list

    


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if weather_data==[]:
        return ()
    else:
        
        data_min = float(weather_data[0])
        min_position = 0
        for i in range(1,len(weather_data)):
            if float(weather_data[i]) <= data_min:
                data_min = float(weather_data[i])
                min_position = i
        return data_min, min_position


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if weather_data==[]:
        return ()
    else:
        
        data_max = float(weather_data[0])
        max_position = 0
        for i in range(1,len(weather_data)):
            if float(weather_data[i]) >= data_max:
                data_max = float(weather_data[i])
                max_position = i
        return data_max, max_position


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    temp_min_list = []
    temp_max_list=[]
    date_list=[]
    for line in weather_data:
        date_list.append(line[0])
        temp_min_list.append(line[1])
        temp_max_list.append(line[2])
    min_value_f = find_min(temp_min_list)[0]
    min_value_c = convert_f_to_c(min_value_f)
    min_data_position = find_min(temp_min_list)[1]
    max_value_f = find_max(temp_max_list)[0]
    max_value_c = convert_f_to_c(max_value_f)
    max_data_positon = find_max(temp_max_list)[1]
    average_low_f = calculate_mean(temp_min_list)
    average_low_c = convert_f_to_c(average_low_f)
    average_high_f = calculate_mean(temp_max_list)
    average_high_c = convert_f_to_c(average_high_f)
    return (
        # f"{len(weather_data)} Day Overview"
        # f" The lowest temperature will be {format_temperature(min_value_c)}, and will occur on {convert_date(date_list[min_data_position])}."
        # f" The highest temperature will be {format_temperature(max_value_c)}, and will occur on {convert_date(date_list[max_data_positon])}."
        # f" The average low this week is {format_temperature(average_low_c)}."
        # f" The average high this week is {format_temperature(average_high_c)}."
        f"{len(weather_data)} Day Overview\n  The lowest temperature will be {format_temperature(min_value_c)}, and will occur on {convert_date(date_list[min_data_position])}.\n  The highest temperature will be {format_temperature(max_value_c)}, and will occur on {convert_date(date_list[max_data_positon])}.\n  The average low this week is {format_temperature(average_low_c)}.\n  The average high this week is {format_temperature(average_high_c)}.\n"
    )
    # return (
    #     f"{len(weather_data)} Day Overview"
    #     f"The lowest temperature will be {min_value}°C, and will occur on {convert_date(date_list[min_data_position])}."
    #     f"The highest temperature will be {max_value}°C, and will occur on {convert_date(date_list[max_data_positon])}."
    #     f"The average low this week is {average_low}°C."
    #     f"The average high this week is {average_high}°C."
    # )


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_list=[]
    for line in weather_data:
        daily_list.append(f"---- {convert_date(line[0])} ----\n  Minimum Temperature: {format_temperature(convert_f_to_c(line[1]))}\n  Maximum Temperature: {format_temperature(convert_f_to_c(line[2]))}\n\n")
        # return(
        #     f"---- {convert_date(line[0])} ----\n  Minimum Temperature: {format_temperature(convert_f_to_c(line[1]))}\n  Maximum Temperature: {format_temperature(convert_f_to_c(line[2]))}\n\n"
        #     )
        
    return "".join(daily_list)
