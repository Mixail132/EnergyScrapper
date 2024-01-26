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