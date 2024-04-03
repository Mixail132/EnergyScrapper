import psutil
import subprocess
import os
import time
from pyautogui import hotkey
from dotenv import load_dotenv
from pywinauto.application import Application


load_dotenv()
main_excel_file = os.getenv("TGEXCEL_PATH")
main_excel_title = os.getenv("TGEXCEL_NAME")


def check_excel_running():
    """ Scan the system processes and launch Excel if it's not running."""
    for process in psutil.process_iter():
        name = process.name()
        if name and name in "EXCELExcelexcel":
            break
    else:
        subprocess.Popen(["start", main_excel_file], shell=True)


def set_excel_focus():
    """ Finds a particular Excel file and sets focus on the file's window. """
    app = Application().connect(title_re="energy.xlsx")
    app[main_excel_title].set_focus()


def run_excel_macro(key: str):
    """ Presses the preset hotkey combination to run Excel macro. """
    hotkey("ctrl", key)


if __name__ == "__main__":
    check_excel_running()
    time.sleep(5)
    set_excel_focus()
    run_excel_macro("m")
    time.sleep(5)
    run_excel_macro("ь")
