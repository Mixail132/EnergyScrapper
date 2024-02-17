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


def filter_counters_consumption(counters: list, consumptions: list) -> list:
    """
    Gets the counters info and excludes reactive and given energy from
    all the consumptions. Also match the consumption to the related counter

    :param counters: list of all counters info like this:
    ['Освещение ЩО-8   А+', '19094838', Decimal('2'), Decimal('56')]
    where
    'Освещение ЩО-8   А+'        - consumer and energy type
    '19094838'                   - the counter number
    Decimal('2'), Decimal('56')  - the counter's parameters

    :param consumptions: list of all the consumptions like this:
    (Decimal('1'), Decimal('16'), datetime.datetime(2024, 2, 16, 0, 0), 289.72424316, 149.96900197, 61.81375122)
    where:
    Decimal('1'), Decimal('16'),          -  the counters parameters;
    datetime.datetime(2024, 2, 16, 0, 0), -  the energy consumption date;
    289.724243164063, 149.96900197342, 61.8137512207031 - the energy values for different rates.
    """
    all_days_filtered_consumption = []
    for consumption in consumptions:
        one_day_filtered_consumption = []
        for counter in counters:
            if counter[3] == consumption[1] and counter[2] == consumption[0]:
                one_day_filtered_consumption.append(consumption[2])
                one_day_filtered_consumption.append(counter[1])
                one_counter_total_energy = (sum(consumption[3:6]))
                one_day_filtered_consumption.append(round(one_counter_total_energy, 2))
                break
        if one_day_filtered_consumption:
            all_days_filtered_consumption.append(one_day_filtered_consumption)
    return all_days_filtered_consumption


def make_consumptions_per_date(period_date: str, consumptions: list) -> dict:
    date = datetime.strptime(period_date, "%Y-%m-%d")
    days = (datetime.today() - date).days
    all_days = {}
    for day in reversed(range(days)):
        get_day = date.today() - timedelta(days=day)
        one_day_consumption = {}
        for consumption in consumptions:
            if consumption[0].date() == get_day.date():
                one_day_consumption[consumption[1]] = consumption[2]
        all_days[f'{get_day.date()}'] = one_day_consumption
    return all_days


if __name__ == "__main__":
    example_date = datetime.today()-timedelta(days=3)
    sql_date = example_date.strftime("%Y-%m-%d")
    all_consumptions = get_counters_consumption(sql_date)
    counters_info = get_counters_info()
    filtered = filter_counters_consumption(counters_info, all_consumptions)
    all_consumptions = make_consumptions_per_date(sql_date, filtered)
