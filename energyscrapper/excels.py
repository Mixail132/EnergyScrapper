# Data storage in excel handler
from openpyxl import load_workbook
import os
from dotenv import load_dotenv
<<<<<<< HEAD
from periodviews import period_energy_handler
=======
>>>>>>> c2549eed45b38fff60e074fe0f2421f24525bed1


load_dotenv()


def put_consumptions_to_excel(data_day, counters_data):
    counters_storage_file = os.getenv('DBEXCEL_PATH')
    counters_data_storage =  load_workbook(counters_storage_file) 
    current_date_row = data_day.toordinal()-737328
    counters_numbers={}
    for col_number in range(2, 47):
        counter_number = counters_data_storage.active.cell(row=3, column = col_number).value
        counters_numbers[counter_number] = col_number
    for counter_number, col_number in counters_numbers.items():
        try:
            energy_value = (counters_data[str(counter_number)])
        except KeyError:
            continue
        column_number = counters_numbers[counter_number]  
        counters_data_storage.active.cell(row=current_date_row, column=column_number).value=energy_value       
    counters_data_storage.save(counters_storage_file)


<<<<<<< HEAD
if __name__ == "__main__" :
    counters_data = period_energy_handler()
    put_consumptions_to_excel(counters_data)

=======
>>>>>>> c2549eed45b38fff60e074fe0f2421f24525bed1
