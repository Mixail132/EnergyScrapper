# Data storage in excel handler
from openpyxl import load_workbook
from datetime import datetime
from dotenv import load_dotenv
import dirs


load_dotenv()


def put_consumptions_to_excel(counters_data: dict) -> None:
    counters_storage_file = dirs.DB_EXCEL
    counters_data_storage = load_workbook(counters_storage_file)
    for date, counters_values in counters_data.items():
        date_to_paste = datetime.strptime(date, "%Y-%m-%d")
        current_date_row = date_to_paste.toordinal()-737328
        counters_numbers = {}
        for col_number in range(2, 47):
            counter_number = counters_data_storage.active.cell(row=3, column=col_number).value
            counters_numbers[counter_number] = col_number
        for counter_number, col_number in counters_numbers.items():
            try:
                energy_value = (counters_values[str(counter_number)])
            except KeyError:
                continue
            column_number = counters_numbers[counter_number]
            counters_data_storage.active.cell(row=current_date_row, column=column_number).value = energy_value
    counters_data_storage.save(counters_storage_file)
