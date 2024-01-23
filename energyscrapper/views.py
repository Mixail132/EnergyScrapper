import fdb

connect = fdb.connect(
    host='localhost',
    database='C:\Program Files (x86)\Control Center Server\Base\ENERGY.GDB',
    user='sysdba',
    password='masterkey',
    charset="UTF-8",
    fb_library_name='C://Program Files (x86)/Firebird/Firebird_2_1/bin/fbclient.dll'
)

cursor = connect.cursor()
request = "SELECT TARIF1, TARIF2, TARIF3 FROM IMPULS4 WHERE NUM_CH=1 AND NUM_SAM=1 ORDER BY DT_DAY"
cursor.execute(request)

for i in  cursor.fetchall():
    print(i)