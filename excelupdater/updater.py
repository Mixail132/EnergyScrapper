import psutil
import subprocess
import os
from pywinauto.application import Application
import pyautogui as pg
from dotenv import load_dotenv
import time

load_dotenv()
main_excel_file = os.getenv("TGEXCEL_PATH")
main_excel_title = os.getenv("TGEXCEL_NAME")

names = []
for process in psutil.process_iter():
    name = process.name()
    if name and name in "EXCELExcelexcel":
        break
else:
    subprocess.Popen(["start", main_excel_file], shell=True)
    time.sleep(5)


app = Application().connect(title_re="energy.xlsx")

app[main_excel_title].set_focus()

# pg.hotkey("ctrl","m")

