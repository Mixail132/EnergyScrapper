# The script gets the energy consumption info

import fdb
from datetime import datetime, timedelta
from counters import get_counters_info

connect = fdb.connect(
    host='localhost',
    database='C:\Program Files (x86)\Control Center Server\Base\ENERGY.GDB',
    user='sysdba',
    password='masterkey',
    charset="UTF-8",
    fb_library_name='C://Program Files (x86)/Firebird/Firebird_2_1/bin/fbclient.dll'
)

cursor = connect.cursor()
yesterday = datetime.today()-timedelta(days=4)
sql_date = yesterday.strftime("%Y-%m-%d") 
request = (f"SELECT NUM_DEVICE, NUM_CH , DT_DAY,TARIF1, TARIF2, TARIF3 FROM IMPULS4 WHERE DT_DAY='{sql_date}'")
cursor.execute(request)
counters = get_counters_info()
consumptions = cursor.fetchall()


def get_counters_consumption():
    """ Gets energy consumption data from the database, 
        looks for which the data belongs to which counter, 
        makes a list of the summed up data. """
    all_couters_consumption=[]
    for counter in counters:
        for consumption in consumptions:
            one_counter_consumption=[]
            if int(counter[3]) == int(consumption[1]):
                if int(counter[2]) == int(consumption[0]):
                    one_counter_consumption.append(counter[1])
                    total_consumption = round(consumption[3]+consumption[4]+consumption[5], 2)
                    one_counter_consumption.append(total_consumption)
                    break
        all_couters_consumption.append(one_counter_consumption)
    return all_couters_consumption


if __name__ == "__main__":
    consumptions = get_counters_consumption()
    for num, char in enumerate(consumptions, 1):
        print(num, char)


