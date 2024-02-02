# Here is the main logic
from datetime import datetime, timedelta
from consumptions import get_counters_consumption
from counters import get_counters_info
from excels import put_consumptions_to_excel


def day_energy_handler(sql_date, data_day):
    """ Gets energy consumption data from the database
        looks for which the data belongs to which counter,
        makes a dict of the summed up data,
        puts the data to excel file. """
    consumptions = get_counters_consumption(sql_date)
    counters = get_counters_info()
    filtered_consumption={} 
    for counter in counters:
        for consumption in consumptions:
            if counter[3] == consumption[1] and counter[2] == consumption[0]:
                one_counter_total_energy = (sum(consumption[3:6]))
                filtered_consumption[counter[1]] = round(one_counter_total_energy, 2)
                break
    put_consumptions_to_excel(data_day, filtered_consumption)
    return filtered_consumption


def period_energy_handler():
    """ Counts the period of needed data,
        pass every single data as a parameter
        to a single day retrieving energy function. """
    for day in range(3, -1, -1): # Today to three days ago in descendштп order
        data_day = datetime.today()-timedelta(days=day)
        sql_date = data_day.strftime("%Y-%m-%d")
        day_energy_handler(sql_date, data_day)


if __name__=="__main__":
    period_energy_handler()