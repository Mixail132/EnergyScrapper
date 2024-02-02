# Data storage in excel handler
from openpyxl import load_workbook
import os
import datetime
from dotenv import load_dotenv
from views import filter_retreived_energy


load_dotenv()
counters_storage_file = os.getenv('DBEXCEL_PATH')
counters_data_storage =  load_workbook(counters_storage_file) 
today_date = datetime.datetime.now()


def put_consumptions_to_excel(counters_data):
    current_date_row = today_date.toordinal()-737328
    counters_numbers={}
    for col_number in range(2, 47):
        counter_number = counters_data_storage.active.cell(row=3, column = col_number).value
        counters_numbers[counter_number] = col_number
    # print(counters_numbers[18085116])
    for counter_number, col_number in counters_numbers.items():
        try:
            energy_value = (counters_data[str(counter_number)])
        except KeyError:
            continue
        column_number = counters_numbers[counter_number]  
        counters_data_storage.active.cell(row=current_date_row, column=column_number).value=energy_value       
    counters_data_storage.save(counters_storage_file)


if __name__ == "__main__" :
    counters_data = filter_retreived_energy()
    put_consumptions_to_excel(counters_data)

