# Here willbe the main logic
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
    filtred_consumption = [] 
    for counter in counters:
        for consumption in consumptions:
            if counter[3] == consumption[1] and counter[2] == consumption[0]:
                one_counter_consumption=[]
                one_counter_total_energy = round(sum(consumption[3:6], 2))
                one_counter_consumption.append(counter[1])
                one_counter_consumption.append(one_counter_total_energy)
                break
        filtred_consumption.append(one_counter_consumption)
    return filtred_consumption


if __name__=="__main__":
    filtered_energy = filter_retreived_energy() 
    for num, char in enumerate (filtered_energy, 1):
        print(num, char)
