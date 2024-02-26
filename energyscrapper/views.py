# Here is the main logic
from datetime import datetime, timedelta
from consumptions import get_counters_consumption
from consumptions import filter_counters_consumption
from consumptions import make_consumptions_per_date
from counters import get_counters_info
from excels import put_consumptions_to_excel

# start_day = datetime.today()
start_day = datetime(2024, 2, 13)


def period_energy_handler() -> dict:
    """
    Gets all the counters' consumption for 31 days.
    Gets all the counters' info, such as counter number, what in counts etc.
    Excludes the reactive energy data and the output energy data.
    Creates a dict where the key is a date and the value is a consumption per the date.
    Writes the given data to Excel file.
    """
    data_day = start_day-timedelta(days=31)
    sql_date = data_day.strftime("%Y-%m-%d")
    all_consumption = get_counters_consumption(sql_date)
    counters_info = get_counters_info()
    filtered_consumption = filter_counters_consumption(counters_info, all_consumption)
    needed_consumption = make_consumptions_per_date(sql_date, filtered_consumption)
    put_consumptions_to_excel(needed_consumption)
    return needed_consumption


if __name__ == "__main__":
    period_energy_handler()
