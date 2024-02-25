# Here is the main logic
from datetime import datetime, timedelta
from consumptions import get_counters_consumption
from consumptions import filter_counters_consumption
from consumptions import make_consumptions_per_date
from counters import get_counters_info
from excels import put_consumptions_to_excel


def period_energy_handler() -> dict:
    """ 
    Counts the period of needed data,
    pass every single data as a parameter
    to a single day retrieving energy function. 
    """
    data_day = datetime.today()-timedelta(days=31)
    sql_date = data_day.strftime("%Y-%m-%d")
    all_consumption = get_counters_consumption(sql_date)
    counters_info = get_counters_info()
    filtered_consumption = filter_counters_consumption(counters_info, all_consumption)
    needed_consumption = make_consumptions_per_date(sql_date, filtered_consumption)
    put_consumptions_to_excel(needed_consumption)
    return needed_consumption


if __name__ == "__main__":
    period_energy_handler()
