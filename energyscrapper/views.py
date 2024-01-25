import fdb
from datetime import datetime

connect = fdb.connect(
    host='localhost',
    database='C:\Program Files (x86)\Control Center Server\Base\ENERGY.GDB',
    user='sysdba',
    password='masterkey',
    charset="UTF-8",
    fb_library_name='C://Program Files (x86)/Firebird/Firebird_2_1/bin/fbclient.dll'
)

cursor1 = connect.cursor()
cursor2 = connect.cursor()

request_1 = (
"SELECT NAME, SERIALNUM, NUM_DEVICE, NUM_CH FROM CHANNEL "
)
request_2 = (
"SELECT NUM_DEVICE, NUM_CH , DT_DAY,TARIF1, TARIF2, TARIF3 FROM IMPULS4 WHERE DT_DAY='2024-01-01' ORDER BY DT_DAY"
)

cursor1.execute(request_1)
cursor2.execute(request_2)

all_counters_info=[]
for i in  cursor1.fetchall():
    counters_info=[]
    for j in i:
        counters_info.append(str(j)) 
    if not 'R-' in counters_info[0] :
        if not 'R+' in counters_info[0]:
            if not 'А-' in counters_info[0]:
                if not 'A-' in counters_info[0]:
                    all_counters_info.append(counters_info)
for num, char  in enumerate (all_counters_info, 1):
    print(num, char)
    # all_counters_info.append(counters_info)
        # counters_info.append((j[0],j[1],j[2],j[3]))
    # day_energy_total=i[1]+i[2]+i[3]
    # day_date = i[0].strftime("%Y-%m-%d")
    # day_energy=round(day_energy_total,2)
    # print(day_date, day_energy)

# for j in cursor2.fetchall():
#     print(j)
# print(all_counters_info)
