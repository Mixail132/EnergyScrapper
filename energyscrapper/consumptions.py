# The script gets the energy consumption info
from datetime import datetime, timedelta
from connections import cursor
from counters import get_counters_info


def get_counters_consumption(data_date: str) -> cursor:
    """
    Gets all the energy consumption data from the database.

    :param data_date: the date  from what one's gonna getting the data
    """
    today_date = datetime.today().strftime("%Y-%m-%d")
    request = (f"""
        SELECT 
        NUM_DEVICE,
        NUM_CH, 
        DT_DAY,
        TARIF1, 
        TARIF2, 
        TARIF3 
        FROM IMPULS4 
        WHERE 
        DT_DAY>='{data_date}'
        AND
        DT_DAY<='{today_date}'
        ORDER BY DT_DAY 
        """)
    cursor.execute(request)
    return cursor.fetchall()


def filter_counters_consumption(counters, consumptions):
    one_day_filtered_consumption = {}
    for counter in counters:
        for consumption in consumptions:
            if counter[3] == consumption[1] and counter[2] == consumption[0]:
                one_counter_total_energy = (sum(consumption[3:6]))
                one_day_filtered_consumption[counter[1]] = round(one_counter_total_energy, 2)
                break
    return one_day_filtered_consumption


if __name__ == "__main__":
    example_date = datetime.today()-timedelta(days=3)
    sql_date = example_date.strftime("%Y-%m-%d")
    all_consumptions = get_counters_consumption(sql_date)
    counters_info = get_counters_info()
    filtered = filter_counters_consumption(counters_info, all_consumptions)
    for i, key in enumerate(filtered.items()):
        print(i, key)
    # for num, char in enumerate(all_consumptions, 1):
    #     print(num, char)


