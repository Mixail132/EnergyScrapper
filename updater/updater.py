# Проверка на предмет открытия программ Excel и EnergyControlCenter
import psutil
import ctypes
import sys
import os
from pywinauto.application import Application
import pyautogui as pg
from dotenv import load_dotenv

load_dotenv()
main_excel_file = os.getenv("TGEXCEL_PATH")

for process in psutil.process_iter():
    name = process.name()
    excel = ["EXCEL.EXE", "Excel.exe", "excel.exe"]
    if name not in excel:
        os.startfile(main_excel_file)

app = Application().connect(best_match="excel")
app.window(best_match='excel').set_focus()

#
# #Поиск и закрытие мешающих окон, когда опрос не запущен
# for j in range(18):
#  s=0
#  try:
#     app=Application().connect(best_match=Ewindow2[j])
#     app.window(best_match=Ewindow2[j]).close()
#     s=1
#  except:
#     continue
#
#
# #Поиск и закрытие мешающих окон, когда опрос работает
# for i in range(55):
#  try:
#     app=Application().connect(best_match=Ewindow1[i])
#     app.window(best_match=Ewindow1[i]).close()
#  except:
#     continue
#
# #Проверка условия и сообщение о том, что обновление не выполняется
# app = Application().connect(best_match="Energy Control Center (v.23.15)")           # Поиск окна по заголовку
# if s == 1:
#     ctypes.windll.user32.MessageBoxW(0, " Обновление данных Energy Control Center не выполняется.\n Зайдите в программу и нажмите кнопку 'Обмен'. Данные будут автоматически обновлены  в ночное время", "Autoscreen", 1)
#     sys.exit()
#
#
#
# app = Application().connect(best_match="energy")
# app.window(best_match='energy').set_focus()                # Вывод окна на передний план
#
#
# # Иммитация нажатий мыши для работы программы
# pg.PAUSE=7                     # Задержка между последующими методами библиотеки pg
# pg.rightClick(398,60,3.5)      # EnergyControlCenter (кнопка  "Счетчики")
# pg.rightClick(381,83,3.5)      # EnergyControlCenter (чекбокс "По каналам группы программыСчетчики")
# pg.rightClick(142,122,3.5)     # EnergyControlCenter (чекбокс "По месяцам")
# pg.rightClick(1788,40,3.5)     # EnergyControlCenter (кнопка  "Документ")
# pg.hotkey("ctrl","m")          # Excel (сочетание клавиш для запуска макроса в Excel)
#
#
# # Закрытие окна "Показания счетчиков по дням и месяцам после выгрузки данных"
# app = Application().connect(best_match="Показания счетчиков по дням и месяцам")      # Поиск окна по заголовку
# app.window(best_match='Показания счетчиков по дням и месяцам').close()               # Закрытие окна
#
