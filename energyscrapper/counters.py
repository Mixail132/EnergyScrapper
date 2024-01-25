# The script gets energy counters info

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

cursor = connect.cursor()

request = ("SELECT NAME, SERIALNUM, NUM_DEVICE, NUM_CH FROM CHANNEL")


cursor.execute(request)

def get_counters_info():
    all_counters_info=[]
    for i in  cursor.fetchall():
        counters_info=[]
        for j in i:
            counters_info.append(str(j)) 
        if not 'R-' in counters_info[0] :
            if not 'R+' in counters_info[0]:
                if not 'А-' in counters_info[0]:
                    if not 'A-' in counters_info[0]:
                        all_counters_info.append(counters_info)
    return all_counters_info

counters = get_counters_info()
for num, char  in enumerate (counters, 1):
    print(num, char)