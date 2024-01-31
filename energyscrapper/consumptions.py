# The script gets the energy consumption info
from datetime import datetime, timedelta
from counters import get_counters_info
from connections import cursor


yesterday = datetime.today()-timedelta(days=16)
sql_date = yesterday.strftime("%Y-%m-%d") 


def get_counters_consumption():
    """ Gets energy consumption data from the database,
            looks for which the data belongs to which counter,
            makes a list of the summed up data. """
    counters = get_counters_info()
    request = (f"SELECT NUM_DEVICE, NUM_CH , DT_DAY,TARIF1, TARIF2, TARIF3 FROM IMPULS4 WHERE DT_DAY='{sql_date}'")
    cursor.execute(request)
    all_counters_consumption = []
    for consumption in cursor.fetchall():
        for counter in counters:
            one_counter_consumption = []
            if counter[3] == consumption[1]:
                if counter[2] == consumption[0]:
                    one_counter_consumption.append(counter[1])
                    total_consumption = round(consumption[3]+consumption[4]+consumption[5], 2)
                    one_counter_consumption.append(total_consumption)
                    break
            all_counters_consumption.append(one_counter_consumption)
    return all_counters_consumption



if __name__ == "__main__":
    all_consumptions = get_counters_consumption()
    for num, char in enumerate(all_consumptions, 1):
        print(num, char)


