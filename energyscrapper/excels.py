# Data storage in excel handler
from openpyxl import load_workbook
import os
from dotenv import load_dotenv

load_dotenv()
storage_file = os.getenv('DBEXCEL_PATH')
print(storage_file)

# meters_data_storage =  load_workbook() 