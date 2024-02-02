# Here will be the main logic
from datetime import datetime, timedelta
from consumptions import get_counters_consumption
from counters import get_counters_info


def filter_retreived_energy():
    """ Gets energy consumption data from the database
        looks for which the data belongs to which counter,
        makes a list of the summed up data. """
    yesterday = datetime.today()-timedelta(days=16)
    sql_date  = yesterday.strftime("%Y-%m-%d")
    consumptions = get_counters_consumption(sql_date)
    counters = get_counters_info()
    filtered_consumption={} 
    for counter in counters:
        for consumption in consumptions:
            if counter[3] == consumption[1] and counter[2] == consumption[0]:
                one_counter_total_energy = (sum(consumption[3:6]))
                filtered_consumption[counter[1]] = round(one_counter_total_energy, 2)
                break
    return filtered_consumption


if __name__=="__main__":
    filtered_energy = filter_retreived_energy() 
    for key, value in filtered_energy.items():
        print(key, value)
