# Here is the main logic
import time
from datetime import datetime, timedelta
from consumptions import get_counters_consumption
from counters import get_counters_info
from inputwindows import UserInput


def day_energy_handler(sql_date: str) -> dict:
    """
    Gets energy consumption data from the database,
    looks for which the data belongs to which counter,
    makes a dict of the summed up data,
    puts the data to excel file.

    :param sql_date: date on which you need to receive the data (str)
    """
    consumptions = get_counters_consumption(sql_date)
    counters = get_counters_info()
    one_filtered_consumption = {}
    for counter in counters:
        for consumption in consumptions:
            if counter[3] == consumption[1] and counter[2] == consumption[0]:
                one_counter_total_energy = (sum(consumption[3:6]))
                one_filtered_consumption[counter[1]] = round(one_counter_total_energy, 2)
                break
    return one_filtered_consumption


def period_energy_handler() -> None:
    """ 
    Counts the period of needed data,
    pass every single data as a parameter
    to a single day retrieving energy function. 
    """
    user_input = UserInput()
    try:
        update_days = user_input.make_user_input() - 1
    except TypeError:
        return
    data_day = datetime.today()-timedelta(days=update_days)
    sql_date = data_day.strftime("%Y-%m-%d")
    day_energy_handler(sql_date)


if __name__ == "__main__":
    print(time.strftime("%X"))
    period_energy_handler()
    print(time.strftime("%X"))
